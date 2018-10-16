# Table Exatract From XML 

This app is to extract data from tables founded in articles. Articles 
are on XML format. 

## File structure 
- src 
Here you will find all source code of the app. 
In this folder we have two files:
    - app.py which contain the maim of our app
    - Article.py which is a class that is used for accessing information 
from the XML file 
- data 
Here you have to put you XML article on which the tables information
will be extracted

## How to use 
Put you XML article in the data folder. 
From the app.py file set the name of the XML article in the **file** 
variable. 
Call this variable as argument for the creation of the Article object. 
Run and se test result 