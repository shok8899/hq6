"""WebSocket server for MT4 client connections."""

import json
import time
from simple_websocket_server import WebSocket, WebSocketServer

class MT4Handler(WebSocket):
    price_manager = None
    
    def handle(self):
        """Handle incoming messages from MT4 clients."""
        pass  # We don't process incoming messages
        
    def connected(self):
        """Handle client connection."""
        print(f"New MT4 client connected from {self.address}")
        
    def handle_close(self):
        """Handle client disconnection."""
        print(f"MT4 client disconnected from {self.address}")

class MT4Server:
    def __init__(self, host, port, price_manager):
        MT4Handler.price_manager = price_manager
        self.server = WebSocketServer(host, port, MT4Handler)
        self.running = False
        
    def start(self):
        """Start the MT4 WebSocket server."""
        def broadcast_prices():
            while self.running:
                try:
                    prices = MT4Handler.price_manager.get_prices()
                    message = json.dumps({
                        "timestamp": int(time.time() * 1000),
                        "prices": prices
                    })
                    for client in self.server.connections.copy():
                        client.send_message(message)
                    time.sleep(0.1)  # Send updates every 100ms
                except Exception as e:
                    print(f"Error broadcasting prices: {e}")
                    
        self.running = True
        broadcast_thread = threading.Thread(target=broadcast_prices)
        broadcast_thread.daemon = True
        broadcast_thread.start()
        
        print(f"MT4 Server started on port {self.server.port}")
        self.server.serve_forever()
        
    def stop(self):
        """Stop the MT4 WebSocket server."""
        self.running = False
        self.server.close()