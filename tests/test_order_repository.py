from lib.order import Order
from lib.order_repository import OrderRepository
from datetime import datetime


def seed_order_repository(db_connection):
    db_connection.seed("seeds/create_tables.sql")


def test_add_order(db_connection):
    seed_order_repository(db_connection)
    repo = OrderRepository(db_connection)

    fixed_date = datetime(2023, 3, 19).date()
    repo.add_order("iPhone 15", "Customer Name", fixed_date)
    repo.add_order("iPad Pro", "Customer Name", fixed_date)

    expected_orders = [
        Order("Alice Johnson", "2023-03-15"),
        Order("Bob Jones", "2023-03-16"),
        Order("Carolyn Bessette", "2023-03-17"),
        Order("David Brown", "2023-03-18"),
        Order("Eva Smith", "2023-03-19"),
        Order("Customer Name", "2023-03-19"),
        Order("Customer Name", "2023-03-19"),
    ]

    orders = repo.find_all_orders()

    assert orders == expected_orders


def test_find_order_by_name(db_connection):
    seed_order_repository(db_connection)
    repo = OrderRepository(db_connection)

    order = repo.find_order_by_name("Carolyn Bessette")
    assert order == Order("Carolyn Bessette", "2023-03-17")


def test_delete_order(db_connection):
    seed_order_repository(db_connection)
    repo = OrderRepository(db_connection)

    repo.delete_order("Carolyn Bessette")

    expected_orders = [
        Order("Alice Johnson", "2023-03-15"),
        Order("Bob Jones", "2023-03-16"),
        Order("David Brown", "2023-03-18"),
        Order("Eva Smith", "2023-03-19"),
    ]

    orders = repo.find_all_orders()

    assert orders == expected_orders


def test_return_order_id(db_connection):
    seed_order_repository(db_connection)
    repo = OrderRepository(db_connection)

    order_id = repo.return_order_id("Carolyn Bessette")
    assert order_id == 3


def test_return_order_date(db_connection):
    seed_order_repository(db_connection)
    repo = OrderRepository(db_connection)

    order_date = repo.return_order_date("Carolyn Bessette")
    assert order_date == "2023-03-17"
