from account import Account

class SavingAccount(Account):

    def __init__(self,account_number,balance,pin,min_balance):
        super().__init__(account_number,balance,pin)
        self.min_balance = min_balance
    
    #method over riding
    def transfer_balance(self,other,amount,pin):
        if pin == self._Account__pin:          
            if (self._Account__balance - amount) >= self.min_balance:                
                self._Account__balance -= amount
                other._Account__balance += amount                
            else:
                return -2
        else:
            return -1
    
