from lib.item import Item


class ItemRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def execute_query(self, query, params=None):
        # Executes a database query with the given parameters
        # reducing code repetiton.
        return self.db_connection.execute(query, params)

    def add_item(self, name, price, quantity):
        self.execute_query(
            "INSERT INTO items (name, price, quantity) VALUES (%s, %s, %s)",
            (name, price, quantity),
        )

    def find_all_items(self):
        rows = self.execute_query("SELECT * FROM items ORDER BY id")
        return [Item(row["name"], str(row["price"]), row["quantity"]) for row in rows]

    def find_item_by_name(self, name):
        rows = self.execute_query("SELECT * FROM items WHERE name = %s", (name,))
        if rows:
            row = rows[0]
            return Item(row["name"], str(row["price"]), row["quantity"])
        else:
            raise ValueError(
                f"Item '{name}' not found"
            )  # Raise an exception when the item is not found

    def update_item(self, name, price, quantity):
        self.execute_query(
            "UPDATE items SET price = %s, quantity = %s WHERE name = %s",
            (price, quantity, name),
        )

    def delete_item(self, name):
        self.execute_query("DELETE FROM items WHERE name = %s", (name,))

    def return_quantity_of_item(self, name):
        rows = self.execute_query("SELECT quantity FROM items WHERE name = %s", (name,))
        if rows:
            row = rows[0]
            return row["quantity"]
        else:
            raise ValueError(f"Item '{name}' not found")
