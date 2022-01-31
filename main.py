import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time
import sys
import smtplib
from email.message import EmailMessage
from datetime import datetime

import sys
from termcolor import colored, cprint

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    user = "freestaiilah@gmail.com"
    msg['from'] = user
    password = "ispyfdqsaoxfxdcp"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

def LDLC():
    ua = UserAgent()
    opts = Options()
    opts.add_argument("user-agent=" + ua.random)
    opts.add_argument('headless')
    driver = webdriver.Chrome(options=opts)
    driver.get("https://www.ldlc.com/es-es/informatica/perifericos-pc/gafas-de-realidad-virtual/c7460/")

    html = driver.page_source
    soup = bs4.BeautifulSoup(html, "html.parser")

    item_in_store = soup.find_all("div", {"class": "modal-stock-web pointer stock stock-9"})
    in_stock = []


    for product in item_in_store:
        if "Agotado" in str(product):
            in_stock.append('Hay Stock')

    if len(in_stock) < 2:
        email_alert("LDLC: Ha vuelto el stock", "¡Buenas! Ya puedes entrar en la página. ¡Date prisa!","harveystockmanalerts@gmail.com")
        print("email enviado, STOCK EN LDLC")
        return("LDLC: EN STOCK")
    return("LDLC: SIN STOCK")

def ECI():
    ua = UserAgent()
    opts = Options()
    opts.add_argument("user-agent="+ua.random)
    opts.add_argument('headless')
    driver = webdriver.Chrome(options=opts)
    driver.get("https://www.elcorteingles.es/videojuegos/ps5/consolas/")

    html = driver.page_source
    soup = bs4.BeautifulSoup(html,"html.parser")

    item_in_store = soup.find_all("span", {"class":"tooltip"})

    in_stock = []

    for product in item_in_store:
        if("Añadir a la cesta" in product.text):
            in_stock.append(product.find_parent("a")["href"])
            #email_alert("Importante, ha vuelto el stock", "¡Buenas!Ya puedes entrar en la página. ¡Date prisa!", "joan.comadran2@gmail.com")
    base_url = "https://elcorteingles.es"

    if len(in_stock)>0:
        email_alert("Importante, ha vuelto el stock", "¡Buenas! Ya puedes entrar en la página. ¡Date prisa!", "harveystockmanalerts@gmail.com")
        print("email enviado, STOCK EN EL CORTE INGLES")
        return ('EL CORTE INGLES: EN STOCK')
    return ('EL CORTE INGLÉS: SIN STOCK')

    for url in in_stock:
        url = base_url + url
        print(url)

def xtralife1():
    ua = UserAgent()
    opts = Options()
    opts.add_argument("user-agent=" + ua.random)
    opts.add_argument('headless')
    driver = webdriver.Chrome(options=opts)
    driver.get("https://www.xtralife.com/producto/ps5-starter-pack-17-ps5-starter-pack-17/69718")

    html = driver.page_source
    soup = bs4.BeautifulSoup(html, "html.parser")

    item_in_store = soup.find_all("p", {"class": "actionText colorWhite fontBold fontNormal"})
    if "Reservar ahora" in str(item_in_store):
        email_alert("XTRALIFE: RESERVAR PACK 17", "¡Buenas! Ya puedes entrar en la página. ¡Date prisa!","harveystockmanalerts@gmail.com")
        print("email enviado, STOCK EN XTRALIFE PACK 17")
        return("XTRALIFE PACK 17: EN STOCK")
    return("XTRALIFE PACK 17: SIN STOCK")

def xtralife2():
    ua = UserAgent()
    opts = Options()
    opts.add_argument("user-agent=" + ua.random)
    opts.add_argument('headless')
    driver = webdriver.Chrome(options=opts)
    driver.get("https://www.xtralife.com/producto/ps5-starter-pack-21-ps5-starter-pack-21/69722")

    html = driver.page_source
    soup = bs4.BeautifulSoup(html, "html.parser")

    item_in_store = soup.find_all("p", {"class": "actionText colorWhite fontBold fontNormal"})
    if "Reservar ahora" in str(item_in_store):
        email_alert("XTRALIFE: RESERVAR PACK 21", "¡Buenas! Ya puedes entrar en la página. ¡Date prisa!","harveystockmanalerts@gmail.com")
        print("email enviado, STOCK EN XTRALIFE PACK 21")
        return("XTRALIFE PACK 21: EN STOCK")
    return ("XTRALIFE PACK 21: SIN STOCK")

while True:

    driver = webdriver.Chrome()
    driver.get("https://www.elcorteingles.es/videojuegos/ps5/consolas/")

    html = driver.page_source
    soup = bs4.BeautifulSoup(html,"html.parser")

    item_in_store = soup.find_all("span", {"class":"tooltip"})

    in_stock = []

    for product in item_in_store:
        if("Añadir a la cesta" in product.text):
            in_stock.append(product.find_parent("a")["href"])

    base_url = "https://elcorteingles.es"

    for url in in_stock:
        url = base_url + url
        print(url)

    time.sleep(10)
    print("Scraping finished")


