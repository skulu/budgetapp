class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        printout = ''
        namelen = len(str(self.category))
        stars = (30-namelen)/2
        if stars%1 != 0:
            printout += int(stars)*'*'
            printout += f'{self.category}'
            printout += (int(stars) + 1)*'*' + '\n'
        else:
            printout += int(stars)*'*' + f'{self.category}' + int(stars)*'*' + '\n'

        for txn in self.ledger:
            if len(txn['description']) <= 23:
                printout += txn['description'] + (23-len(txn['description']))*' '
            else:
                printout += txn['description'][0:23]
                
            spaces = 7-len(f"{txn['amount']:.2f}")
            printout += (spaces*' ' + f"{txn['amount']:.2f}" + '\n')

        printout += f'Total: {self.get_balance()}'
        
        return printout

    def category_name(self):
        return f'{self.category}'
    
    def deposit(self, amount, desc=''):
        self.ledger.append({'amount': amount, 'description': desc})

    def withdraw(self, amount, desc=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': desc})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for txn in self.ledger:
            balance += txn['amount']

        return balance

    def total_spent(self):
        total = 0
        for txn in self.ledger:
            if txn['amount'] < 0:
                total -= txn['amount']
        return total
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            desc = f'Transfer to {category.category_name()}'
            self.withdraw(amount, desc)
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        else:
            return False

    def check_funds(self, amount):
        balance = self.get_balance()
        if balance >= amount:
            return True
        else:
            return False
    
def create_spend_chart(categories):
    total = 0
    spends = []
    for cat in categories:
        total += cat.total_spent()
        spends.append(cat.total_spent())

    pct = [(spend/total * 100)//10*10 for spend in spends]
    pct = [int(x) for x in pct]
    printout = 'Percentage spent by category\n'

    for i in range(100,-10,-10):
        if (len(str(i))) < 3: printout += ' '
        if (len(str(i))) < 2: printout += ' '
        printout += (str(i) + '| ')
        indices = [True if x >= i else False for x in pct]

        for idx in indices:
            if idx:
                printout += 'o  '
            else:
                printout += '   '

        printout += '\n'

    printout += '    -' + '---'*len(categories) + '\n'
    printout += '     '

    wordlength = [len(cat.category_name()) for cat in categories]
    maxlength = max(wordlength)
    
    for i in range(maxlength):
        for j in range(len(categories)):
            if i < wordlength[j]:
                printout += (str(categories[j].category_name())[i] + '  ')
            else:
                printout += '   '
        if i != maxlength-1: printout += '\n     '

    return printout
