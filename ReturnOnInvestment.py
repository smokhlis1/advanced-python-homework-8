class RentalPropertyROI():
    def __init__(self, rental_income, taxes, insurance, vacancy, repairs, capex, mortgage, property_management):
        self.rental_income = rental_income
        self.taxes = taxes
        self.insurance = insurance
        self.vacancy = vacancy
        self.repairs = repairs 
        self.capex = capex
        self.mortgage = mortgage
        self.property_management = property_management

    def monthly_cash_flow(self):
        total_income = self.rental_income
        total_expense = self.taxes + self.insurance + self.vacancy + self.repairs + self.capex + self.mortgage + self.property_management
        return total_income - total_expense
        
    def annual_cash_flow(self, total_investment):
        monthly_cash = self.monthly_cash_flow()
        annual_cash = monthly_cash * 12
        return (annual_cash / total_investment) * 100

property_info = RentalPropertyROI(
    rental_income = 2000.00,
    taxes= 150.00,
    insurance= 100.00,
    vacancy= 100.00,
    repairs = 100.00,
    capex= 100.00,
    mortgage= 860.00,
    property_management= 200.00
)


total_investment = 50000.00
cash_flow = property_info.monthly_cash_flow()
roi = property_info.annual_cash_flow(total_investment)

print(f"Cash Flow: ${cash_flow:.2f}")
print(f"ROI: {roi:.1f}%")