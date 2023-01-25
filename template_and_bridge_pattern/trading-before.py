from typing import List

#! the class has too many responsibilities
#! You could use the strategy pattern for sell, buy stc. -> that would leade to lots of classes
#! You can use the template method -> the process is the same (check price, check if buy or sell etc.),
#! but the strategy to use to etermine if buy/sell maybe different
#! Create a class for the main process, and abstract methods for different part of this process
#! We also decouple the process from the actual strategies
class Application:

    def __init__(self, trading_strategy = "average"):
        self.trading_strategy = trading_strategy

    def connect(self):
        print(f"Connecting to Crypto exchange...")

    def get_market_data(self, coin: str) -> List[float]:
        return [10, 12, 18, 14]

    def list_average(self, l: List[float]) -> float:
        return sum(l) / len(l)

    def should_buy(self, prices: List[float]) -> bool:
        if self.trading_strategy == "minmax":
            return prices[-1] == min(prices)
        else:
            return prices[-1] < self.list_average(prices)

    def should_sell(self, prices: List[float]) -> bool:
        if self.trading_strategy == "minmax":
            return prices[-1] == max(prices)
        else:
            return prices[-1] > self.list_average(prices)

    def check_prices(self, coin: str):
        self.connect()
        prices = self.get_market_data(coin)
        should_buy = self.should_buy(prices)
        should_sell = self.should_sell(prices)
        if should_buy:
            print(f"You should buy {coin}!")
        elif should_sell:
            print(f"You should sell {coin}!")
        else:
            print(f"No action needed for {coin}.")

application = Application("average")
application.check_prices("BTC/USD")
