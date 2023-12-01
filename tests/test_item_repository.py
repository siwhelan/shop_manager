from lib.item_repository import ItemRepository
from lib.item import Item
import pytest


def seed_item_repository(db_connection):
    db_connection.seed("seeds/create_tables.sql")


def test_add_item(db_connection):
    seed_item_repository(db_connection)
    repo = ItemRepository(db_connection)

    repo.add_item("AirPods Pro", 220, 40)
    repo.add_item("Sony TV", 1500, 20)

    expected_items = [
        Item("MacBook Pro 16-inch", "2399.99", 30),
        Item("iPhone 15", "799.99", 50),
        Item("Sony Headphones", "349.99", 40),
        Item("Samsung Galaxy", "999.99", 35),
        Item("iPad Pro", "1099.99", 25),
        Item("AirPods Pro", "220.00", 40),
        Item("Sony TV", "1500.00", 20),
    ]

    items = repo.find_all_items()
    assert items == expected_items


def test_find_item_by_name(db_connection):
    seed_item_repository(db_connection)
    repo = ItemRepository(db_connection)

    item = repo.find_item_by_name("iPhone 15")
    assert item == Item("iPhone 15", "799.99", 50)


def test_find_nonexistent_item_by_name(db_connection):
    seed_item_repository(db_connection)
    repo = ItemRepository(db_connection)

    with pytest.raises(ValueError) as err:
        repo.find_item_by_name("Non-existent Item")
    assert "Non-existent Item" in str(err.value)


def test_update_item(db_connection):
    seed_item_repository(db_connection)
    repo = ItemRepository(db_connection)

    repo.update_item("iPhone 15", 899.99, 60)

    expected_items = [
        Item("MacBook Pro 16-inch", "2399.99", 30),
        Item("iPhone 15", "899.99", 60),
        Item("Sony Headphones", "349.99", 40),
        Item("Samsung Galaxy", "999.99", 35),
        Item("iPad Pro", "1099.99", 25),
    ]

    items = repo.find_all_items()
    for item in items:
        print(item)
    assert items == expected_items


def test_delete_item(db_connection):
    seed_item_repository(db_connection)
    repo = ItemRepository(db_connection)

    repo.delete_item("iPhone 15")

    expected_items = [
        Item("MacBook Pro 16-inch", "2399.99", 30),
        Item("Sony Headphones", "349.99", 40),
        Item("Samsung Galaxy", "999.99", 35),
        Item("iPad Pro", "1099.99", 25),
    ]

    items = repo.find_all_items()
    assert items == expected_items


def test_return_quantity_of_item(db_connection):
    seed_item_repository(db_connection)
    repo = ItemRepository(db_connection)

    quantity = repo.return_quantity_of_item("iPhone 15")
    assert quantity == 50
