
from models import (Order,
                    Product,
                    Customer,
                    Status,
                    OrderLine,
                    engine)
from sqlalchemy.orm import sessionmaker
import datetime

Session = sessionmaker(bind=engine)
session = Session()

while True:
    pasirinkimas = int(input("Pasirinkite veiksmą: \n1 - atvaizduoti užsakymus \n2 - sukurti užsakymą\n3 - pridėti užsakymo eilutės\n"))
    if pasirinkimas == 1:
        orders = session.query(Order).all()
        for order in orders:
            print(order)
    if pasirinkimas == 2:
        my_date_str = input("Įveskite užsakymo datą (YYYY-MM-DD HH:MM:SS)")
        my_date = datetime.datetime.strptime(my_date_str, "%Y-%m-%d %H:%M:%S")
        customers = session.query(Customer).all()
        for customer in customers:
            print(customer.id, customer.name, customer.last_name)
        active_customer_id = int(input("Įveskite pasirinkto vartotojo ID: "))
        active_customer = session.query(Customer).get(active_customer_id)
        status_all = session.query(Status).all()
        for status in status_all:
            print(status.id, status.name)
        active_status_id = int(input("Įveskite pasirinkto statuso ID: "))
        active_status = session.query(Status).get(active_status_id)
        order = Order(date=my_date, customer=active_customer, status=active_status)
        session.add(order)
        session.commit()
    if pasirinkimas == 3:
        orders = session.query(Order).all()
        for order in orders:
            print(order)
        active_order_id = int(input("Įveskite pasirinkto užsakymo ID: "))
        active_order = session.query(Customer).get(active_order_id)
        products = session.query(Product).all()
        for product in products:
            print(product.name)
        active_product_id = int(input("Įveskite pasirinkto produkto ID: "))
        active_product = session.query(Customer).get(active_product_id)
        qty = int(input("Įveskite produkto kiekį: "))
        order_line = OrderLine(product=active_product, qty=qty)
        active_order.order_line.append(order_line)
        session.commit()

