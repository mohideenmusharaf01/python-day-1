# ======================================================================
# CREATE DATABASE LibraryDB
# ======================================================================

create database LibraryDB;
use LibraryDB;


# ======================================================================
# SCHEMA OF LibraryDB
# ======================================================================

create table Books(book_id int primary key,book_name varchar(50),author varchar(30),price int);

create table Members(mem_id int primary key,mem_name varchar(50),city varchar(30),phone int);

create table Borrow(brw_id int primary key,book_id int,mem_id int,brw_date date);

alter table Books add category varchar(30);
alter table Books add quantity int;
alter table Members add email varchar(30);
alter table Borrow add return_date date;
alter table Books modify price decimal(10,2);
alter table Books change quantity stock_quantity int;

insert into Books(book_id,book_name,author,price,category,stock_quantity)
values
(1, 'The Alchemist', 'Paulo Coelho', 299.00, 'Fiction', 25),
(2, 'Atomic Habits', 'James Clear', 450.00, 'Self Help', 30),
(3, 'Harry Potter', 'J.K. Rowling', 399.00, 'Fantasy', 20),
(4, 'The Hobbit', 'J.R.R. Tolkien', 350.00, 'Fantasy', 15),
(5, 'Wings of Fire', 'A.P.J. Abdul Kalam', 250.00, 'Biography', 40),
(6, '1984', 'George Orwell', 300.00, 'Dystopian', 18),
(7, 'The Great Gatsby', 'F. Scott Fitzgerald', 275.00, 'Classic', 22),
(8, 'Rich Dad Poor Dad', 'J.K. Rowling', 320.00, 'Finance', 35),
(9, 'Ikigai', 'Paulo Coelho', 280.00, 'Self Help', 28),
(10, 'Pride and Prejudice', 'J.K. Rowling', 330.00, 'Romance', 17);

insert into Members(mem_id,mem_name,city,phone,email)
values
(1, 'Arun Kumar', 'Chennai',987654210, 'arun@gmail.com'),
(2, 'Priya Devi', 'Madurai',987653211, 'priya@gmail.com'),
(3, 'Rahul Raj', 'Coimbatore',987654312, 'rahul@gmail.com'),
(4, 'Sneha', 'Salem',987654313, 'sneha@gmail.com'),
(5, 'Karthik', 'Trichy',987643214, 'karthik@gmail.com'),
(6, 'Divya', 'Erode',987654215, 'divya@gmail.com'),
(7, 'Vijay', 'Tirunelveli',987654216, 'vijay@gmail.com'),
(8, 'Anitha', 'Thanjavur',987653217, 'anitha@gmail.com');

insert into Borrow(brw_id,book_id,mem_id,brw_date,return_date)
values
(1, 1, 1, '2026-09-01', '2026-09-10'),
(2, 2, 5, '2026-09-02', '2026-09-12'),
(3, 1, 3, '2026-09-03', '2026-09-13'),
(4, 3, 4, '2026-09-04', '2026-09-14'),
(5, 4, 5, '2026-09-05', '2026-09-15'),
(6, 1, 6, '2026-09-06', '2026-09-16'),
(7, 5, 7, '2026-09-07', '2026-09-17'),
(8, 3, 8, '2026-09-08', '2026-09-18'),
(9, 6, 7, '2026-09-09', '2026-09-19'),
(10, 7, 4, '2026-09-10', '2026-09-20');

insert into Books(book_id,book_name,author,price,category,stock_quantity)
values(11, 'The Psychology of Money', 'Morgan Housel', 399.00, 'Finance', 25);

insert into Members(mem_id,mem_name,city,phone,email)
values(9, 'Mohammed Ali', 'Bangalore', 987654329, 'mohammed@gmail.com');

insert into Borrow(brw_id,book_id,mem_id,brw_date,return_date)values(11, 11, 9, '2026-09-11', '2026-10-01');

update Books set price=430 where book_id =3;

update Books set price=price*1.10 where category='Fantasy';

update Books set stock_quantity=stock_quantity+5;

update Books set stock_quantity=0 where book_id in (3,5,7);

update Members set city='Tenkasi' where mem_id=4;

update Members set email='abdpuchandi@gmail.com'where mem_id=5;

update Books set category='Motivation' where book_id=5;

update Borrow set return_date='2026-09-21'
where brw_id=11;

delete from Books
where book_id=6;

delete from Members where mem_id not in(
select mem_id from Borrow);

delete from Borrow where brw_id=7;

delete from Books where stock_quantity=0;


# ======================================================================
# QUERIES OF LibraryDB
# ======================================================================

select*from Books;
select*from Members;
select*from Borrow;
select book_name,author from Books;
select book_name,category,price from Books;
select * from Books where price > 300;
select * from Books where price < 300;
select * from Books
where price between 300 and 400;
select * from Books where category='Finance';
select * from Books where author='James Clear';
select * from Books where book_name like 'p%';
select * from Books where book_name like '%it%';
select * from Books where category in('Self Help','Finance');
select * from Books where price != 320;
select * from Books where stock_quantity > 30;
select * from Books
where stock_quantity between 2 and 30;
select * from Books order by price asc;
select * from Books order by price desc;
select * from Books order by book_name asc;
select * from Books order by category,price;
select * from Books order by price desc limit 3;
select * from Books order by price limit 3;
select * from Books order by stock_quantity desc limit 5;
select * from Members order by mem_name limit 5;
select * from Borrow
order by brw_date desc limit 5;
select count(*) as total_books from Books;
select count(*) as total_members from Members;
select count(*) as total_borrow from Borrow;
select sum(stock_quantity) as book_to_qnty from Books;
select sum(price) as book_tot_price from Books;
select avg(price) as book_avg_price from Books;
select max(price) as book_max_price from Books;
select min(price) as book_min_price from Books;
select max(price) - min(price)
as book_difference from Books;
select avg(stock_quantity) as book_avg_stqnty from Books;
select category,count(*) as category_count from Books group by category;
select category,avg(price) as category_avg_price from Books group by category;
select category,max(price) as category_max_price from Books group by category;
select category,min(price) as category_min_price from Books group by category;
select category,sum(stock_quantity) as category_tot_stock from Books group by category;
select category,sum(price*stock_quantity) as category_tot_book_price from Books group by category;
select category,count() as cat_tot_book from Books group by category having count() > 1;
select category,avg(price) as avg_book_price from Books group by category having avg(price) > 350;
select author,count(*) as auth_each_book from Books group by author;
select author,avg(price) as auth_avg_price from Books group by author;
select category,count() as cat_tot_book from Books group by category having count() > 1;
select category,avg(price) as avg_book_price from Books group by category having avg(price) < 350;
select author,count() as auth_each_book from Books group by author having count() > 1;
select category,sum(stock_quantity) as category_tot_stock from Books group by category having sum(stock_quantity) > 30;
select author,avg(price) as auth_avg_price from Books group by author having avg(price) > 350;


# ======================================================================
# PERMISSIONS OF LibraryDB
# ======================================================================

create user 'library_user'@'localhost' identified by 'library123';

grant select on LibraryDB.Books to 'library_user'@'localhost';

grant insert on LibraryDB.Books to 'library_user'@'localhost';

grant update on LibraryDB.Books to 'library_user'@'localhost';

show grants for 'library_user'@'localhost';

revoke insert on LibraryDB.Books from 'library_user'@'localhost';

revoke update on LibraryDB.Books from 'library_user'@'localhost';

grant select on LibraryDB.* to 'library_user'@'localhost';

revoke select on LibraryDB.Books from 'library_user'@'localhost';

show grants for 'library_user'@'localhost';
