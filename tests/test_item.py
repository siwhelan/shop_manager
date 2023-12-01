from lib.item import Item


def test_item_contruct():
    item = Item("New Item", 150, 20)
    assert item.name == "New Item"
    assert item.price == 150
    assert item.quantity == 20


def test_item_repr():
    item = Item("New Item", 150, 20)
    assert repr(item) == "Item(New Item, 150, 20)"


def test_item_eq():
    item1 = Item("New Item", 150, 20)
    item2 = Item("New Item", 150, 20)
    assert item1 == item2
