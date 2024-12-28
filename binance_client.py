"""Handles Binance WebSocket connection and price updates."""

import json
import time
import threading
import requests
from simple_websocket_server import WebSocket, WebSocketServer
from config import BINANCE_WS_URL, BINANCE_REST_URL

class BinanceClient:
    def __init__(self, price_manager, symbols):
        self.price_manager = price_manager
        self.symbols = symbols
        self.running = False
        
    def start(self):
        """Start price updates using REST API polling."""
        self.running = True
        self._start_price_updates()
        
    def stop(self):
        """Stop price updates."""
        self.running = False
        
    def _start_price_updates(self):
        """Poll prices using REST API."""
        def update_loop():
            while self.running:
                try:
                    # Get prices for all symbols
                    for symbol in self.symbols:
                        response = requests.get(
                            f"{BINANCE_REST_URL}/ticker/price",
                            params={"symbol": symbol}
                        )
                        if response.status_code == 200:
                            data = response.json()
                            self.price_manager.update_price(data["symbol"], data["price"])
                    time.sleep(1)  # Update every second
                except Exception as e:
                    print(f"Error updating prices: {e}")
                    time.sleep(5)  # Wait before retrying
                    
        thread = threading.Thread(target=update_loop)
        thread.daemon = True
        thread.start()