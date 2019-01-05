import ccxt
import sys


class Exchange(object):
    exchange = None

    def __init__(self, exchange_class=None, apiKey=None, secret=None):
        """

        :param exchange_class:
        :param apiKey:
        :param secret:
        """

        module = __import__("ccxt")

        if exchange_class is None:
            exchange_class = "binance"
        try:
            class_ = getattr(module, exchange_class)
            self.exchange: ccxt.bittrex = class_()
        except Exception as err:
            print(type(err), "", err)
            sys.exit(0)

        if apiKey is not None:
            self.exchange.apiKey = apiKey
        if secret is not None:
            self.exchange.secret = secret

    def fetch_markets(self):
        """

        :return:
        """
        return self.exchange.fetch_markets()

    def fetch_balance(self, params={}):
        """

        :param params:
        :return:
        """
        return self.exchange.fetch_balance(params)

    def fetch_order_book(self, symbol, limit=None, params={}):
        """

        :param symbol:
        :param limit:
        :param params:
        :return:
        """
        return self.exchange.fetch_order_book(symbol, limit, params)

    def fetch_currencies(self, params={}):
        """

        :param params:
        :return:
        """
        return self.exchange.fetch_currencies(params)

    def fetch_tickers(self, symbols=None, params={}):
        """

        :param symbols:
        :param params:
        :return:
        """
        return self.exchange.fetch_tickers(symbols, params)

    def fetch_ticker(self, symbol, params={}):
        """

        :param symbol:
        :param params:
        :return:
        """
        return self.exchange.fetch_ticker(symbol, params)

    def fetch_trades(self, symbol, since=None, limit=None, params={}):
        """

        :param symbol:
        :param since:
        :param limit:
        :param params:
        :return:
        """
        return self.exchange.fetch_trades(symbol, since, limit,
                                          params)

    def fetch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}):
        """
        :param symbol:
        :param timeframe:
        :param since:
        :param limit:
        :param params:
        :return:
        """
        return self.exchange.fetch_ohlcv(symbol, timeframe, since, limit,
                                         params)

    def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        """
        fectch open orders
        :param symbol:
        :param since:
        :param limit:
        :param params:
        :return:
        """
        return self.exchange.fetch_open_orders(symbol, since, limit,
                                               params)

    def create_order(self, symbol, type, side, amount, price=None, params={}):
        """
        create new order
        :param symbol:
        :param type:
        :param side:
        :param amount:
        :param price:
        :param params:
        :return:
        """
        return self.exchange.create_order(symbol, type, side, amount, price,
                                          params)

    @staticmethod
    def get_order_id_field():
        return 'uuid'

    def cancel_order(self, id, symbol=None, params={}):
        """
        cancel order with id
        :param id:
        :param symbol:
        :param params:
        :return:
        """
        return self.exchange.cancel_order(id, symbol, params)

    def fetch_order(self, id, symbol=None, params={}):
        """
        fetch order with id
        :param id:
        :param symbol:
        :param params:
        :return:
        """
        return self.exchange.fetch_order(id, symbol, params)

    def fetch_closed_orders(self, symbol=None, since=None, limit=None, params={}):
        """
        fetch closed orders
        :param symbol:
        :param since:
        :param limit:
        :param params:
        :return:
        """
        return self.exchange.fetch_closed_orders(symbol, since, limit,
                                                 params)

    def fetch_deposit_address(self, code, params={}):
        """
        :param code: CODE=XRP,ETC ex
        :param params:
        :return:
        """
        return self.exchange.fetch_deposit_address(code, params)

    def withdraw(self, code, amount, address, tag=None, params={}):
        self.exchange.withdraw(code, amount, address, tag, params)
