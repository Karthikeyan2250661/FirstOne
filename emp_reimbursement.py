
class EmpReimbursement:
    def __init__(self, request_id, employee_code, date_of_request, grade, date_of_travel, no_of_days, local_travel_kms, manager_approval):
        self.__request_id = request_id
        self.__employee_code = employee_code
        self.__date_of_request = date_of_request
        self.__grade = grade
        self.__date_of_travel = date_of_travel
        self.__no_of_days = no_of_days
        self.__local_travel_kms = local_travel_kms
        self.__manager_approval = manager_approval
        self.__accomodation_cost = 0.0
        self.__dining_cost = 0.0
        self.__allowances = 0.0
        self.__travel_cost = 0.0
        self.__total_cost = 0.0

    def get_request_id(self): return self.__request_id
    def set_request_id(self, request_id): self.__request_id = request_id
    def get_employee_code(self): return self.__employee_code
    def set_employee_code(self, employee_code): self.__employee_code = employee_code
    def get_date_of_request(self): return self.__date_of_request
    def set_date_of_request(self, date_of_request): self.__date_of_request = date_of_request
    def get_grade(self): return self.__grade
    def set_grade(self, grade): self.__grade = grade
    def get_date_of_travel(self): return self.__date_of_travel
    def set_date_of_travel(self, date_of_travel): self.__date_of_travel = date_of_travel
    def get_no_of_days(self): return self.__no_of_days
    def set_no_of_days(self, no_of_days): self.__no_of_days = no_of_days
    def get_local_travel_kms(self): return self.__local_travel_kms
    def set_local_travel_kms(self, local_travel_kms): self.__local_travel_kms = local_travel_kms
    def get_manager_approval(self): return self.__manager_approval
    def set_manager_approval(self, manager_approval): self.__manager_approval = manager_approval
    def get_accomodation_cost(self): return self.__accomodation_cost
    def set_accomodation_cost(self, accomodation_cost): self.__accomodation_cost = accomodation_cost
    def get_dining_cost(self): return self.__dining_cost
    def set_dining_cost(self, dining_cost): self.__dining_cost = dining_cost
    def get_allowances(self): return self.__allowances
    def set_allowances(self, allowances): self.__allowances = allowances
    def get_travel_cost(self): return self.__travel_cost
    def set_travel_cost(self, travel_cost): self.__travel_cost = travel_cost
    def get_total_cost(self): return self.__total_cost
    def set_total_cost(self, total_cost): self.__total_cost = total_cost
