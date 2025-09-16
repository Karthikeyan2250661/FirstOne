
class Loan:
    # Parameterized constructor
    def __init__(self, loan_id, customer_name, loan_type, loan_amount, loan_start_date, loan_duration):
        self._loan_id = loan_id
        self._customer_name = customer_name
        self._loan_type = loan_type
        self._loan_amount = float(loan_amount)
        self._loan_start_date = loan_start_date
        self._loan_duration = int(loan_duration)
        self._total_loan_amount = 0.0
        self._monthly_amount = 0.0

    # Getters and setters (provide only one, others repeated for all fields as per skeleton)
    def get_loan_id(self):
        return self._loan_id
    def set_loan_id(self, loan_id):
        self._loan_id = loan_id
    def get_customer_name(self):
        return self._customer_name
    def set_customer_name(self, customer_name):
        self._customer_name = customer_name
    def get_loan_type(self):
        return self._loan_type
    def set_loan_type(self, loan_type):
        self._loan_type = loan_type
    def get_loan_amount(self):
        return self._loan_amount
    def set_loan_amount(self, loan_amount):
        self._loan_amount = loan_amount
    def get_loan_start_date(self):
        return self._loan_start_date
    def set_loan_start_date(self, loan_start_date):
        self._loan_start_date = loan_start_date
    def get_loan_duration(self):
        return self._loan_duration
    def set_loan_duration(self, loan_duration):
        self._loan_duration = loan_duration
    def get_total_loan_amount(self):
        return self._total_loan_amount
    def set_total_loan_amount(self, total_loan_amount):
        self._total_loan_amount = total_loan_amount
    def get_monthly_amount(self):
        return self._monthly_amount
    def set_monthly_amount(self, monthly_amount):
        self._monthly_amount = monthly_amount

    # Interest calculation logic
    def calculate_total_amount(self):
        interest_rate = 0.0
        amt = self._loan_amount
        typ = self._loan_type.lower()
        if typ == "car":
            interest_rate = 0.075 if amt <= 1000000 else 0.066
        elif typ == "business":
            interest_rate = 0.15 if amt <= 1000000 else 0.135
        elif typ == "agricultural":
            interest_rate = 0.085 if amt <= 1000000 else 0.08
        elif typ == "home":
            interest_rate = 0.082 if amt <= 1000000 else 0.074
        elif typ == "personal":
            interest_rate = 0.125 if amt <= 1000000 else 0.108
        elif typ == "education":
            interest_rate = 0.04 if amt <= 1000000 else 0.038

        self._total_loan_amount = round(amt + (amt * interest_rate), 2)
        return self._total_loan_amount
      
