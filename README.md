# Restaurant Invoice System

In this project my aim to create a restaurant invoice system whose provide by the restaurant to the customer.

## Technology & Concept:

In this I am using the Tkinter library for the designing all windows. Mysql is used for database storing the username and password. File handling used for saving the invoice soft copy in text form. You can see on the directory customer in the project and regular expressions are used for creating the total of the all items in the invoice. 

## System Requirements:

• Python 3.7 [download](https://www.python.org/downloads/)

• Tkinter library for GUI download steps:
    
   ◦ Open cmd(window) or terminal(ubuntu/linux)
   
   ◦ Write command pip install tkinter(in window) or sudo apt-get install python3.6-tk (in ubuntu)

• Mysql : If need in your system you can be download and install on [link](https://www.mysql.com/downloads/)
    
	◦ Write command in cmd  pip install mysql for link between mysql and python.

## How to run:

* Open cmd on location where you are save/download project and write the command python login_page.py ->press enter like:

![cmd](/restaurant/images/pyfileopen.png)

* After some time the following window is appear:

![open file in cmd](restaurant/images/login.png)

* Enter user root and password is root which you are enter unter the db restaurant and  in the mysql table like login:
    * Firstly you are create a database in mysql name restaurant and create a table under the restaurant database name login. 
    
    ![first screen](restaurant/images/database1.png)

    ![change database](restaurant/images/changedatabase.png)
    
    * Enter the user whose want to login in yours software like following users:

    ![table data show](restaurant/images/tablesdatashow.png)

* Login by the given mysql login table users:

![login](restaurant/images/login1.png)

* After login the add the customer details like customer number, name, address, mobile number ,allocated table(like following):

![Add Customer](restaurant/images/customer.png)

* Select the items under the course whose want to customer :

![Course item select]( restaurant/images/course.png)

* After selection the dishes click on the final button and the click on the bill button:

![Final Bill](restaurant/images/bill.png)
