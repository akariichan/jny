from flask import Flask
app = Flask (__name__)

@app.route('/items', methods=['GET'])

def get_items():
   return "Getting all items."
@app. route('/items', methods=['POST' ])
def create_item():
  return "Creating a new item."
