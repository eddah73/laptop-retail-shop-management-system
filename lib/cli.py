
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
    list_customer_laptops,
    list_orders,
    create_order,
    find_order_by_id,
    update_order,
    delete_order,
    list_orders_by_customer,
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_customers()
        elif choice == "2":
            find_customer_by_name()
        elif choice == "3":
            find_customer_by_id()
        elif choice == "4":
            create_customer()
        elif choice == "5":
            update_customer()
        elif choice == "6":
            delete_customer()
        elif choice == "7":
            list_laptops()
        elif choice == "8":
            find_laptop_by_name()
        elif choice == "9":
            find_laptop_by_id()
        elif choice == "10":
            create_laptop()
        elif choice == "11":
            update_laptop()
        elif choice == "12":
            delete_laptop()
        elif choice == "13":
            list_customer_laptops()
        elif choice == "14":
            list_orders()
        elif choice == "15":
            create_order()
        elif choice == "16":
            find_order_by_id()
        elif choice == "17":
            update_order()
        elif choice == "18":
            delete_order()
        elif choice == "19":
            list_orders_by_customer()
        
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all customers")
    print("2. Find customer by name")
    print("3. Find customer by id")
    print("4: Create customer")
    print("5: Update customer")
    print("6: Delete customer")
    print("7. List all laptops")
    print("8. Find laptops by name")
    print("9. Find laptops by id")
    print("10: Create laptops")
    print("11: Update laptops")
    print("12: Delete laptops")
    print("13: List all laptops ordered by customer")
    print("14: List all orders")
    print("15: Create order")
    print("16: Find order by id")
    print("17: Update order")
    print("18: Delete order")
    print("19: List all orders by customer")
    


if __name__ == "__main__":
    main()