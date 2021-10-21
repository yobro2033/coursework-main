import requests
from bs4 import BeautifulSoup as soup
import json

def Iceland(productInput):
    productInput = productInput
    productURLInput = productInput.replace(" ","%20")
    my_url = 'https://www.iceland.co.uk/search?q=' + productURLInput
    response = requests.get(my_url)
    responseCode = str(response)
    if responseCode == "<Response [200]>":
        try:
            productListFound = soup(response.text, 'html.parser')
            containers = productListFound.findAll("div",{"class":"product-tile"})
            icelandItems = []
            for container in containers:
                productLinkContainer = container.find("div",{"class":"product-image"})
                productLinkItem = productLinkContainer.a["href"]
                productName = productLinkContainer.a["title"]
                productImage = productLinkContainer.a.picture.img["src"]
                price_container = container.find("span",{"class":"product-sales-price"})
                productPrice1 = price_container.text
                productPrice1 = str(productPrice1)
                productPrice2 = productPrice1.replace("\n", "")
                productPrice = productPrice2.replace("£", "")
                unitprice_container = container.find("div",{"class":"product-pricing-info"})
                productUnitPrice1 = unitprice_container.text
                productUnitPrice1 = str(productUnitPrice1)
                productUnitPrice = productPrice1.replace("\n", "")
                row = ['Iceland',productName,productLinkItem,productPrice,productImage,productUnitPrice]
                icelandItems.append(row)
            return icelandItems
        except Exception as e:
            print(e)
            return icelandItems
    else:
        print(responseCode)