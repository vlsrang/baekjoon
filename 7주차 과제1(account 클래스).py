import random

class Account:
    def __init__(self, name, balance):
        self.name=name
        self.balance=balance
        self.bank="SKK은행"
        num1=random.randint(0,9999)
        num2=random.randint(0,999)
        num3=random.randint(0,999999)
        num1=str(num1).zfill(4)
        num2=str(num2).zfill(3)
        num3=str(num3).zfill(6)
        self.account_number = num1 + "-" + num2 + "-" + num3



###### do not edit here ####### 
person = Account("철수", 1000)
print(person.name)
print(person.balance)
print(person.bank)
print(person.account_number)

