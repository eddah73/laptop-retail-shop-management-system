from models import Customer,Order,Laptop,session


def exit_program():
    print("Goodbye!")
    exit()

def list_customers():
    customers = session.query(Customer).all()
    print("Customers:")    
    for customer in customers:
        print(f"ID: {customer.id}, Name: {customer.name}, Contacts: {customer.contacts}")
    


def find_customer_by_name():
    """Find customers by name."""
    name = input("Enter customer name to find: ")
    customers = session.query(Customer).filter_by(name=name).all()
    
    if customers:
        for customer in customers:
            print(f"ID: {customer.id}, Name: {customer.name}, Contacts: {customer.contacts}")
    else:
        print("Customer name not found.")

def find_customer_by_id():
    """finding customers by id"""
    id = int(input("Enter customer id to find:"))
    customer = session.query(Customer).filter_by(id=id).first()
    if customer:
        print(f"ID: {customer.id}, Name: {customer.name}, Contacts: {customer.contacts}")
    else:
        print("Customer not found.")


def create_customer():
    """Create a new customer."""
    name = input("Enter customer name: ")
    contacts = input("Enter customer contacts: ")
    if not name:
        print("Customer name field is empty.")
        return
    
    if not contacts:
        print("Customer contacts field is empty.")
        return   
    
    existing_customer = session.query(Customer).filter_by(name=name, contacts=contacts).first()
    
    if existing_customer:
        print("Customer already exists.")
    else:
        customer = Customer(name=name, contacts=contacts)
        session.add(customer)
        session.commit()
        print("Customer created successfully!")


def update_customer():
    """Update customer"""
    id = int(input("Enter customer id to update: "))
    customer = session.query(Customer).filter_by(id=id).first()
    
    if customer:
        name = input("Enter new customer name (leave blankt): ")
        contacts = input("Enter new customer contacts (leave blank): ")
        
        if name:
            customer.name = name
        if contacts:
            customer.contacts = contacts
        
        session.commit()
        print("Customer updated successfully!")
    else:
        print("Customer not found.")
def delete_customer():
    """Delete customer"""
    id = int(input("Enter customer id to delete:"))
    customer = session.query(Customer).filter_by(id=id).first()
    if customer:
        session.delete(customer)
        session.commit()
        print("Customer deleted successfully!!!")
    else:
        print("Customer not found.")

def list_laptops():
    laptops = session.query(Laptop).all()
    print("Laptops:")    
    for laptop in laptops:
        print(f"ID: {laptop.id}, Name: {laptop.name}, Specification: {laptop.specification}, Price: {laptop.price},stock: {laptop.stock}")


def find_laptop_by_name():
    """Find laptops by name."""
    name = input("Enter laptop name to find: ")
    laptops = session.query(Laptop).filter_by(name=name).all()
    
    if laptops:
        for laptop in laptops:
            print(f"ID: {laptop.id}, Name: {laptop.name}, Specification: {laptop.specification}, Price: {laptop.price},stock: {laptop.stock}")
    else:
        print("Laptop name not found.")
    


def find_laptop_by_id():
    """finding laptops by id"""
    id = int(input("Enter laptop id to find:"))
    laptop = session.query(Laptop).filter_by(id=id).first()
    if laptop:
        print(f"ID: {laptop.id}, Name: {laptop.name}, Specification: {laptop.specification}, Price: {laptop.price},stock: {laptop.stock}")
    else:
        print("Laptop id not found.")    


def create_laptop():
    """Create a new laptop """
    
    name = input("Enter laptop name: ")
    specification = input("Enter laptop specification: ")
    price = int(input("Enter laptop price: ")) 
    stock = int(input("Enter quantity of stock: "))
    if not name:
        print("Laptop name field is empty.")
        return
    if not specification:
        print("Laptop specification field is empty.")
        return

    # Check if the laptop already exists
    existing_laptop = session.query(Laptop).filter_by(name=name, specification=specification, price=price).first()
    
    if existing_laptop:
        # If it exists, increase the stock
        existing_laptop.stock += stock
        print("New laptop(s) have added to existing stock")
    else:
        # If it doesn't exist, create a new laptop entry
        laptop = Laptop(name=name, specification=specification, price=price, stock=stock)
        session.add(laptop)
        print("New laptop created successfully")
    
    session.commit()



def update_laptop():
    """Update laptop."""
    id = int(input("Enter laptop id to update: "))
    laptop = session.query(Laptop).filter_by(id=id).first()
    
    if laptop:
        name = input("Enter new laptop name (leave blank): ")
        specification = input("Enter new laptop specification (leave blank): ")
        price = input("Enter new laptop price (leave blank): ")
        stock = input("Enter new quantity of stock (leave blank): ")

        if name:
            laptop.name = name
        if specification:
            laptop.specification = specification
        if price:
            laptop.price = price
        if stock:
            laptop.stock = int(stock)  

        session.commit()
        print("Laptop updated successfully!")
    else:
        print("Laptop not found.")


def delete_laptop():
    """Delete laptop"""
    id = int(input("Enter laptop id to delete:"))
    laptop = session.query(Laptop).filter_by(id=id).first()
    if laptop:
        session.delete(laptop)
        session.commit()
        print("Laptop deleted successfully!!!")
    else:
        print("Laptop not found.")


def list_orders():
    orders = session.query(Order).all()
    print("Orders:")    
    for order in orders:
        print(f"ID: {order.id}, Customer ID: {order.customer_id}, Laptop ID: {order.laptop_id}, Quantity: {order.quantity}, Total Price: {order.total_price}, Status: {order.status}")
    

def create_order():
    """Create an order for an existing customer and laptop."""
    
    # Get customer name and check if exists
    customer_name = input("Customer name: ")
    customer = session.query(Customer).filter_by(name=customer_name).first()
    
    if not customer:
        print("Customer not found.")
        return
    
    # Get laptop name and check if exists
    laptop_name = input("Laptop name: ")
    laptop = session.query(Laptop).filter_by(name=laptop_name).first()
    
    if not laptop:
        print("Laptop not found.")
        return
    
    # Get quantity and calculate total price
    quantity = int(input("Quantity: "))
    if quantity > laptop.stock:  
        print(f"Not enough stock available.")
        return
    total_price = laptop.price * quantity

    # Create the order with status 'ordered'
    order = Order(customer=customer, laptop=laptop, quantity=quantity, total_price=total_price, status='order on process')
    session.add(order)
    session.commit()
    print("An Order created Successfully")

    
def update_order():
    """Update an existing order's quantity or status."""
    id = int(input("Enter Id of Order: "))
    order = session.query(Order).filter_by(id=id).first()

    if not order:
        print("Order not found.")
        return

    # Update quantity
    new_quantity = input("Enter new quantity (leave blank): ")
    if new_quantity:
        order.quantity = int(new_quantity)
        order.total_price = order.laptop.price * order.quantity 

    # Update status
    new_status = input("Enter new status (leave ): ")
    if new_status:
        if order.status.lower() == "order on process" and new_status.lower() == "completed":
            # Query the laptop using laptop_id from the order
            laptop = session.query(Laptop).filter_by(id=order.laptop_id).first()
            
            if laptop:
                # Reduce the stock of the laptop
                if laptop.stock >= order.quantity:
                    laptop.stock -= order.quantity
                    print("Stock updated successfully.")
                else:
                    print("Insufficient stock to fulfill this order.")
                    return
            else:
                print("Laptop not found.")
                return

        # Update the order status
        order.status = new_status

    session.commit()
    print("Order updated successfully!")


    

def cancel_order():
    """Cancel an existing order."""
    order_id = int(input("Enter Id of Order to cancel: "))
    order = session.query(Order).filter_by(id=order_id).first()
    
    if not order:
        print("Order not found.")
        return

    session.delete(order)
    session.commit()
    print("Order cancelled")


def list_orders_by_customer():
    """list of oreders made by customer"""
    customer_id = int(input("Enter Customer ID: "))
    orders = session.query(Order).filter_by(customer_id=customer_id).all()
    
    if orders:
        print("Orders:")    
        for order in orders:
            print(f"ID: {order.id}, Customer ID: {order.customer_id}, Laptop ID: {order.laptop_id}, Quantity: {order.quantity}, Total Price: {order.total_price}, Status: {order.status}")
    else:
        print("No orders found for this customer.")
    
