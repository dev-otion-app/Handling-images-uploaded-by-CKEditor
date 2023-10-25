This repository demonstrates what is explained in https://dev-otion.com/en/entry/

In order to install the minimal requirements to use this example, create a virutial environment with Python 3.11.4 and run `pip install -r requirements.txt`

The `img` folder contains some images to work with.

The SQlite database provided in the repository contains the models used in the example, if you want to modify the models remember to carry out the migrations. An admin user is already defined:
- ID: admin 
- Password: 123456. 

You can create as many admins as you need by running `python manage.py createsuperuser`
