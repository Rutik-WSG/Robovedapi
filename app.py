
import email
import json
from flask import Flask, Response, request, jsonify
from flask_mongoengine import MongoEngine
from flask_mail import Mail,Message
import os
#from __future__ import print_function
import time
import razorpay
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint


app = Flask(__name__)

razorpay_client = razorpay.Client(auth=("rzp_test_hAYTO5a3WVZkPe", "RhY3gSMz6U1ejJXdliestlZu"))

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] ='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 '                             


app.config['MONGODB_SETTINGS'] = {
    'db': 'roboveda',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)


#=========================================================================================================================================




code = (('Basic', 'Basic entry Ticket @INR 399/-'),
            ('Premium', 'Premium entry Ticket @INR 699/-'),
            ('Master', 'Master entry Ticket @INR 799/-'),
            ('Pardarshan', 'Pardarshan entry Ticket @INR 200/-'),
            ('IoT', 'IoT Workshop Ticket @INR 800/-'),
            ('Drone', 'Drone Workshop Ticket @INR 800/-'),)
  


class emp(db.Document):
    name = db.StringField()
    mobile=db.IntField()
    email = db.StringField()
   
    ticket = db.StringField(max_length=20, choices=code, required = True)
    def to_json(self):
        return {"name": self.name,
                "mobile_no":self.mobile,
                "email": self.email,
                "ticket ": self.ticket,
                
                
                }
        
class amount(db.Document):
    amount=db.IntField()
    def to_json(self):
        return {" amount": self.amount,}


    

   
#==============================================================================================================================================================


api_instance = sib_api_v3_sdk.ContactsApi(sib_api_v3_sdk.ApiClient(configuration))
repeat_contact_api_instance = sib_api_v3_sdk.ListsApi(sib_api_v3_sdk.ApiClient(configuration)) #lists-api
transaction_mail_api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration)) #transactional-emails-api 

create_contact = sib_api_v3_sdk.CreateContact(email= "sdk212006@gmail.com",  ) # CreateContact | Values to create a contact

try:
    # Create a contact
    api_response = api_instance.create_contact(create_contact)
    #pprint(api_response)
except ApiException as e:
    #print(e)
    print("Exception when calling ContactsApi->create_contact: %s\n" % e)

#---------------------------------------------------------------------------------------------------------------------------------------

@app.route('/add', methods=['POST'])
def create_record(): 
    record = json.loads(request.data)
    user = emp(name=record['name'],
               mobile=record['mobile_no'],
               email=record['email'],
               ticket=record['ticket'],
             
             )
    user.save()
    
    return jsonify(user.to_json(),{"message":"Data Succefully Add"})




@app.route('/charge', methods=['POST'])
def app_charge():
    if request.method=="POST":
        #data = request.get_json()
        global payment,name                 #,razorpay_key,rezorpay_secret 
        name=request.form.get('name')
        mobile=request.form.get('mobile')
        email = request.form.get('email')
        amount=request.form.get('amount')
        notes={'name':name,"mobile":mobile,"email":email}
       # notes.save()
        amount = 200*1000
        currency="INR"
        client=razorpay.Client(auth=("rzp_test_hAYTO5a3WVZkPe", "RhY3gSMz6U1ejJXdliestlZu"))           #auth=(razorpay_key,rezorpay_secret ))
        payment=client.order.create({'amount':amount,'currency':currency,'payment_capture':1,'notes':notes})
        return jsonify(payment=payment )#,razorpay_key=razorpay_key)    

if __name__ == "__main__":
    app.run(debug=True)
    
    