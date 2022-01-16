from accountA import AccountA
from datetime import datetime as dt
from invalid_pin_error import InvalidPinError
from insufficient_balance_error import InsufficientBalanceError

class SavingAccount(AccountA):

    def __init__(self,account_number,balance,pin,min_balance):
        super().__init__(account_number,balance,pin)
        self.min_balance = min_balance
        file = open(str(account_number) + "txt","x")
        file.close()
    
    # method overriding    
    def transfer_balance(self,other,amount,pin):
        
        if pin == self._Account__pin:
             
            if (self._Account__balance - amount) >= self.min_balance:
                
                self._Account__balance -= amount
                other._Account__balance += amount
                file = open(str(self.__account_number) + ".txt","a")
                file.write("fund transfer at - {} , to account - {} , closing balance - {}\n".format(dt.now(),other.__account_number,self.__balance))
                file.flush()
                file.close()
                
                file = open(str(other.__account_number) + ".txt","a")
                file.write("fund received at - {} , from account - {} , closing balance - {}\n".format(dt.now(),self.__account_number,other.__balance))
                file.flush()
                file.close()
                
            else:
                raise InvalidPinError
        else:
            raise InsufficientBalanceError
      