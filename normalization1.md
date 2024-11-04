Customer ( **Customer_id**, Customer_name, Address, Tel_no, Email, { Order_id, Order_date, Total_amount { Product_id, Product_description, Finish, Quantity, Unit_price, Extended_price } })

1NF:

Customer-1 ( **Customer_id**, Customer_name, Address, Tel_no, Email )

Order-1 (**Order_id**, Order_date, Total_amount, *Customer_id* )

Product-1 ( **Product_id**, Product_description, Finish, Quantity, Unit_price, Extended_price, *Order_id*, *Customer_id* )

# 2NF:
## Order-1
Order_id -> X

Customer_id -> X

Order_id, Customer_id -> Order_date, Total_amount

## Product-1
Product_id -> Product_description, Finish, Unit_price, Extended_price

Order_id -> X

Customer_id -> X

Product_id, Order_id -> Quantity

Product_id, Customer_id -> X

Order_id, Customer_id -> X

Product_id, Order_id, Customer_id -> X

### Final Tables
Customer-2 ( **Customer_id**, Customer_name, Address, Tel_no, Email )

Order-Customer-2 (**Order_id, Customer_id**, Order_date, Total_amount)

Product-2 (**Product_id**, Product_description, Finish, Unit_price, Extended_price)

Product-Order-2 (***Product_id, Order_id***, Quantity)

### Already in 3NF