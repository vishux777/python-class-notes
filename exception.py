'''a=5
b=0
try:
    print("open resource")
    print(a/b)
    print("close resource")
except ZeroDivisionError as e:
    print("You cannot divide by 0")
print("Good Bye")
# except Exception'''
class  BalanceException(Exception):
    pass
'''def CheckBalance():
    money=10000
    withdraw=8000
    Balance=money-withdraw
    print(Balance)
CheckBalance()'''
try:
    money=10000
    withdraw=9000
    balance=money-withdraw
    if (balance<=2000):
        raise BalanceException('Insufficient Balance')
    print(balance)
    except BalanceException as e:
        print(e)
