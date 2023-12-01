DROP TABLE IF EXISTS item_orders CASCADE;
DROP TABLE IF EXISTS items CASCADE;
DROP TABLE IF EXISTS orders CASCADE;

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

-- Inserting data into 'items'
INSERT INTO items (name, price, quantity)
VALUES 
('MacBook Pro 16-inch', 2399.99, 30),
('iPhone 15', 799.99, 50),
('Sony Headphones', 349.99, 40),
('Samsung Galaxy', 999.99, 35),
('iPad Pro', 1099.99, 25);

-- Inserting data into 'orders'
INSERT INTO orders (name, order_date)
VALUES 
('Alice Johnson', '2023-03-15'),
('Bob Jones', '2023-03-16'),
('Carolyn Bessette', '2023-03-17'),
('David Brown', '2023-03-18'),
('Eva Smith', '2023-03-19');

-- Inserting data into 'item_orders'

INSERT INTO item_orders (item_id, order_id)
VALUES 
(1, 1), -- MacBook Pro bought by Alice Johnson
(2, 1), -- iPhone 15 also bought by Alice Johnson
(2, 2), -- iPhone 15 bought by Bob Jones
(3, 3), -- Sony Headphones bought by Carolyn Bessette
(4, 4), -- Samsung Galaxy S21 bought by David Brown
(5, 5); -- iPad Pro bought by Eva Smith