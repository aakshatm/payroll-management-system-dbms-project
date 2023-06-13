from DBHelper import DBHelper;
import time

def main():
    helper = DBHelper();

    print("******************************Welcome**********************************")

    while (True):
        print("\nenter 0: to add employee details: ")
        print("\nenter 1: show employee details: ")
        print("\nenter 2: fix da and hra rates: ")
        print("\nenter 3: show current da and hra rates: ")
        print("\nenter 4: paybill entry ")
        print("\nenter 5: show paybill")
        print("\nenter 6: to delete employee details(both from payslip and emp database)")
        print("\nenter 7: exit\n")

        choic = int(input("Enter your choice: "))
        try: 
        

            if choic == 0:
                print("Loading...\n")
                time.sleep(0.3)
                ecode = int(input("Enter ecode: "));
                fname = input("Enter first name: ");
                lname = input("Enter last name: ");
                desgination = input("Enter Designation: ");
                gender = input("Enter gender M/F: ");
                DOB = input("Enter dob: ");
                DOJ = input("Enter date of joining: ")
                mob = input("Enter mob: ");
                pan = input("Enter pan number: ");
                acno = input("Enter Account number: ");
                ifsc = input("Enter ifsc code: ");
                basic = int(input("Enter basic salary: "));
                ta = int(input("Enter ta: "))
                helper.input_employee(ecode, fname, lname, desgination, gender, DOB, DOJ, mob, pan, acno, ifsc, basic, ta);

            elif choic == 1:
                print("Loading...\n")
                time.sleep(0.3)
                helper.display_AllEmp();

            elif choic == 2:
                print("Loading...\n")
                time.sleep(0.3)
                daPercent = int(input("Enter da percentage: "))
                hraPercent = int(input("Enter HRA percentage: "))
                helper.percentage_setter(daPercent, hraPercent);

            elif choic == 3:
                print("Loading...\n")
                time.sleep(0.3)
                helper.show_rates();

            elif choic == 4:
                print("Loading...\n")
                time.sleep(0.3)
                helper.salary_entry();

            elif choic == 5:
                print("Loading...\n")
                time.sleep(0.3)
                year = int(input("Enter the year: "))
                helper.show_payBill(year);

            elif choic == 6:
                print("Loading...\n")
                time.sleep(0.3)
                ecode = int(input("Enter the ecode of the employee whose data u want to delete: "))
                helper.removeEmployee(ecode);


            elif choic == 7: 
                print("Exiting...");
                break;
                

            else: 
                print("Wrong choice.. try again..")

        
        except Exception as e: 
            print(e);



if (__name__ == "__main__"):
    main();

