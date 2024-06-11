DELIMITER //

CREATE FUNCTION generate_random_id() RETURNS INT
BEGIN
    DECLARE rand_id INT;
    SET rand_id = FLOOR(100000 + (RAND() * 899999));
    WHILE EXISTS (SELECT 1 FROM user WHERE id = rand_id) DO
        SET rand_id = FLOOR(100000 + (RAND() * 899999));
    END WHILE;
    RETURN rand_id;
END //

DELIMITER ;

-- Bảng user
CREATE TABLE user (
    id INT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    phone VARCHAR(20),
    email VARCHAR(255)
);

DELIMITER //

CREATE TRIGGER before_insert_user
BEFORE INSERT ON user
FOR EACH ROW
BEGIN
    IF NEW.id = 0 THEN
        SET NEW.id = generate_random_id();
    END IF;
END //

DELIMITER ;

-- Bảng category
CREATE TABLE category (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

DELIMITER //

CREATE TRIGGER before_insert_category
BEFORE INSERT ON category
FOR EACH ROW
BEGIN
    IF NEW.id = 0 THEN
        SET NEW.id = generate_random_id();
    END IF;
END //

DELIMITER ;

-- Bảng product
CREATE TABLE product (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2),
    quantity INT,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES category(id)
);

DELIMITER //

CREATE TRIGGER before_insert_product
BEFORE INSERT ON product
FOR EACH ROW
BEGIN
    IF NEW.id = 0 THEN
        SET NEW.id = generate_random_id();
    END IF;
END //

DELIMITER ;

-- Bảng order
CREATE TABLE `order` (
    id INT PRIMARY KEY,
    date DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_price DECIMAL(10, 2),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

DELIMITER //

CREATE TRIGGER before_insert_order
BEFORE INSERT ON `order`
FOR EACH ROW
BEGIN
    IF NEW.id = 0 THEN
        SET NEW.id = generate_random_id();
    END IF;
END //

DELIMITER ;

-- Bảng order_item
CREATE TABLE order_item (
    id INT PRIMARY KEY,
    quantity INT,
    product_id INT,
    order_id INT,
    FOREIGN KEY (product_id) REFERENCES product(id),
    FOREIGN KEY (order_id) REFERENCES `order`(id)
);

DELIMITER //

CREATE TRIGGER before_insert_order_item
BEFORE INSERT ON order_item
FOR EACH ROW
BEGIN
    IF NEW.id = 0 THEN
        SET NEW.id = generate_random_id();
    END IF;
END //

DELIMITER ;
