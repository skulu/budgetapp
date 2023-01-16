# Budget App

A simple budgeting app.

Budget catergories can be instantiated based on different budget categories like so:

`Category('food')`

You can perform deposits (`deposit(amount, description)`), withdrawals (`withdraw(amount, description)`), transfers (`transfer(amount, category)`). Checks are performed to ensure that there are sufficient funds before transactions are confirmed.

You can also get your balance via the `get_balance()` method.

See: https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app
