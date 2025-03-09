# WhatsApp Bulk Messaging

## 📌 Overview

This project automates bulk messaging via WhatsApp using the **Meta WhatsApp Cloud API**. It is designed for businesses to send messages to multiple customers efficiently. While the current implementation uses a testing account, switching to a **paid account** allows full bulk messaging capabilities with **custom templates** and unrestricted recipient messaging.

## 🚀 Features

- Reads customer contact details (name and phone number) from a CSV file.
- Sends WhatsApp messages using the **pre-approved** `hello_world` template in testing mode.
- Uses **Meta's API** with proper authentication.
- Supports **bulk messaging** by reading numbers from a CSV file.
- Easily configurable for production use with **custom templates**.
- **Recommended:** Uses `argparse` to pass the message as a command-line argument.

## 🛠️ Requirements

### 🔹 Prerequisites

Ensure you have the following installed:

- Python 3.x
- Required libraries (listed in `requirements.txt`)

You can install dependencies using:

```
pip install -r requirements.txt
```

### 🔹 Setup

**Note:** Before configuring and using this project, you must create a **Meta Business Account** and set up a **Business Portfolio** to be able to add WhatsApp to your app.

Follow these steps:

1. Create a **Meta Developer Account**

2. Create a **Business App**

3. Add Products to this app (WhatsApp, Instagram, Facebook, etc.)

4. Set up a **Meta Business Portfolio**&#x20;

5. Click on **“Setup API”**

6. Create an Access Token**

7. Add a Valid Recipient WhatsApp Number** (to receive test messages)

8. Create a **JSON file** with the following structure:

   ```json
   {
       "phoneNumID": "YOUR_PHONE_NUMBER_ID",
       "AccessToken": "YOUR_ACCESS_TOKEN",
       "ContactsCSV": "customers.csv"
   }
   ```

9. Prepare a **CSV file** for customers' data:

   ```csv
   firstName,phoneNum
   Alice,1234567890
   Bob,0987654321
   ```

## 📜 Usage

Run the script using:

```
python script.py 
```

## 🔍 Code Explanation

- **Reads JSON config**: Loads API credentials and CSV file path.
- **Loads contacts**: Reads customer details into a DataFrame.
- **Iterates over contacts**: Sends a message to each phone number using Meta's WhatsApp API.
- **Handles missing values**: Skips invalid or empty phone numbers.

## ❗ Limitations

- In **testing mode**, 5 verified numbers can receive messages.
- Freeform messages and custom templates require a **paid subscription**.

## 🎯 Future Enhancements

- Support for **custom templates** (for paid accounts).
- Implementing **logging** for tracking sent messages.
- **Enhancing message customization** beyond simple placeholders.
- Use the args module to enable the user to enter their custom message at runtime.

## ⚠️ Disclaimer

This project is intended **for professional bulk messaging purposes**. Ensure all recipients have provided **opt-in consent** to comply with WhatsApp's policies.

