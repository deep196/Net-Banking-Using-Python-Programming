from datetime import datetime as dt
from invalid_pin_error import InvalidPinError
from insufficient_balance_error import InsufficientBalanceError

class AccountA:
    bank_name="ITVBank"
   
    def __init__(self,account_number,balance,pin):
        
        self.__account_number = account_number
        self.__balance = balance
        self.__pin = pin
        file = open(str(account_number) + ".txt","x")
        file.close()
        
    def check_balance(self,pin):
        
        if pin == self.__pin:
            file = open(str(self.__account_number) + ".txt","a")
            file.write("check balance at {} \n".format(dt.now()))
            file.flush()
            file.close()
            return self.__balance
        else:
           raise InvalidPinError
    
    def transfer_balance(self,other,amount,pin):
        
        if pin == self.__pin:
            
            if amount <= self.__balance:
                
                self.__balance -= amount
                other.__balance += amount
                file = open(str(self.__account_number) + ".txt","a")
                file.write("fund transfer at - {} , to account - {} , closing balance - {}\n".format(dt.now(),other.__account_number,self.__balance))
                file.flush()
                file.close()
                
                file = open(str(other.__account_number) + ".txt","a")
                file.write("fund received at - {} , from account - {} , closing balance - {}\n".format(dt.now(),self.__account_number,other.__balance))
                file.flush()
                file.close()
                
            else:
                raise InsufficientBalanceError
        else:
            raise InvalidPinError
    
    @staticmethod 
    def calculate_emi(loan_amount,year):
         
         months = year* 12
         monthly_emi = loan_amount/months
         return monthly_emi