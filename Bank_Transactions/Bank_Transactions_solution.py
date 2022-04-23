class Account:
    accntNo = 0
    accntName = " "
    accntBalance = 0

    def __init__(self, no, na, bal):
        self.accntNo = no
        self.accntName = na
        self.accntBalance = bal

class AccountDemo:
    def __init__(self):
        pass

    def deposit(self, obj, amt):
        obj.accntBalance += amt
        return obj.accntBalance

    def withdraw(self, obj, amt):
        if obj.accntBalance-amt>=1000:
            obj.accntBalance-amt
        else:
            print("No Adequate balance")


accno=int(input())
accname = input()
accbal =int(input())
x= Account(accno, accname, accbal)
depoamt = int(input())
withdamt = int(input())
y = AccountDemo()

print(y.deposit(x, depoamt))
y.withdraw(x, withdamt)



