import statistics
# Python has the module called statistics and we can use this module to do all
# the statistical calculations. However, to learn how to make function and
# reuse function let us try to develop a program, which calculates the measure
# of central tendency of a sample (mean, median, mode) and measure of variability
# (range, variance, standard deviation). In addition to those measures, find the min,
# max, count, percentile, and frequency distribution of the sample. You can create a
# class called Statistics and create all the functions that do statistical calculations
# as methods for the Statistics class. Check the output below.
class PersonAccount:
    def __init__(self, firstname, lastname, properties):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = set()
        self.expenses = set()
        self.properties = properties
    def total_income(self):
        total = 0
        for income in self.incomes:
            total += income[0]
        return total
    def total_expenses(self):
        total = 0
        for expense in self.expenses:
            total += expense[0]
        return total
    def add_income(self, income):
        self.incomes.add(income)
    def add_expenses(self, expense):
        self.expenses.add(expense)
    def account_balance(self):
        return self.total_income - self.total_expenses

