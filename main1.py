from accountA import AccountA
from invalid_pin_error import InvalidPinError
from insufficient_balance_error import InsufficientBalanceError

account1 = AccountA(1234,10000,123)

account2 = AccountA(5678,5000,321)

try:
    account1.check_balance(345)
except InvalidPinError:
    print("Pin is wrong")

account2.check_balance(321)


account1.transfer_balance(account2,2000,123)

account1.check_balance(123)

account2.check_balance(321)


# static members can be accessed directly using class name

AccountA.bank_name

AccountA.calculate_emi(100000,1)

from saving_account import SavingAccount

account3 = SavingAccount(1234,10000,123,5000)
account4 = SavingAccount(5678,5000,321,5000)


account3.check_balance(123)
account4.check_balance(321)


account3.transfer_balance(account4,2000,123)

account3.check_balance(123)
account4.check_balance(321)
