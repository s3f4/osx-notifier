import urllib.request, json, os


class Util(object):
    @staticmethod
    def currency(currency):
        """
        currency calculation
        :param currency:
        :return:
        """
        with urllib.request.urlopen(
                "http://free.currencyconverterapi.com/api/v5/convert?q={}&compact=y".format(currency)) as url:
            data = json.loads(url.read().decode())
            return data[currency]["val"]

    @staticmethod
    def notify(title, subtitle, message):
        """
        Mac os x notify caller
        :param title:
        :param subtitle:
        :param message:
        """
        command = 'terminal-notifier -title "{}" -subtitle "{}" -message "{}"'.format(title, subtitle, message)
        os.system(command)

    @staticmethod
    def read_config():
        """
        read config.json file
        :return:
        """
        with open("config.json") as file:
            data = json.load(file)
        return data
