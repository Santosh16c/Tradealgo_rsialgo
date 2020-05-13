import alpaca_trade_api as tradeapi
from alpaca_trade_api import StreamConn
import threading
import time
import datetime
import logging
import argparse
import csv
from rsi_algo import RsiAlgo
import time


# API KEYS
# region
API_KEY = "ENTER API KEY"
API_SECRET = "ENTER SCERET"
APCA_API_BASE_URL = "https://paper-api.alpaca.markets"


# Create tickers_list by opening portfolio CSV and addtion ticker symbol in each row to the list.
tickers_list = []
with open('ARK_INNOVATION_ETF_ARKK_HOLDINGS.csv', newline='') as csvfile:  # open file
    # create csvreader using file
    portfolio = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in portfolio:  # for every row
        # add the third element in the row to tickers_list
        tickers_list.append(row[3])

print("Generated tickers_list: ", tickers_list)

# Run the Buy&sell class

rsi_algo = RsiAlgo(API_KEY, API_SECRET, APCA_API_BASE_URL)
while True:
    print("Running @ TS: ", time.ctime())
    rsi_algo.run(tickers_list)
    print("Sleeping for 60*60 seconds")
    time.sleep(60*60)
