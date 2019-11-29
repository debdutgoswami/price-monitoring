import urllib.error, urllib.parse, urllib.request
from bs4 import BeautifulSoup

import certificate

class Flipkart:

    def findPrice(self, url, new_price):
        # adding headers so that we don't get blocked by the website
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        # for handling https certificates
        ctx = certificate.context_ssl()
        try:
            html = urllib.request.urlopen(req, context=ctx).read()
        except:
            print("check the link or check your internet connection")
        # parsings html to BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')

        nametag = soup.find('span', attrs={'class':"_35KyD6"}).text
        pricetag = float(soup.find('div', attrs={'class': "_1vC4OE _3qQ9m1"}).text[1:].replace(',',''))

        if new_price.price == None:
            new_price.name = nametag
            new_price.price = pricetag
            print(new_price.name,new_price.price)
        elif new_price.price > pricetag:
            new_price.name = nametag.text
            new_price.price = pricetag
            print(new_price.name,new_price.price)

class Amazon:

    def findPrice(self, url, new_price):
        #TODO

        return