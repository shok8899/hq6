"""Manages price data for crypto symbols."""

class PriceManager:
    def __init__(self, symbols):
        self.prices = {}
        for symbol in symbols:
            self.prices[symbol] = {"bid": 0, "ask": 0}

    def update_price(self, symbol, price):
        """Update price with spread for a given symbol."""
        try:
            price = float(price)
            spread = price * 0.001  # 0.1% spread
            self.prices[symbol] = {
                "bid": price - spread/2,
                "ask": price + spread/2
            }
        except (ValueError, TypeError) as e:
            print(f"Error updating price for {symbol}: {e}")

    def get_prices(self):
        """Get current prices for all symbols."""
        return self.prices