#importing
import requests
from bs4 import BeautifulSoup
import csv
import mysql.connector as mysql

url='https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
page=requests.get(url,headers=headers)
soup=BeautifulSoup(page.content,"html.parser")
products=soup.find_all('div',class_='_13oc-S')

#Initializing csv file
csv_headers=['name','price','rating','summary']
with open("flipkart.csv",'w',encoding='utf-8',newline='')as f:
    writer=csv.writer(f)
    writer.writerow(csv_headers)
#ini mysql
mydb = mysql.connect(
    host="localhost",
    user="root",
    password="admin",
    database="flipkart")
mycursor=mydb.cursor()


for product in products:
    name=product.find("div",class_="_4rR01T").text.strip()
    price=product.find('div',class_='_30jeq3 _1_WHN1').text.strip()
    rating=product.find('div',class_='_3LWZlK').text.strip()
    summary=product.find('div',class_='fMghEO').text.strip()
#Inserting data
    with open("flipkart.csv",'a',encoding='utf-8',newline='')as f:
        writer=csv.writer(f)
        writer.writerow([name,price,rating,summary])
#Inserting data into MySql 

    sql="INSERT INTO flipkart_table Values(%s,%s,%s,%s)"
    val=(name,price,rating,summary)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Records Inserting in MySQL.....")
print("Done")

    

    


    
    
