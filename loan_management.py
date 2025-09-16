
import loan as ln
import cx_Oracle
import datetime

class LoanManagement:
    def __init__(self):
        self._loan_details_list = []

    def build_loan_details(self, file):
        with open(file) as f:
            for line in f:
                values = line.strip().split(",")
                if len(values) != 6:
                    continue
                loan_id, name, loan_type, loan_amt, start_date, duration = [v.strip() for v in values]
                loan_obj = ln.Loan(loan_id, name, loan_type, float(loan_amt), self.convert_date(start_date), int(duration))
                loan_obj.calculate_total_amount()
                loan_obj.set_monthly_amount(round(loan_obj.get_total_loan_amount() / loan_obj.get_loan_duration(), 2))
                self._loan_details_list.append(loan_obj)

    def convert_date(self, start_date):
        return datetime.datetime.strptime(start_date, "%Y-%m-%d").date()

    def add_loan_details(self):
        # Load database params from properties file
        db = {}
        with open('database.properties') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    k, v = line.strip().split('=', 1)
                    db[k.strip()] = v.strip()
        conn = cx_Oracle.connect(db['DB_USERNAME'], db['DB_PASSWORD'], db['DSN'])
        cursor = conn.cursor()
        for loan in self._loan_details_list:
            cursor.execute("""INSERT INTO loan (loan_id, customer_name, loan_type, loan_amount, loan_start_date, loan_duration, total_loan_amount, monthly_amount)
                VALUES (:1,:2,:3,:4,:5,:6,:7,:8)""",
                [loan.get_loan_id(), loan.get_customer_name(), loan.get_loan_type(), loan.get_loan_amount(),
                  loan.get_loan_start_date(), loan.get_loan_duration(), loan.get_total_loan_amount(), loan.get_monthly_amount()])
        conn.commit()
        cursor.close()
        conn.close()

    def update_loan_details(self, loan_id, duration):
        db = {}
        with open('database.properties') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    k, v = line.strip().split('=', 1)
                    db[k.strip()] = v.strip()
        conn = cx_Oracle.connect(db['DB_USERNAME'], db['DB_PASSWORD'], db['DSN'])
        cursor = conn.cursor()
        cursor.execute("SELECT loan_id, customer_name, loan_type, loan_amount, loan_start_date, loan_duration, total_loan_amount, monthly_amount FROM loan WHERE loan_id=:1", [loan_id])
        result = cursor.fetchone()
        if not result:
            cursor.close()
            conn.close()
            return None
        loan_duration = int(result[5])
        if duration >= loan_duration:
            cursor.close()
            conn.close()
            return None
        total_loan_amount = float(result[6])
        monthly_amount = float(result[7])
        new_total_loan_amount = round(total_loan_amount - (duration * monthly_amount), 0)
        new_duration = loan_duration - duration
        cursor.execute("UPDATE loan SET loan_duration=:1, total_loan_amount=:2 WHERE loan_id=:3", [new_duration, new_total_loan_amount, loan_id])
        conn.commit()
        cursor.close()
        conn.close()
        return ln.Loan(result[0], result[1], result[2], result[3], result[4], new_duration)

    def search_loan_type(self, loan_type):
        db = {}
        with open('database.properties') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    k, v = line.strip().split('=', 1)
                    db[k.strip()] = v.strip()
        conn = cx_Oracle.connect(db['DB_USERNAME'], db['DB_PASSWORD'], db['DSN'])
        cursor = conn.cursor()
        cursor.execute("SELECT loan_id, customer_name, loan_type, loan_amount, loan_start_date, loan_duration, total_loan_amount, monthly_amount FROM loan WHERE lower(loan_type)=:1", [loan_type.lower()])
        results = cursor.fetchall()
        loans = []
        for result in results:
            loan = ln.Loan(result[0], result[1], result[2], float(result[3]), result[4], int(result[5]))
            loan.set_total_loan_amount(float(result[6]))
            loan.set_monthly_amount(float(result[7]))
            loans.append(loan)
        cursor.close()
        conn.close()
        return loans
      
