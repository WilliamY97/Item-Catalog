# CatalogIt

By William Yang

Developed a content management system using the Flask framework in Python. Authentication is provided via OAuth and all data is stored within a PostgreSQL database.

It provides a list of items within a variety of categories as well as a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

# Instructions

## Running The Application

*Install Vagrant and VirtualBox
*Clone this repository
*Open terminal an cd into the folder
*Execute the command Vagrant Up to launch Vagrant VM
*Execute the commant Vagrant ssh to gain access to shell
*CD into /vagrant and then into the catalog folder
*Run python catalogit.py to launch application
*Open a browser of your choice and navigate to http://localhost:5001/
*You will now have access to the web application

## Navigating The Application
* You must first log in using Google to create a new catalog
* Click "Create New Catalog" and give it a name
* Click "Create New Category" and give it a name
* Each one of the categories is populated by records.
* To create a record you must first create a record template which
defines the details of what can be added about the record (e.g. description)
* Once you create a record template you can then click on it to create a record
* You may edit any level of the catalog by clicking the pencil icon.
* Additionally you may delete any level of the catalog by click the trash icon.
* Note: Any levels below the catalog level you delete will be deleted as well.
* Note: You can only edit/delete catalogs you made with your own account.
* Note: The update column on the right side shows recent actions performed.
