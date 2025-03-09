# This code represents a simulation for WA Bulk Messaging
# To create an actual production app, I must have a subscription which I have no purpose to pay for
# But in case, changes to this code wouldn't be too much

import pandas as pd
import requests
import json

with open("test_setup_config.json") as config:
    data = json.load(config)
# print(data)

# The endpoint's URL
url = f"https://graph.facebook.com/v22.0/{data['phoneNumID']}/messages"

# Requests Header (These are general across any message request)
headers = {
    "Authorization": f"Bearer {data['AccessToken']}",
    "Content-Type": "application/json"
}

# The "data section" of the request is going to change based on the customer's number we're contacting
cols_to_load = ['firstName', 'phoneNum']
contacts_df = pd.read_csv(data['ContactsCSV'], skipinitialspace=True, usecols=cols_to_load)[['firstName', 'phoneNum']] # The additional part is for reserving order
# Skipping the initial space with the second parameter is essential in cases you're using this format
# in your csv file: x, y, z
# Otherwise, trying to read 'y' column won't work cuz it's read as ' y'
print(contacts_df.head())

# Now, we get the number of non-null phoneNumbers
length = contacts_df.shape[0]
for i in range(length):
    customer = contacts_df.iloc[i] # Accessing the ith row in the df as a series
    firstName = customer['firstName']
    phoneNum = customer['phoneNum']
    if pd.notna(phoneNum) and str(phoneNum).isdigit():
        data = {
            "messaging_product": "whatsapp",
            "to": f"{phoneNum}",
            "type": "template",
            "template": {
                "name": "hello_world",
                "language": {"code": "en_US"},
                # "components": [
                #     {
                #         # https://developers.facebook.com/docs/whatsapp/cloud-api/reference/messages#template-object
                #         # https://developers.facebook.com/docs/whatsapp/cloud-api/reference/messages#components-object
                #         "type": "body",
                #         "parameters": [{"type": "text", "text": f"Hey, {firstName}!"}] #Adding first name to the msg template
                #     }
                # ]
            }
        }
        try:
            response = requests.post(url, headers=headers, json=data)
            # Print the response status and response content
            print(response.status_code) 
            print(response.json())
        except Exception as e:
            print(f"Error: This URL can't be reached!\n{e}")

