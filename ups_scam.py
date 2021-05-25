from datetime import date
from selenium import webdriver
import time
import json
import random
import threading


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
            random_CC = (data[rand]["CreditCard"]["CardNumber"])

        with open('addresses.json') as f:
            data = json.load(f)
            address = (data[rand]["address"])
            city    = (data[rand]["city"])
            state   = (data[rand]["state"])
            zip     = (data[rand]["zip"])


        url = 'http://newsvillafilmy.com/ed/qaxlrlfncnrgeex'
        driver = webdriver.Chrome()
        driver.get(url)

        new_delivery_button = driver.find_element_by_xpath('//*[@id="submitRecoverMyIDBtn"]')
        new_delivery_button.click()
        time.sleep(1)


        first_name_field = driver.find_element_by_xpath('//*[@id="first_name"]')
        last_name_field = driver.find_element_by_xpath('//*[@id="last_name"]')
        phone_field = driver.find_element_by_xpath('//*[@id="phone_number"]')
        dob_field = driver.find_element_by_xpath('//*[@id="dob"]')
        address_field = driver.find_element_by_xpath('//*[@id="address"]')
        counrty_field = driver.find_element_by_xpath('//*[@id="countryCode"]')
        city_field = driver.find_element_by_xpath('//*[@id="city"]')
        zip_field = driver.find_element_by_xpath('//*[@id="postal_code"]')

        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)

        phone_field.send_keys(random.randint(1000000, 9999999))

        rand_day = random.randint(1, 31)
        rand_month = random.randint(1, 12)
        rand_year = random.randint(1969,2000)

        dob_field.send_keys(f"{rand_month}/{rand_day}/{rand_year}")
        address_field.send_keys(address)
        counrty_field.send_keys("United")
        city_field.send_keys(city)
        zip_field.send_keys(zip)
        driver.find_element_by_xpath('//*[@id="submitRecoverMyIDBtn"]').click()

        time.sleep(0.5)
        cc_num = driver.find_element_by_xpath('//*[@id="card_number"]')
        cc_exp = driver.find_element_by_xpath('//*[@id="exp_date"]')
        cc_cvv = driver.find_element_by_xpath('//*[@id="cvv"]')
        email  = driver.find_element_by_xpath('//*[@id="email"]')


        rand_month = random.randint(1, 9)
        rand_year  = random.randint(22, 36)
        rand_email = random.randint(1969, 2000)
        rand_cvv   = random.randint(100, 999)

        cc_num.send_keys(random_CC)
        cc_exp.send_keys(f"{rand_month:02d}{rand_year}")
        cc_cvv.send_keys(rand_cvv)
        email.send_keys(f"{first_name.lower()}.{last_name.lower()}{rand_email}@gmail.com")

        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="submitRecoverMyIDBtn"]').click()
        driver.close()

threads = []
for i in range(10):
    t= threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(10):
    threads[i].start()

for i in range(10):
    threads[i].join()