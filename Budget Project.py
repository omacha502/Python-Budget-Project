class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def __str__(self):
        title = "*" * ((30 - len(self.name)) // 2) + self.name + "*" * ((30 - len(self.name)) // 2)
        for item in self.ledger:
            left = item['description'][:23]
            right = "{:.2f}".format(item['amount'])
            title += "\n" + left + " " * (30 - len(left) - len(right)) + right
        title += "\nTotal: " + "{:.2f}".format(self.balance)

        return title

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False

        self.ledger.append({"amount": -amount, "description": description})
        self.balance -= amount

        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False

        self.withdraw(amount, "Transfer to {}".format(category.name))
        category.deposit(amount, "Transfer from {}".format(self.name))

        return True

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        return True


food = Category("Food")
clothing = Category("Clothing")
Entertainment = Category("Entertainment")

food.deposit(1000, "initial deposit")
clothing.deposit(1000, "initial deposit")
Entertainment.deposit(1000, "initial deposit")

food.transfer(200, clothing)
food.withdraw(200, "Food stuffs")
food.withdraw(300, "More food")

clothing.transfer(200, Entertainment)
clothing.withdraw(50, "Clothing expenses")
clothing.withdraw(100, "More expenses")

Entertainment.transfer(200, food)
Entertainment.withdraw(500, "Party")

print(food)
print(clothing)
print(Entertainment)
