
import emp_reimbursement_service as rs
import utility as ut

def main():
    request_id = input("Enter the Request Id: ")
    obj = rs.EmpReimbursementService()
    obj.add_employee_details("EmpDetails.txt")
    validation_result = ut.validate_request_id(request_id)
    if validation_result == True:
        emp_record = obj.search_reimbursement_request(request_id)
        if emp_record is not None:
            print("Record found")
            print(f"Request Id: {emp_record.get_request_id()}")
            print(f"Employee Code: {emp_record.get_employee_code()}")
            print(f"Date of Travel: {emp_record.get_date_of_travel()}")
            print(f"No.of Days: {emp_record.get_no_of_days()}")
            print(f"Accommodation Cost: {emp_record.get_accomodation_cost()}")
            print(f"Dinning Cost: {emp_record.get_dining_cost()}")
            print(f"Local Travel cost: {emp_record.get_travel_cost()}")
            print(f"Allowances: {emp_record.get_allowances()}")
            print(f"Total Reimbursement Amount: {emp_record.get_total_cost()}")
        else:
            print("No record found")
    else:
        print(validation_result)

    updated_details = obj.update_costs()
    if updated_details:
        print("The updated record details are:")
        for emp in updated_details:
            print(f"Request Id: {emp.get_request_id()}")
            print(f"Employee Code: {emp.get_employee_code()}")
            print(f"Date of Travel: {emp.get_date_of_travel()}")
            print(f"No.of Days: {emp.get_no_of_days()}")
            print(f"Accommodation Cost: {emp.get_accomodation_cost()}")
            print(f"Dinning Cost: {emp.get_dining_cost()}")
            print(f"Local Travel cost: {emp.get_travel_cost()}")
            print(f"Allowances: {emp.get_allowances()}")
            print(f"Total Reimbursement Amount: {emp.get_total_cost()}")

if __name__ == "__main__":
    main()
  
