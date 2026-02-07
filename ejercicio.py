class Stock:
    def __init__(self, name, price):
        self.name = name
        self.current_price = price

    def update_price(self, new_price):
        self.current_price = new_price

    def __str__(self):
        return f"Stock: {self.name}, Current Price: ${self.current_price:.2f}"
    

class Portafolio:
    def __init__(self, cash):
        self.stocks: {Stock : float} = {}
        self.allocation: {Stock : float} = {}
        self.__cash = cash

    @property
    def cash(self):
        return self.__cash
    
    @cash.setter
    def cash(self, value):
        if value < 0:
            raise ValueError("Cash cannot be negative.")
        self.__cash = value

    def set_allocation(self, allocation:dict):
        self.allocation = allocation

    def add_stock(self, stock : Stock, amount : float = 0):
        self.stocks[stock] = amount

    def total_value(self):
        total_value = self.cash
        for stock, amount in self.stocks.items():
            total_value += stock.current_price * amount
        return total_value

    def buy_stock(self, stock : Stock , amount : float):
        stock_price = stock.current_price
        total_cost = stock_price * amount
        if self.cash >= total_cost:
            self.cash -= total_cost
            if stock in self.stocks:
                self.stocks[stock] += amount
            else:
                self.stocks[stock] = amount
            print(f"Bought {amount} of {stock.name} for ${total_cost:.2f}.")
        else:
            print("Not enough cash to complete the purchase.")

    def sell_stock(self, stock : Stock, amount : float):
        if stock in self.stocks:
            stock_price = stock.current_price
            total_revenue = stock_price * amount
            self.cash += total_revenue
            self.stocks[stock] -= amount
            print(f"Sold {amount} of {stock.name} for ${total_revenue:.2f}.")
        else:
            raise ValueError(f"Stock {stock.name} not found in portfolio.")

    def rebalance(self):
        buy_actions, sell_actions = self.calculate_trades()
        self.execute_trades(sell_actions, buy_actions)

    def calculate_trades(self):
        total_value = self.total_value()
        buy_actions = {}
        sell_actions = {}

        for stock, target_percentage in self.allocation.items():
            if stock in self.stocks:
                current_value = stock.current_price * self.stocks[stock]
                target_value = total_value * target_percentage
                difference = target_value - current_value

                if difference > 0:
                    buy_actions[stock] = difference
                elif difference < 0:
                    sell_actions[stock] = -difference

        return buy_actions, sell_actions

    def execute_trades(self, sell_actions, buy_actions):
        # first sell stocks that are over the target allocation
        for stock, difference in sell_actions.items():
            if stock in self.stocks:
                amount_to_sell = difference / stock.current_price
                self.sell_stock(stock, amount_to_sell)

        # then buy stocks that are under the target allocation
        for stock, difference in buy_actions.items():
            if difference > 0:
                amount_to_buy = difference / stock.current_price
                self.buy_stock(stock, amount_to_buy)
                
  

    def __str__(self):
        return f"Portfolio Cash: ${self.cash:.2f}, Stocks: {[str(stock) for stock in self.stocks.values()]}"



if __name__ == "__main__":
    # Create some stocks
    stock_a = Stock("AAPL", 150.00)
    stock_b = Stock("GOOGL", 2800.00)
    stock_c = Stock("AMZN", 3400.00)

    # Create a portfolio with $10,000 cash
    portfolio = Portafolio(10000)

    # Set target allocation for the stocks
    portfolio.set_allocation({
        stock_a: 0.5,  # 50% in AAPL
        stock_b: 0.3,  # 30% in GOOGL
        stock_c: 0.2   # 20% in AMZN
    })

    # Add stocks to the portfolio
    portfolio.add_stock(stock_a)
    portfolio.add_stock(stock_b)
    portfolio.add_stock(stock_c)

    # Rebalance the portfolio to meet the target allocation
    portfolio.rebalance()

    # Print the final state of the portfolio
    print(portfolio)





