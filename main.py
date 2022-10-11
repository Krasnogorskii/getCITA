import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import requests
import telebot

token = "your_telegram_bot_token"
tb = telebot.TeleBot(token)
#browser = webdriver.Firefox(executable_path='/Users/nick/PycharmProjects/alicante/Drivers/geckodriver')
browser = webdriver.Chrome('/Users/nick/PycharmProjects/alicante/Drivers/chromedriver')


def cookie():
    browser.get('https://icp.administracionelectronica.gob.es/icpplus/index.html')
    time.sleep(5)
    # get cookie
    try:
        c = browser.find_element_by_id("cookie_action_close_header")
        c.click()
        rep()
    except:
        tb.send_message(109837290, 'error')
        time.sleep(500)
        return rep()

res = 'null'
def rep():
    r = 1
    while res == 'null':
        if r % 5 == 0:
            tb.send_message(109837290, '+5')
            time.sleep(0)
            r += 1
        else:
            r += 1
            print(r)
            getcita()

def getcita():
    browser.get('https://icp.administracionelectronica.gob.es/icpplus/index.html')
    # choose region
    time.sleep(5)
    try:
        m = browser.find_element_by_css_selector('[id="form"]')
        Select(m).select_by_visible_text('Alicante')
        time.sleep(5)
    except:
        tb.send_message(109837290, 'error')
        time.sleep(300)
        return rep()
    # press button
    try:
        q = browser.find_element_by_id("btnAceptar")
        q.click()
        time.sleep(5)
    except:
        tb.send_message(109837290, 'error')
        time.sleep(300)
        return rep()
    # choose place
    # CNP Denia, Avda Marquesado, 53

    try:
        w = browser.find_element_by_css_selector('[id="sede"]')
        multi1 = Select(w)
        multi1.select_by_visible_text('CNP Denia, Avda Marquesado, 53')
        time.sleep(2)
    except:
        tb.send_message(109837290, 'error')
        time.sleep(300)
        return rep()
    # choose service
    # Asignación de N.I.E.
    try:
        e = browser.find_element_by_css_selector('[id="tramiteGrupo[0]"]')
        multi2 = Select(e)
        multi2.select_by_visible_text('Asignación de N.I.E.')
        time.sleep(2)
    except:
        tb.send_message(109837290, 'error')
        time.sleep(300)
        return rep()
    # press button
    try:
        t = browser.find_element_by_id("btnAceptar")
        t.click()
        time.sleep(2)
    except:
        tb.send_message(109837290, 'error')
        time.sleep(300)
        return rep()
    # down page
    browser.find_element_by_tag_name('body').send_keys(Keys.END)
    # press button
    time.sleep(2)
    try:
        browser.find_element_by_id("btnEntrar").click()
    except:
        tb.send_message(109837290, 'error')
        time.sleep(300)
        return rep()
    # passport
    # 753718478
    try:
        y = browser.find_element_by_id("txtIdCitado")
        time.sleep(2)
        y.send_keys('753718478')
    except:
        tb.send_message(109837290, 'error')
        time.sleep(300)
        return rep()
    # page down
    browser.find_element_by_tag_name('body').send_keys(Keys.END)
    # Last name, first name
    time.sleep(2)
    browser.find_element_by_id("txtDesCitado").send_keys('EKATERINA KRASNOGORSKAIA')
    # birth year
    time.sleep(2)
    browser.find_element_by_id("txtAnnoCitado").send_keys('1989')
    # native country
    multi3 = Select(browser.find_element_by_css_selector('[id="txtPaisNac"]'))
    multi3.select_by_visible_text('RUSIA')
    # press button
    browser.find_element_by_id("btnEnviar").click()
    # press button
    time.sleep(2)
    try:
        u = browser.find_element_by_id("btnEnviar")
        u.click()
        time.sleep(2)
    except:
        tb.send_message(109837290, 'error')
        time.sleep(300)
        return rep()
    # take result
    try:
        t = browser.find_element_by_class_name('mf-msg__info')
        result = t.text
        # tb.send_message(109837290, 'ok')
    except:
        tb.send_message(109837290, 'alarm')
        time.sleep(10000)
    browser.find_element_by_id("btnSalir").click()
cookie()
rep()
tb.infinity_poling()
