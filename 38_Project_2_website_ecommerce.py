
# Ecommerce website using the Django Framework
# https://www.djangoproject.com/

# A framwork is a library of re-usable modules 
# It also defines a structure for our applications 

##  INSTALL DJANGO
# pip install django==2.1

## CREATE A WORKSPACE FOR YOUR PROJECT (Be in the folder)
# django-admin startproject pyshop .

## START YOUR DJANGO SERVER
# python3 manage.py runserver
# navigate to the URL E.g. http://127.0.0.1:8000/

# CREATE YOUR FIRST APPLICATION
# The following command will create a folder called products and has a base of a webshop already for us
# python3 manage.py startapp products
# Ammend the views.py under the products folder to add an index
# Create a new file called urls.py under the products folder to define the URL mapping 
# Edit the urls.py in the root of the pyshop folder
# http://127.0.0.1:8000/products/

# CREATING THE MODELS
# Edit the models.py under the products folder.

# DATABASE
# Download this so we can connect to the DB https://sqlitebrowser.org/dl/
# sudo apt-get install sqlitebrowser -y
# Open the DB Program and open the db.sqllite3 file in the progrm
# Edit the settings.py under the pyshop folder
# python3 manage.py makemigrations    <-- Should make a model for you
# python3 manage.py migrate
# Open the DB Program and open the db.sqllite3 file in the progrm (Again, you will see data now) 
    # Add new class to the DB
        # Add the class to models.py
        # python3 manage.py makemigrations   
        # python3 manage.py migrate
        # Open the DB Program and open the db.sqllite3 file in the progrm (Again, you will see data now) 

# ADMIN PAGE
# http://127.0.0.1:8000/admin/
# python3 manage.py createsuperuser
# admin
# admin
# Edit the admin.py in the products foldr
# http://127.0.0.1:8000/admin/ -- Click on products
# Add a new product
    # GOTCHA
        # Delete the DB File it fails then run 
        # python3 manage.py makemigrations    <-- Should make a model for you
        # python3 manage.py migrate


# CREATING BETTER PRODUCT MANAGEMENT
# Edit the admin.py under products

# CREATING OFFERS Page
# edit the admin.py in products <-- This will add a new class and register it

# CREATING THE LANDING PAGE WITH TEMPLATES
# Open the view.py under products edit this 
# create a templates directory under products  - add new file index.html
# Base.html code Starter Template (gets edited) comes from https://getbootstrap.com/docs/5.1/getting-started/introduction/
# Card code comes from https://getbootstrap.com/docs/5.1/components/card/


# Start the Server
# python3 manage.py runserver