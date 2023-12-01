from lib.order import Order


class OrderRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def add_order(self, item_name, order_name, order_date):
        # Insert new order
        self.db_connection.execute(
            "INSERT INTO orders (name, order_date) VALUES (%s, %s)",
            (order_name, order_date),
        )

        # Find the newly created order_id
        self.db_connection.execute(
            "SELECT id FROM orders WHERE name = %s AND order_date = %s",
            (order_name, order_date),
        )
        order_rows = self.db_connection.execute(
            "SELECT id FROM orders WHERE name = %s AND order_date = %s",
            (order_name, order_date),
        )
        order_id = order_rows[0]["id"] if order_rows else None

        # Find item_id based on item_name
        item_rows = self.db_connection.execute(
            "SELECT id FROM items WHERE name = %s", (item_name,)
        )
        item_id = item_rows[0]["id"] if item_rows else None

        # Insert into item_orders
        if order_id and item_id:
            self.db_connection.execute(
                "INSERT INTO item_orders (item_id, order_id) VALUES (%s, %s)",
                (item_id, order_id),
            )
        else:
            raise ValueError("Order or Item not found")

    def find_all_orders(self):
        rows = self.db_connection.execute("SELECT * FROM orders ORDER BY id")
        return [Order(row["name"], str(row["order_date"])) for row in rows]

    def find_order_by_name(self, name):
        rows = self.db_connection.execute(
            "SELECT * FROM orders WHERE name = %s", (name,)
        )
        if rows:
            row = rows[0]
            return Order(row["name"], str(row["order_date"]))
        else:
            raise ValueError(f"Order '{name}' not found")

    def delete_order(self, name):
        self.db_connection.execute("DELETE FROM orders WHERE name = %s", (name,))

    def return_order_id(self, name):
        rows = self.db_connection.execute(
            "SELECT id FROM orders WHERE name = %s", (name,)
        )
        if rows:
            row = rows[0]
            return row["id"]
        else:
            raise ValueError(f"Order '{name}' not found")

    def return_order_date(self, name):
        rows = self.db_connection.execute(
            "SELECT order_date FROM orders WHERE name = %s", (name,)
        )
        if rows:
            row = rows[0]
            return str(row["order_date"])
        else:
            raise ValueError(f"Order '{name}' not found")
