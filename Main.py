
import loan_management as lm

def main():
    loan_manager = lm.LoanManagement()
    loan_manager.build_loan_details("LoanDetails.txt")
    loan_manager.add_loan_details()
    loan_id = input("Enter the loan id:")
    duration = int(input("Enter the duration:"))
    updated_loan = loan_manager.update_loan_details(loan_id, duration)
    if updated_loan:
        print("The updated record details are:")
        print(f"Loan ID: {updated_loan.get_loan_id()}")
        print(f"Customer Name: {updated_loan.get_customer_name()}")
        print(f"Loan Type: {updated_loan.get_loan_type()}")
        print(f"Loan amount: {updated_loan.get_loan_amount()}")
        print(f"Remaining total loan amount: {updated_loan.get_total_loan_amount()}")
        print(f"Remaining loan durations: {updated_loan.get_loan_duration()}")
    else:
        print("No record found")
    loan_type = input("Enter the loan type to be searched:")
    loans_found = loan_manager.search_loan_type(loan_type)
    if loans_found:
        print(f"The customer who gets {loan_type} loan")
        print("loan ID Customer name")
        for loan in loans_found:
            print(f"{loan.get_loan_id()} {loan.get_customer_name()}")
    else:
        print("Invalid loan type")
      
