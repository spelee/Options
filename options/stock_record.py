import options.asset_record

class Stock(options.asset_record.Asset):

    def __init__(self, ticker):
        super().__init__(ticker)

    def bloomberg_ticker(self):
        return self.ticker + " Equity"

