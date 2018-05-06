# Bu kısımda gerekli importları yaptık
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import MySQLdb

import colorama 
from colorama import Fore, Back, Style

import datetime 
import time

# Textlerden renkli çıktı alabilmek için coloromayı init edip fonksiyon içinde tanımladık
colorama.init()
def cprint(color, text):
    print(color + text)

class Firma_logo:
    
    def __init__(self, driver, url, profil):

        self.driver = driver
        self.url_profil = profil
        self.url = url
        self.driver.get(self.url)
        self.k_ad = self.driver.find_element_by_id("username")
        self.k_sif = self.driver.find_element_by_id("pass")
        self.giris_btn = self.driver.find_element_by_id("submit_button")

        self.k_ad.send_keys("7040000001")
        self.k_sif.send_keys("123456")
        self.giris_btn.click()
        self.driver.get(self.url_profil)
        time.sleep(1.5) 
        self.firma_adi = self.driver.find_element_by_id("firma_adi").click()
        self.txt = self.driver.find_element_by_class_name("bilgi_val").text
        

    def firma_pp(self):
        db = MySQLdb.connect(host= "127.0.0.1", user = "root", passwd = "", db= "deustaj", use_unicode=True, charset="utf8")
        cursor = db.cursor()

        self.img_btn = self.driver.find_element_by_id("img-input")
        self.img_btn.send_keys("C:\\xampp\\htdocs\\assets\\img\\fl_0c35d3e.png")
        time.sleep(2)

        self.img_name = self.driver.find_element_by_id("img-name").text
        self.driver.find_element_by_id("up-btn").click()
       
        time.sleep(1.5)

        self.driver.find_element_by_class_name("btn-success").click()
        time.sleep(3)
        db.commit()
       
        cursor.execute("SELECT * FROM firmalar WHERE firma_logo = '%s'" % (self.img_name))
        if cursor:
            dtm = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("LOGS/firma-pp.txt", "a") as file:
                file.write(" " + "\n")
                file.write(str(dtm))
                file.write(" " + "\n")
                file.write("Yapılan test: Firma Profil Upload Foto  BAŞARILI testi!")
                file.write(" " + "\n")
                file.write("Firmanın Adı : " + self.txt)
                file.write(" " + "\n")
                file.write("Upload Edilen Img: " + self.img_name)
                file.write(" " + "\n")
                file.write("Beklenen Sonuç: İŞLEM BAŞARILI!")
                file.write(" " + "\n")
                file.write("Alınan Sonuç: İŞLEM BAŞARILI!")
                file.write(" " + "\n\n")
                file.write("TEST BAŞARILI!")
                file.write(" " + "\n\n")
            cprint(Fore.LIGHTBLUE_EX, "Test Çalıştırılma Tarih/Saat'i : " + str(dtm))
            print("")       
            cprint(Fore.LIGHTBLUE_EX, "Firmanın Adı : " + self.txt)
            cprint(Fore.LIGHTBLUE_EX, "Upload Edilen Img : " + self.img_name)

            print("")
            cprint(Fore.YELLOW, "Beklenen Sonuç = İŞLEM BAŞARILI!")
            print("")
            cprint(Fore.GREEN, "Alınan Sonuç = İŞLEM BAŞARILI!")  
            print("")
            cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARILI!")
            print("\n") 
            time.sleep(1)

        else:
            dtm = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("LOGS/firma-pp.txt", "a") as file:
                file.write(" " + "\n")
                file.write(str(dtm))
                file.write(" " + "\n")
                file.write("Yapılan test: Firma Profil Upload Foto  BAŞARILI testi!")
                file.write(" " + "\n")
                file.write("Firmanın Adı : " + self.txt)
                file.write(" " + "\n")
                file.write("Upload Edilen Img: " + self.img_name)
                file.write(" " + "\n")
                file.write("Beklenen Sonuç: İŞLEM BAŞARILI!")
                file.write(" " + "\n")
                file.write("Alınan Sonuç: İŞLEM BAŞARISIZ!")
                file.write(" " + "\n\n")
                file.write("TEST BAŞARISIZ!")
                file.write(" " + "\n\n")
            cprint(Fore.LIGHTBLUE_EX, "Test Çalıştırılma Tarih/Saat'i : " + str(dtm))
            print("")       
            cprint(Fore.LIGHTBLUE_EX, "Firmanın Adı : " + self.txt)
            cprint(Fore.LIGHTBLUE_EX, "Upload Edilen Img : " + self.img_name)

            print("")
            cprint(Fore.YELLOW, "Beklenen Sonuç = İŞLEM BAŞARILI!")
            print("")
            cprint(Fore.GREEN, "Alınan Sonuç = BAŞARISIZ!")  
            print("")
            cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARISIZ!")
            print("\n") 
            time.sleep(1)

driver = webdriver.Chrome("C:\\xampp\\chromedriver.exe")

Firma_logo = Firma_logo(driver, "http://localhost:100/admin", "http://localhost:100/firmalar")

Firma_logo.firma_pp()