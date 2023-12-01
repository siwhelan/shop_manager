# Shop Manager Project 


## 1. Extract nouns from the user stories or specification

```
As a shop manager
So I can know which items I have in stock
I want to keep a list of my shop items with their name and unit price.

As a shop manager
So I can know which items I have in stock
I want to know which quantity (a number) I have for each item.

As a shop manager
So I can manage items
I want to be able to create a new item.

As a shop manager
So I can know which orders were made
I want to keep a list of orders with their customer name.

As a shop manager
So I can know which orders were made
I want to assign each order to their corresponding item.

As a shop manager
So I can know which orders were made
I want to know on which date an order was placed. 

As a shop manager
So I can manage orders
I want to be able to create a new order.

```

```
Keywords:

stock, item, name, price, quantity, create new, orders, customer name, order item, order date, new order
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| item                  | name, quantity,
| order                 | name, item_id, date, quantity

1. Name of the first table (always plural): `items` 

    Column names: `name`, `quantity`

2. Name of the second table (always plural): `orders` 

    Column names: `name`, `date`, `item_id` 

## 3. Decide the column types.

```
Table: items
id: SERIAL
name: text
price: float
quantity: int

Table: orders
id: SERIAL
name: text
order_date: date
quantity: int

```

## 4. Design the Many-to-Many relationship

Make sure you can answer YES to these two questions:

1. Can one item have many orders? (Yes)
2. Can one order have many items? (Yes)



## 5. Design the Join Table

```
# EXAMPLE

Join table for tables: items and orders
Join table name: item_orders
Columns: item_id, order_id
```

## 6. Write the SQL.

```sql
CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  name text,
  price DECIMAL(10, 2),
  quantity int
);

-- Create the second table.
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  name text,
  order_date date,
  quantity int
);

-- Create the join table.
CREATE TABLE item_orders (
  item_id int,
  order_id int,
  constraint fk_item foreign key(item_id) references items(id) on delete cascade,
  constraint fk_order foreign key(order_id) references orders(id) on delete cascade,
  PRIMARY KEY (item_id, order_id)
);

```

## 7. Create the tables.

```bash
psql -h 127.0.0.1 shop_manager < create_tables.sql
```