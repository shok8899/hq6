"""Main entry point for the crypto market data server."""

import threading
from config import MT4_PORT, SYMBOLS
from price_manager import PriceManager
from binance_client import BinanceClient
from mt4_server import MT4Server

def main():
    # Initialize components
    price_manager = PriceManager(SYMBOLS)
    binance_client = BinanceClient(price_manager, SYMBOLS)
    mt4_server = MT4Server('localhost', MT4_PORT, price_manager)
    
    try:
        print("Starting Crypto Market Data Server...")
        print("Supported symbols:", ", ".join(SYMBOLS))
        
        # Start Binance price updates
        binance_client.start()
        
        # Start MT4 server
        mt4_server.start()
        
    except KeyboardInterrupt:
        print("\nShutting down server...")
        binance_client.stop()
        mt4_server.stop()
    except Exception as e:
        print(f"Error starting server: {e}")

if __name__ == "__main__":
    main()