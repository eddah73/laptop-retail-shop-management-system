# Phase 3 CLI Project Template
Author:Eddah chepkoech
## Introduction-proplem statement
Problem Statement for a Laptop Retail Shop Management System 
In today's growing online market, businesses need effective and easy-to-use tools to manage their stores. For laptop retailers, this means handling inventory, processing customer orders, and managing transactions smoothly. Many small laptop shops struggle with outdated or inadequate systems, leading to problems like messy inventory, poor customer service, and missed sales. 

Solutions 

As a result, I will be developing a laptop retail Shop Management System developed using Python, its designed to provide a seamless laptop purchasing experience. The application will allow customers  to access variety of available laptops and make order of laptops available. The application can securely store customer  credentials, laptop details and order details.overall, laptop retail shop management system is dedicated to delivering a high-quality retail application that meets customer expectations by providing seamless functionality, product diversity, and robust data

MVP FEATURES

Laptop Management 
Add New Laptops: Enter new laptops into the system with details like name, specs, and price. 
View Laptops: See a list of all laptops currently in stock. 
Update Laptops: Change details such as price or specifications, or update inventory . Remove Laptops: Delete laptops from the system that are no longer available.

 Order Management 
Create Orders: Place new orders for laptops, including customer details and order specifics. 
View Orders: See a list of all orders, including their status and customer information.
Cancel Orders: Delete the order

Customer Management
Add New Customers: Enter new customer details into the system, including name, contact.
View Customers: See a list of all customers with their details.
Update Customer Information: Modify customer details, such as updating contact information.
Remove Customers: Delete customer records that are no longer needed.

Technical Expectations 
Python: The programming language used to build the system. 
SQLAlchemy: A tool for managing the database. 
CLI: A command-line interface for interacting with the system, managing laptops, and processing orders.

<!-- directory atructure -->
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    └──db
       ├── models.py
       ├── cli.py
       └── helpers.py
       
# Generating Your Pipenv
pipenv install && pipenv shell

Install  SQLAlchemy and Alembic,:

```console
$ pipenv install sqlalchemy alembic``

```console
$ git add Pipfile Pipfile.lock
$ git commit -m'add sqlalchemy and alembic to pipenv'
$ git push
```

## Generating Your Database

Once you're in your environment, start with setting up your database.

`cd` into the `lib/db` directory, then run `alembic init migrations` to set up
Alembic. Modify line 58 in `alembic.ini` to point to the database you intend to
create, then replace line 21 in `migrations/env.py` with the following:

```py
from models import Base
target_metadata = Base.metadata
```

## Generating Your CLI

 run  `python cli.py`
