#!vflask/bin/python3.5
from app import app
import os

# app.run(debug=True)

#use below for running on c9
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 9000)))