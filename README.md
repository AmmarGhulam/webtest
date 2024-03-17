# Coffee shop website
#### Video Demo:  <https://youtu.be/NFgdVYMijQM>
#### Description:

This website to help the owner to track all the income and outgoing for his/her coffee shop.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
To run locally, you must first clone the repository. After that run the following commands in the root of the repository:
```bash
flask run
```
then you can open the URL that the server provid you and try it

### Prerequisites

you have to install python from this website
https://www.python.org/downloads/


### Installing

Install flask from terminal
```
$ pip install -U Flask
```

## Running the tests

once you are in the main folder you can run this comand
```
$ flask run
```
then open the browser and visit 127.0.0.1:5000/


## Deployment

If you want to go live you have to upload it to any server and get the URL to access this website.


## License

There is no license needed for this project.

## Acknowledgments

For every one work in this course (CS50)

# what file do we have?

## app.py

The main page where you can see all nursery library then every page wheen you call it by get or by post.

## helper.py

this page is just to make sure the user is loged in or not.

## cherrybeans.db

database contain all the table needed to track and manage this website

-users table: all the user information stord in this table.
-orders table: any items that the coffe shop offers to sell for the costomers.
-purchases table: this table to store any outgoing from the coffee shop.
-cart table: to store every invoice with its detail
-transactions: show all the history for pirion of time.

## layout.html

This page is the layout for every other page

## register.html

To all new user to this website just to pick new username and password now any noe can create username but we can enhance it by make level of authorization.

## login.html

Login page to incure that the user match his password the one it stored in the database

## buy.html

This page when the user whant to puy any thing to the coffee shop once he/she add any item or service it will add to purchases table and history table.

## sell.html

The user use this page to add itmes that the costomers orders, onec it done it will add to cart table and transaction table.

## history.html

this page to see all the income and outgoing for pirod of time.

#  Running locally for development

To run locally, you must first clone the repository. After that run the following commands in the root of the repository:

```bash
flask run
```

then you can open the URL that the server provid you and try it

# note

This version is just to make sure we can insert into database and we can read fom it. It is possible to expand and cover more things rather than track the income ond outgoing. it depend on the customer when he agree about the system and agree
