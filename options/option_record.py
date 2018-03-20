import datetime

import options.asset_record

class Option(options.asset_record.Asset):

    def __init__(self, ticker, strike, type, expiration):
        super().__init__(ticker)
        self.strike = strike
        self.type = type
        self.expiration = expiration
        self.description = ticker + " " + str(expiration) + " " + str(strike) + " " + type

    def __str__(self):
        return self.description

    def bloomberg_ticker(self):
        return self.ticker + " Equity " + self.expiration.strftime("%m/%d/%y") + " " + self.type[0] + str(self.strike)




