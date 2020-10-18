from abc import ABC, abstractmethod
class bike(ABC):
    def reciept(self, amount):
        print("Your total cost: ",amount)

    @abstractmethod
    def chargeAmount(self, amount):
        pass

class CreditCardPayment(bike):
    def chargeAmount(self, amount):
        print('Your total cost of {} exeeds your 200 dollar limit'.format(amount))


obj = CreditCardPayment()
obj.reciept("$500")
obj.chargeAmount("$500")
