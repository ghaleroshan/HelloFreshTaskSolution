# Get Ingredients

Fetches the ingredients from the database using peewee and flask. Renders the fetched data using vue in the frontend.

## Solution formulation

Steps I thought of and executed for solving the getIngredient:

- First understood the database model and how all the tables were linked
- Went through step by step process of sql query from basic queries and move on accordingly
- Learned how peewee and sqlite query are written and translated the sql query in to sqlite query
- Learned how python works and how to created an endpoint to get all the ingredients

## Libraries/Tools used

- No main dependency basic use of Flask and peewee as provided.
- For FrontEnd used axios to fetch the data from the api

## How to setup

- Extract the zip file
- open the folder back in your favorite code editor
- install all the dependencies
- run the main.py file using `python3 main.py` (this will provide you with the localhost url endpoint which we will use for the frontend to fetch)
- Go to the front folder and simply open the index.html file in your browser
- you should be able to see the list of the ingredients

## Decisions and tradeoffs

- I was not able to get the correct volume and display them accordingly as I had limited time to learn everything from scratch. (I know this is just my excuse but if I am given an opportunity I am sure that I will be able to complete it with finesse.)
