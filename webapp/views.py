

#!/usr/bin/python
# coding: utf-8
from webapp import app
 
# importing application wide parameters and global variables that have been
# defined in __init__.py
message = app.config['HELLO_WORLD']
 
@app.route('/')
def webapp():
  return message

import view_search
