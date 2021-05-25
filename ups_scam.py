from datetime import date
from selenium import webdriver
import time
import json
import random
import requests

tracking_url = 'https://52-55-65-224.cprapid.com/tracking/en/gb/'
address_url = 'https://18-190-156-86.cprapid.com/tracking/en/gb/address.php'
payment_url = 'https://18-190-156-86.cprapid.com/tracking/en/gb/payment.php'
confirmation_url = 'https://18-190-156-86.cprapid.com/tracking/en/gb/confirmation.php'
data = {
    'first_name': 'aaaaaaaaaaa',
    'last_name': 'aaaaaaaaa',
    'phone_number': '2222222222',
    'dob': 'aaaaaaa',
    'address': 'aaaaaaa',
    'countryCode': 'DZ',
    'city': 'aaaa',
    'postal_code': 'aaaaa',
    'recoverMyID': ''
}


response = requests.post(address_url, data=data).text
print(response)
time.sleep(50)
data = {
    'card_number': '5398706302348124',
    'exp_date': '33/33',
    'cvv': '333',
    'email': 'dog@yopmail.com',
    'recoverMyID':' '
}
response = requests.post(payment_url, data=data).text
print(response)

#Does not send any information, is currently stuck at homepage. Cannot click button