class Account:
    #static method
    bank_name="ITVBank"
     
     
    def __init__(self,account_number,balance,pin):        
        self.__account_number = account_number
        self.__balance = balance
        self.__pin = pin
        
        
    def check_balance(self,pin):        
        if pin == self.__pin:
            return self.__balance
        else:
           return -1
       
    def transfer_balance(self,other,amount,pin):        
        if pin == self.__pin:            
            if amount <= self.__balance:                
                self.__balance -= amount
                other.__balance += amount                
            else:
                return -2
        else:
            return -1
    @staticmethod
    def emi(loan_amount,year):
        months=year*12
        monthly_emi = loan_amount/months
        return monthly_emi