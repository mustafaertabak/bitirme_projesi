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

colorama.init()
def cprint(color, text):
    print(color + text)

class firma_bilgi:

    def __init__(self, driver, url, url2, dizi, k_ad, k_sfr):
       
        self.driver = driver
        self.url = url
        self.url2 = url2
        self.driver.get(self.url)

        self.u_name = self.driver.find_element_by_id("username")
        self.u_pass = self.driver.find_element_by_id("pass")
        self.bttn = self.driver.find_element_by_id("submit_button")

        self.u_name.send_keys(k_ad)
        self.u_pass.send_keys(k_sfr)
        self.bttn.click()
        time.sleep(1.5)
        self.driver.get(self.url2)
        self.driver.find_element_by_id("info_show").click()

        self.degerler = dizi

        self.b_isim = self.driver.find_element_by_id(self.degerler["bilgiler_isim"])
        self.b_gad = self.driver.find_element_by_id(self.degerler["bilgiler_giris_adi"])
        self.b_gbtn = self.driver.find_element_by_id(self.degerler["bilgiler_btn"])

    def basarisiz(self, frm_adi, frm_kadi):
        for i in range (len(frm_adi)):
            self.b_isim.clear()
            self.b_gad.clear()

            self.b_isim.send_keys(frm_adi[i])
            self.b_gad.send_keys(frm_kadi[i])
            self.b_gbtn.click()
            time.sleep(1.5)
            self.show  = self.driver.find_element_by_id(self.degerler["bilgiler_btn"]).is_displayed()

            if self.show == True:
                dtm = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/log-firma-profil-bilgi.txt", "a") as file:
                    file.write(" " + "\n")
                    file.write(str(dtm))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Firma Profil sayfasının Bilgi Düzenle alanının BAŞARISIZ testi!")
                    file.write(" " + "\n")
                    file.write("Beklenen Sonuç: Başarısız!")
                    file.write(" " + "\n")
                    file.write("Alının Sonuç: BAŞARISIZ!")
                    file.write(" " + "\n\n")
                cprint(Fore.RED, "BAŞARISIZ!")
            else:
                cprint(Fore.GREEN, "BAŞARILI!")
        
    def basarili(self, frm_adi, frm_kadi):
        db = MySQLdb.connect(host= "127.0.0.1", user = "root", passwd = "", db= "deustaj")
        cursor = db.cursor()

        for i in range (len(frm_adi)):
            self.b_isim.clear()
            self.b_gad.clear()

            self.b_isim.send_keys(frm_adi[i])
            self.b_gad.send_keys(frm_kadi[i])
            self.b_gbtn.click()
            time.sleep(1.5)

            self.bilgi_btn = self.driver.find_element_by_class_name("btn-success").click()
            time.sleep(2)
            cursor.execute("SELECT * FROM firmalar WHERE firma_isim = '%s' and firma_giris_adi = '%s'" % (frm_adi[i], frm_kadi[i]))

            if cursor.rowcount > 0:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/log-firma-profil-bilgi.txt", "a") as file:
                    file.write(" " + "\n")
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarılı bilgi testi")
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: Başarılı")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: Başarılı")
                    file.write(" " + "\n\n")
                cprint(Fore.GREEN, "Basarili")
            else:                
                cprint(Fore.RED, "Basarisiz")
                time.sleep(0.5)

driver = webdriver.Chrome()

print(Fore.CYAN + "Kullanıcı adı girin")
kullanici_adi = input()
print(Fore.CYAN + "Sifre Girin")
sifre = input()

firma_bilgi = firma_bilgi(driver, "http://localhost/firma-giris", "http://localhost/profil", {"isim": "b_isim", "gad": "b_gad", "btn": "b_gbtn"}, kullanici_adi, sifre)

print(Fore.YELLOW + "Başarısız test içi 1, başarılı test için 2")
test = int(input())

print(" ")

if test == 1:
    print(Fore.YELLOW + "Çalıştırılan test: " + "firma_bilgi, basarisiz_test", end="\n\n")  
    firma_bilgi.basarisiz(["",""], ["",""])


elif test == 2:
    print(Fore.YELLOW + "Çalıştırılan test: " + "firma_bilgi, basarili_test")
    firma_bilgi.basarili(["testdeneme"], ["denemekullanıcıadı"])
    print("")
    






