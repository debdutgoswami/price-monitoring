from products import Product
from scraper import *
import certificate, time


new_price = Product()
n = int(input("1. Amazon\n2. Flipkart\nenter your choice: "))

url = input("enter the url of the product you want to track -\n")

if n == 1:
    while(True):
        Amazon().findPrice(url,new_price)
        time.sleep(600)
elif n == 2:
    while(True):
        Flipkart().findPrice(url,new_price)
        time.sleep(600)