from bs4 import BeautifulSoup
import requests
from crediantials import *
import smtplib


BUY_PRICE  = float (5250)



URL = "https://www.amazon.in/Seagate-Expansion-1TB-External-HDD/dp/B08ZJDWTJ1/ref=sr_1_5?crid=30C2YEWGTE3U5&dib=eyJ2IjoiMSJ9.FwxPqQLt8BZsUKHQGp5Gkh5zfeywDsGlTOA5FfC-zkBuobkH_E8OpmUsrp_Ij4ugJHATFyFJRCnj7ktvr3W8PRpryZZztvD_dFIhXYvgP0WbJpA518FXna1ruKSe4plvNvZAJnEaRau55NQH6lOG_rRPBI9IVDX_lYEUpVrSYJfgDuKHlyWtY7iHJ4YrlgxnbBsaBZQbhWBjgTNdIVR6pOSkuzFxJnZ8GswrZUB83-4.ylCCqjZ_9EYWjGailmMlhMnkg-1fHbsxIYJs5R38te0&dib_tag=se&keywords=ssd%2Bexternal%2B1tb&qid=1738901939&sprefix=ssd%2Caps%2C259&sr=8-5&th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(url=URL , headers= headers )

soup = BeautifulSoup(response.content , "html.parser" )

price = soup.find(class_="a-offscreen").get_text()
# print(price)


only_price = (price.split("₹")[1])

# since in Indian price comma is present so you cannot convert directly string to float
# you would face this error ::: ValueError: could not convert string to float: '5,249.00'
# So just replace comma with this ""

float_price = float(price.split("₹")[1].replace(",", "").strip())
# print(float_price)




# MAILing part


title = soup.find(id = "productTitle").get_text().strip()
print(title)


if float_price < BUY_PRICE :
    message = f"Bhai, teri SSD abhi sasti mil rahi hai! Le lena warna baad mein Mahenga padega. 😜"



    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(user = EMAIL_ADDRESS  , password= EMAIL_PASSWORD )
        connection.sendmail(from_addr=EMAIL_ADDRESS ,
                            to_addrs= EMAIL_ADDRESS ,
                            msg=f"Subject:'Sale aa gayi re, sale aa gayi! 🛍🔥!!!'\n\n{message}\n{URL}".encode("utf-8")
                            )


