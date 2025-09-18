import emp_reimbursement as er
import utility as ut
from datetime import date

class EmpReimbursementService:
    def __init__(self):
        self.__emp_reimbursement_list = []

    def build_employee_list(self, emp_reimburses_records):
        for record in emp_reimburses_records:
            fields = [field.strip() for field in record.split(",")]
            if len(fields) >= 8:
                request_id = fields[0]
                employee_code = fields[1]
                date_of_request_str = fields[2]
                grade = fields[3]
                date_of_travel_str = fields[4]
                no_of_days = int(fields[5])
                local_travel_kms = int(fields[6])
                manager_approval = fields[7]
                validation_result = ut.validate_request_id(request_id)
                if validation_result == True:
                    date_of_request = ut.convert_date(date_of_request_str)
                    date_of_travel = ut.convert_date(date_of_travel_str)
                    # Filtering logic, modify as needed:
                    days = abs((date_of_request - date_of_travel).days)
                    if days <= 180 and manager_approval.lower() == "approved":
                        emp_obj = er.EmpReimbursement(
                            request_id, employee_code, date_of_request,
                            grade, date_of_travel, no_of_days, local_travel_kms, manager_approval
                        )
                        costs = self.calculate_reimbursement_costs(no_of_days, local_travel_kms, grade)
                        emp_obj.set_accomodation_cost(costs[0])
                        emp_obj.set_dining_cost(costs[1])
                        emp_obj.set_travel_cost(costs[2])
                        emp_obj.set_allowances(costs[3])
                        emp_obj.set_total_cost(costs[4])
                        self.__emp_reimbursement_list.append(emp_obj)
        return

    def add_employee_details(self, input_file):
        records = ut.read_file(input_file)
        self.build_employee_list(records)
        return

    def calculate_reimbursement_costs(self, no_of_days, local_travel_kms, grade):
        cost_matrix = {
            "Level01": {"accomodation": 10000, "dining": 1000, "travel_per_km": 22, "allowances": 1500},
            "Level02": {"accomodation": 10000, "dining": 1000, "travel_per_km": 22, "allowances": 1500},
            "Level03": {"accomodation": 4000, "dining": 700, "travel_per_km": 16, "allowances": 1000},
            "Level04": {"accomodation": 4000, "dining": 700, "travel_per_km": 16, "allowances": 1000},
            "Level05": {"accomodation": 2500, "dining": 450, "travel_per_km": 12, "allowances": 750},
            "Level06": {"accomodation": 2500, "dining": 450, "travel_per_km": 12, "allowances": 750}
        }
        if grade in cost_matrix:
            rates = cost_matrix[grade]
            accomodation_cost = float(no_of_days * rates["accomodation"])
            dining_cost = float(no_of_days * rates["dining"])
            travel_cost = float(local_travel_kms * rates["travel_per_km"])
            allowances_cost = float(no_of_days * rates["allowances"])
            total_cost = accomodation_cost + dining_cost + travel_cost + allowances_cost
            return [accomodation_cost, dining_cost, travel_cost, allowances_cost, total_cost]
        else:
            return [0.0, 0.0, 0.0, 0.0, 0.0]

    def search_reimbursement_request(self, request_id):
        for emp in self.__emp_reimbursement_list:
            if emp.get_request_id() == request_id:
                return emp
        return None

    def update_costs(self):
        updated_list = []
        new_rates = {
            "accomodation": 12000,
            "dining": 1200,
            "travel_per_km": 24,
            "allowances": 1700
        }
        for emp in self.__emp_reimbursement_list:
            if emp.get_grade() == "Level01":
                no_of_days = emp.get_no_of_days()
                local_travel_kms = emp.get_local_travel_kms()
                new_accomodation = float(no_of_days * new_rates["accomodation"])
                new_dining = float(no_of_days * new_rates["dining"])
                new_travel = float(local_travel_kms * new_rates["travel_per_km"])
                new_allowances = float(no_of_days * new_rates["allowances"])
                new_total = new_accomodation + new_dining + new_travel + new_allowances
                emp.set_accomodation_cost(new_accomodation)
                emp.set_dining_cost(new_dining)
                emp.set_travel_cost(new_travel)
                emp.set_allowances(new_allowances)
                emp.set_total_cost(new_total)
                updated_list.append(emp)
        return updated_list

