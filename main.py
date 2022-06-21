
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
    pasirinkimas = int(input("Pasirinkite veiksmą: \n1 - atvaizduoti užsakymus \n2 - sukurti užsakymą\n3 - pridėti užsakymo eilutės\n4 - redaguoti vartotojus\n"))
    if pasirinkimas == 1:
        orders = session.query(Order).all()
        for order in orders:
            print(f"{order}:")
            bendra = 0
            for nr, line in enumerate(order.order_line):
                suma = line.product.price * line.qty
                print(f"\t {nr + 1} {line.product.name}, kaina: {line.product.price}, kiekis: {line.qty}, suma - {suma} Eur")
                bendra += suma
            print("\t Bendra suma", bendra)
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
        active_order = session.query(Order).get(active_order_id)
        products = session.query(Product).all()
        for product in products:
            print(product.id, product.name)
        active_product_id = int(input("Įveskite pasirinkto produkto ID: "))
        active_product = session.query(Product).get(active_product_id)
        qty = int(input("Įveskite produkto kiekį: "))
        order_line = OrderLine(order=active_order, product=active_product, qty=qty)
        session.add(order_line)
        session.commit()
    if pasirinkimas == 4:
        # customers = Customer.query.all()
        customers = session.query(Customer).all()
        for customer in customers:
            print(customer.id, customer.name, customer.last_name)
        customer_pasirinkimas = input("Pasirinkite veiksmą: \na - pridėti vartotoją \nb - ištrinti vartotoją\nc - išeiti iš vartotojų redagavimo\n")
        if customer_pasirinkimas == "a":
            new_name = input("Įveskite vartotojo vardą")
            new_last_name = input("Įveskite vartotojo pavardę")
            new_email = input("Įveskite vartotojo el. pašto adresą")
            new_customer = Customer(name=new_name, last_name=new_last_name, email=new_email)
            session.add(new_customer)
            session.commit()
        if customer_pasirinkimas == "b":
            active_customer_id = int(input("Įveskite norimo ištrinti vartotojo ID: "))
            active_customer = session.query(Customer).get(active_customer_id)
            session.delete(active_customer)
            session.commit()
            print("Vartotojas ištrintas")
        if customer_pasirinkimas == "c":
            pass

