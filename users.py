class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawl(self, amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


klaus = User("Klaus")
sara = User("Sara")
enio = User("Enio")

klaus.make_deposit(200)
klaus.make_deposit(200)
klaus.make_deposit(100)
klaus.make_withdrawl(45)
klaus.display_user_balance()

sara.make_deposit(500)
sara.make_deposit(500)
sara.make_withdrawl(50)
sara.make_withdrawl(100)
sara.display_user_balance()

enio.make_deposit(3500)
enio.make_withdrawl(100)
enio.make_withdrawl(200)
enio.make_withdrawl(150)
enio.display_user_balance()

sara.transfer_money(400, klaus)
