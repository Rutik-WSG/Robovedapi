
from bson import ObjectId
from flask import Flask , request , jsonify
import pymongo
from flask_pymongo import PyMongo
import flask
from pymongo import MongoClient
#app = Flask(__name__)


app = Flask(__name__)

#client = MongoClient('localhost', 27017)
client = MongoClient('localhost', 27017, username='', password='')  #mongodb://localhost:27017
db = client.flask_db
todos = db.todos




#mongodb_client = pymongo.MongoClient("mongodb+srv://rutik:<password>@atlascluster.59beml7.mongodb.net/test")
# emp = myclient["roboveda"]


# robo_collection =emp["student"]
# doubt_collection = emp["user_doubt"]


# app.config['MONGO_URI'] = 'mongodb://database/roboveda'

# db = PyMongo(app)


# myclient = pymongo.MongoClient("mongodb+srv://iisd:sonali321@cluster0.aqlsjgn.mongodb.net/test", tlsCAFile=certifi.where())

# roboveda_db = myclient["IISD"]

# participant_collection =roboveda_db["student"]

#app = Flask(__name__)


# @app.route('/add', methods=['POST'])

# def add():
#     if request.method == 'POST':
#         pledge_data = request.get_json() 
#         name=pledge_data.get('name')
#         mobile=pledge_data.get('mobile')
#         email = pledge_data.get('email')
  
#         adds = robo_collection.insert_one({'name':name ,  'mobile' : mobile ,'email': email})
#         pledge_info = robo_collection.find_one({"_id":ObjectId(adds.inserted_id)})
#         return jsonify({'status':201,'user_id':str(pledge_info['_id']),'message':'new created successfully','data':{'user_id':str(pledge_info['_id'])},'error':False})
		
        #return jsonify({'message':'Something went wrong', },add_pledges) 
 
 
@app.route('/add', methods=['POST'])
def index():
    if request.method=='POST':
        data = request.get_json()
        name=data.get('name')
        mobile=data.get('mobile')
        email =data.get('email')
        todos.insert_one({' name':  name, 'mobile': mobile,"email":email})
        all_todos = todos.find()
        return jsonify(todos=all_todos)
        
        
        # content = request.form['content']
        # degree = request.form['degree']
        # todos.insert_one({'content': content, 'degree': degree})
        # return redirect(url_for('index'))

    # all_todos = todos.find()
    # return render_template('index.html', todos=all_todos)
 
# @app.route('/users', methods=['POST'])
# def create_user():
#     # Receiving Data
#     name = request.json['name']
#     email = request.json['email']
#     mobail=request.json['mobail_no']
#     if name and email and mobail:
        
#         id =db.users.insert({'name': name, 'email': email, "mobail_no":mobail })
#         response = jsonify({'_id': str(id),'name': name,'email': email,"mobail_no":mobail })
#         response.status_code = 201
#         return response
#     else:
#         return NOT_FOUND()

# @app.route('/mention_doubt', methods=['POST'])

# def mention_doubt():

# 	if request.method == 'POST':

# 		print("\n---Mention Doubt---")

# 		try:

# 			user_doubt_data = request.get_json()
# 			print(user_doubt_data)
			
# 			name=user_doubt_data.get('name')
			
# 			mobile=user_doubt_data.get('mobile')
# 			email = user_doubt_data.get('email')
			
# 			add_doubt = doubt_collection.insert_one({'name':name ,  'mobile' : mobile ,'email': email})

# 			doubt_info = doubt_collection.find_one({"_id":ObjectId(add_doubt.inserted_id)})
# 			return jsonify({'status':201,'user_id':str(doubt_info['_id']),'message':'new account created successfully','data':{'user_id':str(doubt_info['_id'])},'error':False})
	
# 		except Exception as e:
# 			return jsonify({'status':204,'message':'Something went wrong', 'error':e})

        
    

if __name__ == "__main__":
    app.run(debug=True)