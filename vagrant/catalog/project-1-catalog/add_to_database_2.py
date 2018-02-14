# coding: utf8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///project_catalog_with_users_final.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

json_data={}

json_data["restaurants"] = [
    {
      "user_id": 1,
      "name": "Big Chills",
    },
    {
      "user_id": 1,
      "name": "Tippling Street",
    },
    {
      "user_id": 1,
      "name": "Photobooth Cafe",
    },
]

json_data["menu_items"]=[
  {
   
      "name":"Veggie Burger", 
      "description":"Juicy grilled veggie patty with tomato mayo and lettuce",
      "price":"$7.50", 
      "course":"Entree", 
      "restaurant_id":1
  },
  {
   
      "name":"French Fries", 
      "description":"with garlic and parmesan",
      "price":"$7.50", 
      "course":"Entree", 
      "restaurant_id":2
  },
  {
  
      "name":"Chicken Burger", 
      "description":"Juicy grilled chicken patty with tomato mayo and lettuce",
      "price":"$7.50", 
      "course":"Entree", 
      "restaurant_id":3
  }
]
print(json_data)
data = json.dumps(json_data)
print(type(data))
d=json.loads(data)
print(d['restaurants'])


for e in d['restaurants']:
  restaurant_input = Restaurant(
    name=str(e['name']), 
    user_id=str(e['user_id']), 

    )
  session.add(restaurant_input)
  session.commit()

for i in d['menu_items']:
  menu_input = MenuItem(
    name=str(i['name']), 
    user_id=1,
    description=str(i['description']),
    price=str(i['price']),
    course=str(i['course']),
    restaurant_id=i['restaurant_id']
    )
  session.add(menu_input)
  session.commit()