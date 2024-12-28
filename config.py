"""Configuration settings for the crypto market data server."""

# Server Configuration
MT4_PORT = 8085

# Trading Symbols
SYMBOLS = [
    "BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "DOGEUSDT",
    "XRPUSDT", "DOTUSDT", "UNIUSDT", "LTCUSDT", "LINKUSDT",
    "SOLUSDT", "MATICUSDT", "AVAXUSDT", "FILUSDT", "ATOMUSDT"
]

# Binance API
BINANCE_WS_URL = "ws://stream.binance.com/ws"
BINANCE_REST_URL = "https://api.binance.com/api/v3"