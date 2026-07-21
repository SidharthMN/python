create database lumira;
use lumira;
create table product_details(product_id int primary key auto_increment ,product_name varchar(30) not null , category varchar(30) , price decimal(10,2) , stock int default 0);
alter table product_details modify price decimal(10,3);
alter table product_details add column rating decimal(5,5);
select* from product_details;
ALTER TABLE product_details MODIFY COLUMN rating DECIMAL(3,1);
insert into product_details (product_name,category,price,stock,rating) values ('iPhone 15', 'Electronics', 799.99, 50, 4.8),
('Galaxy S24', 'Electronics', 749.99, 45, 4.6),
('MacBook Air', 'Computers', 999.99, 20, 4.9),
('Sony WH-1000XM5', 'Audio', 349.99, 0, 4.7);
select product_name , price from product_details;
select* from product_details;
select product_name from product_details where stock=0;
select* from product_details;
select* from product_details where category = "Electronics";
select* from product_details where category = "Electronics" or category = "Computers";
select* from product_details where category = "Electronics" and price < 750;
SET SQL_SAFE_UPDATES = 0;
update product_details set stock = 35 where product_name ="MacBook Air";
select* from product_details;
delete from product_details where product_id = 2;
SET SQL_SAFE_UPDATES = 0;
select* from product_details;
select product_name,rating from product_details order by rating desc limit 2;
select avg(price) as Average from product_details;
select category as Category,count(*) as Count,sum(stock*price) as Sum from product_details GROUP BY category;
select* from product_details;

create table customer_details (customer_id int primary key auto_increment ,customer_name varchar(30) not null, favourite_product int , foreign key(favourite_product) references product_details(product_id));
desc customer_details;
insert into customer_details (customer_name,favourite_product) values ('Alice Smith', 1),('Bob Jones', 3);
select* from customer_details;
select* from product_details;

select c.customer_name,p.product_name from customer_details as c join product_details as p on c.favourite_product = p.product_id;

create table orders (order_id int primary key auto_increment , customer_id int,product_id int,quantity int default 1, order_date date);
desc orders;
truncate table customer_details;
select* from customer_details;
alter table customer_details drop foreign key customer_details_ibfk_1;
alter table customer_details drop column favourite_product;
select* from customer_details;
insert into customer_details (customer_name) values ('Alice Smith'),('Bob Jones'),
('Charlie Brown'), 
('Diana Prince');
insert into orders (customer_id, product_id, order_date, quantity) values (1, 1, '2026-06-01', 1),
(1, 3, '2026-06-03', 1),
(2, 1, '2026-06-04', 2),
(3, NULL, '2026-06-05', 1);
select* from orders;
select c.customer_name , o.order_id , o.order_date  from orders as o join customer_details as c on o.customer_id = c.customer_id;
select c.customer_name from customer_details as c left join orders as o on c.customer_id = o.customer_id where order_id is null;
select p.product_name , p.product_id from product_details as p left join orders as o on p.product_id = o.product_id where o.order_id is null;
select c.customer_name, p.product_name, o.quantity from orders as o join product_details as p on o.product_id = p.product_id  join customer_details as c on o.customer_id = c.customer_id;
select c.customer_name, p.product_name, o.quantity from customer_details as c left join orders as o on o.customer_id=c.customer_id  left join product_details as p on p.product_id = o.product_id
union
select c.customer_name,p.product_name,o.quantity from product_details as p left join orders as o on o.product_id = p.product_id left join customer_details as c on c.customer_id = o.customer_id;
