from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import sleep
from random import randint

 
def Scraper(count):
    my_url = 'https://www.newegg.com/p/pl?d=gpu&N=100007709&isdeptsrh=1&page='+str(count)

    # makes the file
    f = open(file, "a");

    # grabs the URL
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    # html parsing
    page_soup = soup(page_html, 'html.parser')
    
    # grabs each products
    containers = page_soup.findAll("div", {"class": "item-container"})

    
    for section in containers[3:]:
        if ("3060" in soup.get_text(section.find('a', {'class': "item-title"})) or "3070" in soup.get_text(section.find('a', {'class': "item-title"})) or"3060" in soup.get_text(section.find('a', {'class': "item-title"}))):
            if (section.a.next_sibling.a.img in section.a.next_sibling.a):
                brand = section.a.next_sibling.a.img['title']
            else:
                brand = 'N/A'
            shipping = soup.get_text(section.find('li', {'class':'price-ship'}))
            card_name = soup.get_text(section.find('a', {'class': "item-title"}));
            was_price = soup.get_text(section.find('li', {'class': 'price-was'}))
            is_price = soup.get_text(section.find('li', {'class': 'price-current'}))
            if (was_price != True):
                was_price=is_price;
            print('\n\n Brand is:',brand, '\n name is:', card_name, '\n price was:', was_price, '\n Price is:', is_price, '\n Shipping cost:', shipping, '\n \n')
            f.write(str(brand).replace(",","")+','+str(card_name).replace(",","|")+','+str(was_price).replace(",","")+','+str(is_price).replace(",","")+','+shipping+ "\n")
        else:
            print('Not the one!')
    
 
def Iterator(count):
    while count != 100:
        Scraper(count);
        count+=1
        sleep(randint(1,4))

file = "Gpu.csv";
f = open(file, "w");
headers = "Brand, Product_Name, Original_Price, Current_Price, Shipping\n"
f.write(headers)
Iterator(1)
f.close();