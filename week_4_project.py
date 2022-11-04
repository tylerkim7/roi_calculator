from time import sleep

class roi():
    def __init__(self):
        self.income = {}
        self.expenses = {}
        self.incomeSum = None
        self.expenseSum = None
        self.totalCashFlow = None
        self.costs = {}
        self.costSum = None


    def calcIncome(self):
        while True:
            income = input("\nWhat are your different types of income? Please enter one at a time. Type 'done' when you are finished. ")
            if income.lower().strip() != "done":
                try:
                    incomeAmount = int(input("\nHow much is that income? "))
                    self.income[income] = incomeAmount
                    print(self.income)
                except ValueError:
                    print("\nThat is not a valid income. Please try again.")
            elif income.lower().strip() == "done":
                if self.income:
                    self.incomeSum = sum(self.income.values())
                    print(f"\nYour total income is: ${self.incomeSum}")
                    self.calcExpenses()
                else:
                    print("\nWhen you have a job, please come back!")
                    break


    def calcExpenses(self):
        while True:
            expense = input("\nWhat are your different types of expenses? Please enter one at a time. Type 'done' when you are finished. ")
            if expense.lower().strip() == 'utilities':
                print("\nPlease be more specific.")
            elif expense.lower().strip() != "done":
                try:
                    expensesAmount = int(input("\nHow much is that expense? "))
                    self.expenses[expense] = expensesAmount
                    print(self.expenses)
                except ValueError:
                    print("\nThat is not a valid amount. Please try again.")
            elif expense.lower().strip() == "done":
                if self.expenses:
                    self.expenseSum = sum(self.expenses.values())
                    print(f"\nYour total expenses are: ${self.expenseSum}")
                    self.cashFlow()
                else:
                    print("\nPlease come back later!")
                    break

    def cashFlow(self):
        self.totalCashFlow = self.incomeSum - self.expenseSum
        sleep(1)
        print(f"\nHere is your totaly monthly cash flow: ${self.totalCashFlow}")
        self.cashOnCashRoi()

    def cashOnCashRoi(self):
        while True:
            costs = input("\nWhat are your different types of costs? Please enter one at a time. Type 'done' when you are finished. ")
            if costs.lower().strip() != "done":
                try:
                    costsAmount = int(input("\nHow much is that cost? "))
                    self.costs[costs] = costsAmount
                    print(self.costs)
                except ValueError:
                    print("\nThat is not a valid amount. Please try again.")
            elif costs.lower().strip() == "done":
                if self.costs:
                    self.costSum = sum(self.costs.values())
                    print(f"\nYour total investment is: ${self.costSum}")
                    sleep(1)
                    print(f"\nAfter calculating your cash flow and your total investment costs, your cash on cash ROI is: {((self.totalCashFlow * 12)/self.costSum)* 100}%")
                    break
                else:
                    print("\nPlease come back later!")

                    break


calculateROI = roi()

def run():
    while True:
        response = input("\nWould you like to calculate your cash on cash ROI? yes/no: ")
        if response.lower().strip() == 'yes':
            calculateROI.calcIncome()
        elif response.lower().strip() == 'no':
            print("\nHave a nice day!")
        else:
            print("\nThat is not a valid response! Please try again!")


run()