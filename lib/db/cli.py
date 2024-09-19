
from helpers import (
    exit_program,
    list_customers,
    find_customer_by_name,
    find_customer_by_id,
    create_customer,
    update_customer,
    delete_customer,
    list_laptops,
    find_laptop_by_name,
    find_laptop_by_id,
    create_laptop,
    update_laptop,
    delete_laptop,
    list_orders,
    create_order,
    update_order,
    cancel_order,
    list_orders_by_customer,
)


def main():
    print("-----Welcome to Laptop Shop-----")
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            custormer_options()
            while True:
                
                choice = input("> ")
                if choice == "0":
                    break
                elif choice == "1":
                    list_customers()
                elif choice == "2":
                    create_customer()
                elif choice == "3":
                    find_customer_by_name()
                elif choice == "4":
                    find_customer_by_id()
                elif choice == "5":
                    update_customer()
                elif choice == "6":
                    delete_customer()
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "2":
            while True:
                laptop_options()
                choice = input("> ")
                if choice == "0":
                    break
                elif choice == "1":
                    list_laptops()
                elif choice == "2":
                    create_laptop()
                elif choice == "3":
                    find_laptop_by_name()
                elif choice == "4":
                    find_laptop_by_id()
                elif choice == "5":
                    update_laptop()
                elif choice == "6":
                    delete_laptop()
                else:
                    print("Invalid choice. Please try again.")
        elif choice =="3":
            while True:
                order_options()
                choice = input("> ")
                if choice == "0":
                    break
                elif choice == "1":
                    list_orders()
                elif choice == "2":
                    create_order()
                elif choice == "3":
                    update_order()
                elif choice == "4":
                    cancel_order()
                elif choice == "5":
                    list_orders_by_customer()

                else:
                    print("Invalid choice. Please try again.")
        
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0.Exit the program")
    print("1.Customer options")
    print("2.Laptop options")
    print("3.Order options")



def custormer_options():
    print("Please select an option:")
    print("0.Exit the program")
    print("1.List all customers")
    print("2:Create customer")
    print("3.Find customer by name")
    print("4.Find customer by id")
    print("5:Update customer")
    print("6:Delete customer")
   


def laptop_options():
    print("Please select an option:")
    print("0.Exit the program")
    print("1.List all laptops")
    print("2:Create laptop")
    print("3.Find laptop by name")
    print("4.Find laptop by id")
    print("5:Update laptop")
    print("6:Delete laptop")
    

def order_options():
    print("Please select an option:")
    print("0.Exit the program")
    print("1:List all orders")
    print("2:Create order")
    print("3:Update order")
    print("4:Cancel order")
    print("5:List all orders made by customer")
if __name__ == "__main__":
    main()