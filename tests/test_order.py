from lib.order import Order
from datetime import date


def test_order_construct():
    order_date = date(2023, 1, 4)
    order = Order("Customer 1", order_date)
    assert order.name == "Customer 1"
    assert order.order_date == order_date


def test_order_repr():
    order_date = date(2023, 1, 4)
    order = Order("Customer 1", order_date)
    assert order.__repr__() == "Order(Customer 1, 2023-01-04)"


def test_order_eq():
    order_date = date(2023, 1, 4)
    order1 = Order("Customer 1", order_date)
    order2 = Order("Customer 1", order_date)
    assert order1 == order2
