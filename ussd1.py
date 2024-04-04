import os
from flask import Flask, request

app = Flask(__name__)

packing_spaces = {
    "Nairobi Garage": {"available": True, "price": 200},
    "Westlands": {"available": False, "price": 150},
}
# Check if slot is available
def is_slot_available(location):
    return packing_spaces.get(location, {}).get("available", False)

# Function to get the price of a slot
def get_slot_price(location):
    return packing_spaces.get(location, {}).get("price", 0)

# Getting price of a slot
def book_slot(location):
     print(f"Slot booked for location: {location}")
     return True
 
#  Function to initiate stk push
def initiate_stk_push(phone_number, amount):
    # Simulate STK Push call to your payment gateway
    print(f"STK Push initiated for phone number: {phone_number}, amount: {amount}")
    return True

@app.route("/ussd", methods = ['POST'])
def ussd():
  # Read the variables sent via POST from our API
  session_id   = request.values.get("sessionId", None)
  serviceCode  = request.values.get("serviceCode", None)
  location = request.values.get("location", None)
  text         = request.values.get("text", "default").strip()
  
  response = ""

  if text      == '':
      # This is the first request. Note how we start the response with CON
      response = (
          session_id,
          "CON Welcome to ParkingSpace Nairobi City!",
      )
      options=[
              "1. View Parking Slots",
              "2. Learn More!",
          ]
      
    

  elif text    == '1':
      # Business logic for first level response
      options = ["1. Choose location"]
      for location in packing_spaces.keys():
          options.append(f"{len(options)}. {location}")
      response = (
          session_id,
          "CON Choose the location you want to view parking slots:",
      )
      options = options
  elif text.isdigit() and int(text) <= len(packing_spaces):
        # Selected location (handle both single-digit and double-digit options)
        selected_location_index = int(text) - 1
        location = list(packing_spaces.keys())[selected_location_index]

        if is_slot_available(location):
            response = ussd.build_response(
                session_id,
                f"CON Parking slot available at {location}. Price: Ksh {get_slot_price(location)}",
                options=[
                    "1. Book Slot",
                    "2. Go Back",
                ]
            )
        else:
            response = ussd.build_response(
                session_id,
                "END Sorry, no parking slots available at this location."
            )
            
  elif text == "1.1":
        # Learn More (replace with your content)
        response = ussd.build_response(session_id, "Thank you for using ParkingSpace!", end_session=True)

  elif text in ("1", "2"):
        # Book Slot or Go Back from location selection
        if text == "1" and is_slot_available(location):
            # Book Slot
            if book_slot(location):
                # Initiate STK Push payment
                phone_number = request.values.get("phoneNumber")  # Get user's phone number
                amount = get_slot_price(location)
                if initiate_stk_push(phone_number, amount):
                    response = ussd.build_response(
                        session_id,
                        "END Slot booked successfully! You will receive an M-Pesa Stk Push"
                    )

  else :
      response = "END Invalid choice"

  # Send the response back to the API
  return response

if __name__ == '__main__':
    app.run(debug=True)