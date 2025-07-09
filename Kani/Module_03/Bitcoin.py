class CreditCardPayment:
    def pay_credit(self, amount):
        print(f"Paid ${amount} with Credit Card")

class BitcoinPayment:
    def pay_bitcoin(self, btc_amount):
        print(f"Paid {btc_amount} BTC")

class Bit_Adapter:
    def __init__(self,currency):
        self.currency = currency

    def pay(self,btc_amount):
        self.currency.pay_bitcoin(btc_amount)


bitcoin = BitcoinPayment()

bit_apt = Bit_Adapter(bitcoin)

bit_apt.pay(100)