class RentalProperty():

    def __init__(self, income, expenses, cash_flow, roi):
        self.income = income
        self.expenses = expenses
        self.cash_flow = cash_flow
        self.roi = roi
    def calculate_cash_flow(self):
        self.cash_flow = self.income - self.expenses
        return self.cash_flow

    def calculate_roi(self):
        if self.income > 0:
            self.roi = (self.cash_flow / self.income) * 100
        else:
            self.roi = 0
        return self.roi 

class Income:

    def __init__(self, rental_income, other_income):
        self.rental_income = rental_income
        self.other_income = other_income

class Expenses:
    def __init__(self, property_taxes, insurance, maintenance):
        self.property_taxes = property_taxes
        self.insurance = insurance
        self.maintenance = maintenance

class Calculator:
    @staticmethod
    def calculate_cash_flow(income, expenses):
        return income.rental_income + income.other_income - expenses.property_taxes - expenses.insurance - expenses.maintenance

    @staticmethod
    def calculate_roi(cash_flow, total_income):
        if total_income > 0:
            return (cash_flow / total_income) * 100
        else:
            return 0


while True:
    try:
        rental_income = float(input("Enter rental income: "))
        other_income = float(input("Enter other income: "))
        property_taxes = float(input("Enter property taxes: "))
        insurance = float(input("Enter insurance expenses: "))
        maintenance = float(input("Enter maintenance expenses: "))

        income = Income(rental_income=rental_income, other_income=other_income)
        expenses = Expenses(property_taxes=property_taxes, insurance=insurance, maintenance=maintenance)

        total_cash_flow = Calculator.calculate_cash_flow(income, expenses)
        total_income = income.rental_income + income.other_income

        roi = Calculator.calculate_roi(total_cash_flow, total_income)

        property_instance = RentalProperty(income, expenses, total_cash_flow, roi)

        print(f"\nCash Flow: ${total_cash_flow}")
        print(f"ROI: {roi}%\n")

    except ValueError:
        print("Please enter valid numerical values.\n")

    user_input = input("Do you want to calculate again? (yes/no): ").lower()
    if user_input != 'yes':
        break
