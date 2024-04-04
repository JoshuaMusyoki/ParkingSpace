import os
from flask import Flask, request

app = Flask(__name__)

username = " chuka_devs"
api_key = "5e8899b7edea5e1cfda0d34088b49bcd354ddcbde963dd0dc2a6329a204015e2"


@app.route("/ussd",methods = ['POST', 'GET'])
def ussd():
    session_id   = request.values.get("sessionId", None)
    serviceCode  = request.values.get("serviceCode", None)
    phnoe_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    
    if text == "":
       response  = "CON Welcome to ParkingSpace Nairobi City!"
       response += "1. Select your Constituency"  
       
    elif text == "1" :
        response = "CON Choose the location"
        response += "1. Langata"  
        response += "2. Westlands"   
        response += "3. Embakasi"   
        response += "4. Kibra"    
        
    elif text == "1":
        response = "The available spaces around ", response +"are:" 
        response += "1. Mama Lucy \n 2. Kwa Chief \n 3. GGGG"    
        
    elif text == "2":
        response = "The available spaces around ", response +"are:" 
        response += "1. Mama Lucy \n 2. Kwa Chief \n 3. GGGG"   
        
    elif text == "3":
        response = "The available spaces around ", response +"are:" 
        response = "1. Mama Lucy \n 2. Kwa Chief \n 3. GGGG"   
    
    elif text == "4":
        response = "The available spaces around ", response +"are:" 
        response = "1. Mama Lucy \n 2. Kwa Chief \n 3. GGGG"    
        
    return response
if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=os.environ.get('PORT'))