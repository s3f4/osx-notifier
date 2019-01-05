from exchange import Exchange
import ccxt, time
from util import Util


class Execute(object):
    exchange = None
    config = None

    def __init__(self):
        """

        """
        self.config = Util.read_config()
        self.exchange = Exchange("binance",
                                 self.config["binance_api_key"],
                                 self.config["binance_api_secret"])

    def follow_notify(self):
        if self.config["follow"] is not None:
            for follow in self.config["follow"]:
                tick = self.exchange.fetch_ticker(follow)["close"]
                Util.notify(title=follow, subtitle="%.08f" % tick, message="")
                time.sleep(4)

    def balances_and_btc(self):
        """

        :return:
        """
        return self.exchange.fetch_balance()["info"]["balances"], float(
            self.exchange.fetch_ticker("BTC/" + self.config["stable"])["close"])

    def notification_loop(self):
        """

        """
        minute = 0
        currency = 0

        while True:

            self.follow_notify()
            balances, BTC_Stable = self.balances_and_btc()
            TotalBTCBalance = 0.0

            for balance in balances:
                amount = float(balance['free']) + float(balance["locked"])
                if amount <= 0.0:
                    continue

                if balance["asset"] != "BTC":
                    try:
                        Asset_BTC = float(self.exchange.fetch_ticker(balance["asset"] + "/BTC")["close"])
                        BTCBalance = Asset_BTC * amount
                        TotalBTCBalance += BTCBalance
                        if BTCBalance >= 0.01:
                            Util.notify(title=balance["asset"], subtitle="Amount : {}".format("%.4f" % amount),
                                        message=balance["asset"] + "/BTC : {}".format("%.8f" % Asset_BTC))
                            time.sleep(4)
                    except ccxt.errors.ExchangeError:
                        pass
                else:
                    TotalBTCBalance += amount

            USDBalance = TotalBTCBalance * BTC_Stable

            if currency == 0 or minute % 30 == 0:
                currency = Util.currency(self.config["currency"])

            Util.notify(title='BTC : {} - {}'.format("%.4f" % TotalBTCBalance, "%.2f" % BTC_Stable),
                        subtitle='USD : {}'.format("%.4f" % USDBalance),
                        message='`echo TRY : {} &&'.format(
                            "%.4f" % (USDBalance * currency)) + ' echo USD/TRY: ' + str(currency) + '`')

            time.sleep(60)
            minute += 1


if __name__ == '__main__':
    try:
        execute = Execute()
        execute.notification_loop()
    except:
        print("An error occured")
