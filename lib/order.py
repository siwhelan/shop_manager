class Order:
    def __init__(self, name, order_date):
        self.name = name
        self.order_date = order_date

    def __repr__(self):
        return f"Order({self.name}, {self.order_date})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
