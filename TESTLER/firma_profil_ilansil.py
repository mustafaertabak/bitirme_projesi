# Bu kısımda gerekli importları yaptık
from selenium import webdriver
import MySQLdb
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


import colorama 
from colorama import Fore, Back, Style

import datetime 
import time

# Textlerden renkli çıktı alabilmek için coloromayı init edip fonksiyon içinde tanımladık
colorama.init()
def cprint(color, text):
    print(color + text)

class ilan_sil:

    def __init__(self, driver, url, url2, k_ad, k_sfr):
        self.driver = driver
        self.url = url
        self.url2 = url2
        self.driver.get(self.url)

        self.u_name = self.driver.find_element_by_id("username")
        self.u_pass = self.driver.find_element_by_id("pass")
        self.u_btn = self.driver.find_element_by_id("submit_button")

        self.u_name.send_keys(k_ad)
        self.u_pass.send_keys(k_sfr)
        self.u_btn.click()
        time.sleep(1.5)

        self.driver.get(self.url2)
    
    def test(self):
        db = MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "", db = "deustaj", use_unicode=True, charset="utf8")
        cursor = db.cursor()

        self.driver.find_element_by_id("ilanlarim").click()
        self.id = self.driver.find_element_by_id("ilan_sil")
        self.att_id = self.id.get_attribute("data-delid")
        
        self.id.click()
        self.driver.find_element_by_class_name("btn-success").click()
        db.commit()
        time.sleep(1.5)

        self.crsr = cursor.execute("SELECT ilan_id FROM ilanlar WHERE ilan_id='%s'" % (self.att_id))
        
        if self.crsr == False:
            d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("LOGS/firma-profil-ilansil.txt", "a") as file:
                file.write(" " + "\n")   
                file.write(str(d))
                file.write(" " + "\n")
                file.write("Yapılan test: Başarılı şifre testi")
                file.write(" " + "\n")
                file.write("Beklenen sonuç: Başarılı")
                file.write(" " + "\n")
                file.write("Alınan sonuç: Başarılı")
                file.write(" " + "\n\n")
            cprint(Fore.GREEN, "Basarili")
        else:
            cprint(Fore.RED, "Basarisiz")

driver = webdriver.Chrome("C:\\xampp\\chromedriver.exe")

print(Fore.CYAN, "Kullanıcı Adı Giriniz")
kullanici_adi = input()
print(Fore.CYAN + "Sifre gir")
sifre = input()
   
firma_ilansil = ilan_sil(driver, "http://localhost/firma-giris", "http://localhost/profil", kullanici_adi, sifre)

firma_ilansil.test()

