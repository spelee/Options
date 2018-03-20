import datetime
import sys

import pandas as pd

from options.option_record import Option
from options.stock_record import Stock

filename = "../sample/sample_exposure_report.csv"

records = pd.read_csv(filename)
options = []
stocks = []

for idx, row in records.iterrows():
    """
    "Ticker"
    "BloombergTicker"
    "Instrument Subtype"
    "Maturity Date"
    "Option Type"
    "Option Strike"
    "Description"
    "Long/Short Position"
    "Quantity"
    """

    try:
        inst_type = row["Instrument Subtype"]
        if inst_type == "Equity":
            #print("Stock:{}".format(row))
            pass
        elif inst_type == "Equity Option":
            dt = row["Maturity Date"].split("/")
            expiration = datetime.date(int(dt[2]),int(dt[0]),int(dt[1]))
            opt_type = "P" if row["Option Type"] == "Put" else "C"
            opt_x = row["Option Strike"]
            opt_ticker = row["Ticker"]
            options.append(Option(opt_ticker, opt_x, opt_type, expiration))

        else:
            # TODO: This should be logged ito a file
            print("Unknown type: {}-{}".format(idx, row), file=sys.stderr)
    except KeyError as ke:
        print("Table missing columns: {}".format(ke), file=sys.stderr)


for o in options:
    print("->{}".format(o.bloomberg_ticker()))

