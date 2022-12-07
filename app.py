
import email
import json
from flask import Flask, Response, request, jsonify
from flask_mongoengine import MongoEngine
from flask_mail import Mail,Message
import os
#from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint


app = Flask(__name__)


configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '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 '



# app.config['MAIL_SERVER']='smtp-relay.sendinblue.com'
# app.config['MAIL_USERNAME']='rutikd@wharfstreetstrategies.com'
# app.config['MAIL_PASSWORD']=os.environ.get('CnvTOtfQqk9XE1Jw')
# app.config['MAIL_PORT']=587
# app.config['MAIL_USE_TLS']=False
# app.config['MAIL_USE_SSL']=True



# mail = Mail(app)



app.config['MONGODB_SETTINGS'] = {
    'db': 'roboveda',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)







class emp(db.Document):
    name = db.StringField()
    mobile=db.IntField()
    email = db.StringField()
    def to_json(self):
        return {"name": self.name,
                "mobile_no":self.mobile,
                "email": self.email}



api_instance = sib_api_v3_sdk.ContactsApi(sib_api_v3_sdk.ApiClient(configuration))
repeat_contact_api_instance = sib_api_v3_sdk.ListsApi(sib_api_v3_sdk.ApiClient(configuration)) #lists-api
transaction_mail_api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration)) #transactional-emails-api 
create_contact = sib_api_v3_sdk.CreateContact(email= "serrrdhjike212006@gmail.com",  ) # CreateContact | Values to create a contact

try:
    # Create a contact
    api_response = api_instance.create_contact(create_contact)
    #pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->create_contact: %s\n" % e)



@app.route('/add', methods=['POST'])
def create_record():
            record = json.loads(request.data)
            user = emp(name=record['name'],
            mobile=record['mobile_no'],
            email=record['email'])
            user.save()
            return jsonify(user.to_json(),{"message":"Data Succefully Add"})


    # create_contact = sib_api_v3_sdk.CreateContact(email=email, attributes = { "FIRSTNAME" : name }, list_ids=[5])
				
	# 			#create contact of the registered user in sendinblue
    # try:
    #     contacts_api_instance.create_contact(create_contact)
    # except:
    #       try:
    #         list_id = 5                 # contact_list ID
    #         contact_emails = sib_api_v3_sdk.AddContactToList()
    #         contact_emails.emails = [email]
    #         try:
    #             repeat_contact_api_instance.add_contact_to_list(list_id, contact_emails)
    #         except ApiException as e:
    #             print("Exception when calling ListsApi->add_contact_to_list: %s\n" % e)
    #         except Exception as e:
    #             print("Exception in Repeat Add Contact")



# @app.route("/",methods=["POST"])
# def index():
#     if request.method=="POST":
#         msg = Message("Hello",
#                   sender="rutik24@gmail.com",
#                   recipients=["rutikd@wharfstreetstrategies.com"])
#         msg.body="how are you"
#         mail.send(msg)
#         return Response('meassge sent')
    
    

if __name__ == "__main__":
    app.run(debug=True)