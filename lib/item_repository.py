from lib.item import Item


class ItemRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def add_item(self, name, price, quantity):
        self.db_connection.execute(
            "INSERT INTO items (name, price, quantity) VALUES (%s, %s, %s)",
            (name, price, quantity),
        )

    def find_all_items(self):
        rows = self.db_connection.execute("SELECT * FROM items ORDER BY id")
        return [Item(row["name"], str(row["price"]), row["quantity"]) for row in rows]

    def find_item_by_name(self, name):
        rows = self.db_connection.execute(
            "SELECT * FROM items WHERE name = %s", (name,)
        )
        if rows:
            row = rows[0]
            return Item(row["name"], str(row["price"]), row["quantity"])
        else:
            raise ValueError(
                f"Item '{name}' not found"
            )  # Raise an exception when the item is not found

    def update_item(self, name, price, quantity):
        self.db_connection.execute(
            "UPDATE items SET price = %s, quantity = %s WHERE name = %s",
            (price, quantity, name),
        )

    def delete_item(self, name):
        self.db_connection.execute("DELETE FROM items WHERE name = %s", (name,))

    def return_quantity_of_item(self, name):
        rows = self.db_connection.execute(
            "SELECT quantity FROM items WHERE name = %s", (name,)
        )
        if rows:
            row = rows[0]
            return row["quantity"]
        else:
            raise ValueError(f"Item '{name}' not found")
