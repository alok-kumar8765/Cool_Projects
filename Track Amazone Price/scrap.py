import requests 
from bs4 import BeautifulSoup
import os
import smtplib
from email.message import EmailMessage

email_id = ""
email_pass = ""
url = "https://www.amazon.in/Samsung-Storage-6000mAh-Purchased-Separately/dp/B09TWDYSWQ?pf_rd_r=C27NR3DMSSCRGG5T86PW&pf_rd_p=6572e500-f915-47c7-a3e8-f7fbe4e90c61&pd_rd_r=0b83277a-f99c-4fce-b8ab-88477acd4cec&pd_rd_w=446Fl&pd_rd_wg=HtYQ5&ref_=pd_gw_unk"

def check_price():
# type "my user agent" in browser you get it
    headers = {"user-Agents" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')

    title = soup.find(class_ ="a-size-large product-title-word-break").get_text()
    price = soup.find(class_ = 'a-price aok-align-center reinventPricePriceToPayMargin priceToPay"').get_text()
    conver_price = int(price[2:8].replace(",",""))
    print(title.strip())
    print(conver_price)

    if conver_price < 15000:
        send_mail()

def send_mail():
    msg = EmailMessage()
    msg['Subject'] = 'Product price fell down'
    msg['From'] = email_id
    msg['To'] = 'alok.kaushal@techqware.com'
    msg.set_content('Hey check this amazone link : {url}')

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(email_id,email_pass)
        smtp.send_message(msg)
check_price()