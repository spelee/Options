
class Asset():

    # TODO:

    def __init__(self, ticker):
        self.description = ticker
        self.ticker = ticker


    def set_description(self, description):
        self.description = description

    def description(self):
        return self.description