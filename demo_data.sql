USE restaurant_ordering_system;

-- Sandwiches (menu items)
INSERT INTO sandwiches (sandwich_name, price, calories, ingredients, category) VALUES
('Classic Veggie Burger', 8.99, 450, 'Lettuce, tomato, plant-based patty, whole wheat bun', 'vegetarian'),
('Spicy Chicken Wrap', 9.49, 520, 'Grilled chicken, spicy mayo, lettuce, tomato wrap', 'spicy'),
('Kids Cheeseburger', 5.99, 350, 'Beef patty, cheese, ketchup, mini bun', 'kids'),
('Grilled Chicken Salad', 10.99, 380, 'Mixed greens, grilled chicken, vinaigrette', 'low fat'),
('Double Bacon Burger', 12.99, 800, 'Two beef patties, bacon, cheese, brioche bun', 'none');

-- Resources (ingredients)
INSERT INTO resources (item, amount) VALUES
('Plant-based patty', 20),
('Whole wheat bun', 15),
('Chicken breast', 10),
('Spicy mayo', 5),
('Beef patty', 12),
('Cheese slice', 30),
('Bacon strips', 8),
('Brioche bun', 10),
('Lettuce', 25),
('Tomato', 20);

-- Recipes (linking sandwiches to resources)
INSERT INTO recipes (sandwich_id, resource_id, amount) VALUES
(1, 1, 1), (1, 2, 1),   -- Veggie Burger: patty + bun
(2, 3, 1), (2, 4, 1),   -- Spicy Wrap: chicken + spicy mayo
(3, 5, 1), (3, 6, 1),   -- Kids Burger: beef + cheese
(4, 3, 1),               -- Chicken Salad: chicken
(5, 5, 2), (5, 7, 2), (5, 8, 1); -- Double Bacon: beef, bacon, bun

-- Promotions
INSERT INTO promotions (promo_code, expiration_date, discount_type, discount_value, is_active) VALUES
('SAVE10', '2026-12-31 23:59:59', 'percentage', 10.00, 1);

-- Customers
INSERT INTO customers (name, phone, address, email) VALUES
('Alex Rivera', '704-555-1234', '123 Main St, Charlotte, NC', 'alex@email.com');

-- Orders
INSERT INTO orders (customer_name, description, tracking_number, order_status, delivery_type, total_price, customer_id, promotion_id) VALUES
('Alex Rivera', 'No onions please', 'TRK123ABC', 'Pending', 'delivery', 28.50, 1, NULL);

-- Order Details
INSERT INTO order_details (order_id, sandwich_id, amount) VALUES
(1, 2, 2),   -- two Spicy Chicken Wraps
(1, 4, 1);   -- one Grilled Chicken Salad

-- Payment
INSERT INTO payments (order_id, card_number, card_holder, expiration_date, payment_type, amount, transaction_status)
VALUES (1, '4111-1111-1111-1111', 'Alex Rivera', '12/27', 'credit', 28.50, 'Pending');

-- Ratings (a low rating to demo low-rated dishes)
INSERT INTO ratings (customer_id, order_id, rating, review_text) VALUES
(1, 1, 1, 'The spicy wrap was way too salty.');