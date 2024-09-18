
from models import Customer, Order,Laptop,session


def add_customer(name, contacts):
    customer = Customer(name=name, contacts=contacts)
    session.add(customer)
    session.commit()
    print(f"Added customer: {name}")

def add_laptop(name, specification,price):
    laptop = Laptop(name=name,specification=specification, price=price)
    session.add(laptop)
    session.commit()
    print(f"Added laptop: {name}")

def create_order(customer_id, laptop_id, quantity,total_price):
    order = Order(customer_id=customer_id, laptop_id=laptop_id,quantity=quantity, total_price=total_price)
    session.add(order)
    session.commit()
    print("Added order")

def get_customer_orders(customer_id):
    return session.query(Order).filter_by(customer_id=customer_id).all()

def get_laptop_details(laptop_id):
    return session.query(Laptop).get(laptop_id)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 7:
        print("Usage: python seed.py <command> <arg1> <arg2> ...")
        sys.exit(1)

    command = sys.argv[1]
    
    if command == "customer":
        add_customer(sys.argv[2], sys.argv[3])
    elif command == "order":
        customer_id = int(sys.argv[2])
        laptop_id = int(sys.argv[3])
        quantity = int(sys.argv[4])
        total_price =int(sys.argv[5])

        create_order(customer_id,laptop_id, quantity,total_price)
    elif command == "laptop":
        name = sys.argv[2]
        specification =sys.argv[3]
        price = int(sys.argv[4])
        add_laptop(name,specification, price)
    else:
        print("Invalid command")




    #  # Add laptops
    # add_laptop("Laptop X","Intel Core i7-1265U, 16GB RAM, 512GB SSD", 99999)
    # add_laptop("Laptop Y", "Intel Core i7-1265U, 16GB RAM, 512GB SSD",129999)

    # # Create customers
    # john = add_customer("John Doe", "john@gmail.com")
    # jane = add_customer("Jane Smith", "jane@gmail.com")

    # # Create orders
    # order1 = create_order(john.id, 1)  # John orders Laptop X
    # order2 = create_order(jane.id, 2)  # Jane orders Laptop Y
    # order3 = create_order(john.id, 1, quantity=2)  # John orders two more Laptop X

    # # Retrieve customer orders
    # john_orders = get_customer_orders(john.id)
    # print("hhhhhhhhhh")
    # print("Orders for John:")
    # for order in john_orders:
    #     laptop = get_laptop_details(order.laptop_id)
    #     print(f"- Order ID: {order.id}, Laptop: {laptop.name}, Quantity: {order.quantity}")

    # # Retrieve laptop details
    # laptop_x = get_laptop_details(1)
    # print("\nLaptop X Details:")
    # print(f"Name: {laptop_x.name}, Price: ${laptop_x.price:.2f}")
    


    
     
    # # Creating tables
    # Base.metadata.drop_all(engine)  # Drop tables if they already exist
    # Base.metadata.create_all(engine)  # Create tables in the database

    # # Inserting data into the tables
    # customer1 = Customer(customer_name='John Doe', contacts=1234567890)
    # customer2 = Customer(customer_name='Jane Smith', contacts=9876543210)
  

    # laptop1 = Laptop(laptop_name='Dell XPS 15', specification='Intel Core i7, 16GB RAM, 512GB SSD', price=12000,)
    # laptop2 = Laptop(laptop_name='HP Spectre x360', specification='AMD Ryzen 5 3600, 16GB RAM, 512GB SSD', price=15000)
    # session.add_all([laptop1, laptop2])
    # session.commit()

    # order1 = Order(customer_id=customer1.id, laptop_id=laptop1.id, quantity=2, total_price=24000)
    # session.add(order1)
    # session.commit()


    # #querying data in database
    # customers = session.query(Customer).all()
    # print (f"Customers:{customers}")
    # print (customers[0])
    # laptops = session.query(Laptop).all()
    # print (f"laptops:{laptops}")
    # orders = session.query(Order).all()
    # print (f"orders:{orders}")
