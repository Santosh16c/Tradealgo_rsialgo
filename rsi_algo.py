import alpaca_trade_api as tradeapi
from alpaca_trade_api import StreamConn
import threading
import time
import datetime
import logging
import argparse
import csv
import talib
import numpy
import talib


class RsiAlgo:
    def __init__(self, key, secret, base_url):
        self.alpaca = tradeapi.REST(key, secret, base_url, api_version='v2')

    def do_rsi(self, ticker):
        print("-------------------------------------------------------")
        print('Running RSI Algo for: ', ticker)
        barMap = self.alpaca.get_barset(ticker, 'minute', limit=30)
        ticker_bars = barMap[ticker]
        prices = []
        for bar in ticker_bars:
            prices.append(bar.c)

        rsi = talib.RSI(numpy.asarray(prices))
        print("RSI: ", rsi[-1])
        latest_rsi = rsi[-1]

        # if RSI > 80, sell, if RSI < 19 buy
        if latest_rsi > 80:
            print("Submitting sell order")
            try:
                self.alpaca.submit_order(ticker, 50, 'sell', 'market', 'day')
            except Exception as e:
                print("Exception trying to submit sell order", e)
        else:
            if latest_rsi < 19:
                print("Submitting buy order")
                try:
                    self.alpaca.submit_order(
                        ticker, 50, 'buy', 'market', 'day')
                except Exception as e:
                    print("Exception trying to submit buy order", e)

        print("-------------------------------------------------------")

    def run(self, tickers_list):
        for symbol in tickers_list:
            self.do_rsi(symbol)
