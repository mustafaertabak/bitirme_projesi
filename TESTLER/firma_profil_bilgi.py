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
        time.sleep(2)

        self.driver.get(self.url2)
        time.sleep(2)
        self.driver.find_element_by_id("show_info").click()

        self.degerler = dizi

        self.b_isim = self.driver.find_element_by_id(self.degerler["bilgiler_isim"])
        self.b_gad = self.driver.find_element_by_id(self.degerler["bilgiler_giris_adi"])
        self.b_gbtn = self.driver.find_element_by_id(self.degerler["bilgiler_btn"])
        self.b_text = self.driver.find_element_by_id(self.degerler["bilgiler_text"])
                                            
    def basarisiz(self, frm_adi, frm_kadi, bilgi_text):
        for i in range (len(frm_adi)):
            self.b_isim.clear()
            self.b_gad.clear()
            self.b_text.clear()

            self.b_text.send_keys(bilgi_text[i])
            self.b_isim.send_keys(frm_adi[i])
            self.b_gad.send_keys(frm_kadi[i])
            self.b_gbtn.click()
            time.sleep(1.5)
            self.bilgi_btn = self.driver.find_element_by_class_name("btn-success").is_displayed()

            if self.bilgi_btn == False:
                dtm = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/log-firma-profil-bilgi.txt", "a") as file:
                    file.write(" " + "\n")
                    file.write(str(dtm))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Firma Profil sayfasının Bilgi Düzenle alanının BAŞARISIZ testi!")
                    file.write(" " + "\n")
                    file.write("Beklenen Sonuç: Başarısız!")
                    file.write(" " + "\n")
                    file.write("Alınan Sonuç: BAŞARISIZ!")
                    file.write(" " + "\n\n")
                    file.write("TEST BAŞARILI!")
                cprint(Fore.RED, "BAŞARISIZ!")

            else:
                cprint(Fore.GREEN, "BAŞARILI!")
        
    def basarili(self, frm_adi, frm_kadi, bilgi_text):
        db = MySQLdb.connect(host= "127.0.0.1", user = "root", passwd = "", db= "deustaj", use_unicode=True, charset="utf8")
        cursor = db.cursor()

        for i in range (len(frm_adi)):
            self.b_isim.clear()
            self.b_gad.clear()
            self.b_text.clear()

            self.b_text.send_keys(bilgi_text[i])
            self.b_isim.send_keys(frm_adi[i])
            self.b_gad.send_keys(frm_kadi[i])
            self.b_gbtn.click()
            time.sleep(1.5)

            self.bilgi_btn = self.driver.find_element_by_class_name("btn-success").click()
            time.sleep(2)
            cursor.execute("SELECT * FROM firmalar WHERE firma_isim = '%s' AND firma_giris_adi = '%s' AND firma_aciklama = '%s'" % (frm_adi[i], frm_kadi[i],bilgi_text[i]))

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
                    file.write("TEST BAŞARILI!")
                cprint(Fore.GREEN, "Basarili")
            else:                
                cprint(Fore.RED, "Basarisiz")
                time.sleep(0.5)

driver = webdriver.Chrome("C:\\Users\\BERKE\\Downloads\\chromedriver.exe")

print(Fore.CYAN + "Kullanıcı adı girin")
kullanici_adi = input()
print(Fore.CYAN + "Sifre Girin")
sifre = input()

firma_bilgi = firma_bilgi(driver, "http://localhost:100/firma-giris", "http://localhost:100/profil", {"bilgiler_isim": "bilgiler_isim", "bilgiler_giris_adi": "bilgiler_giris_adi", "bilgiler_btn": "bilgiler_btn", "bilgiler_text": "bilgiler_text"}, kullanici_adi, sifre)

print(Fore.YELLOW + "Başarısız test içi 1, başarılı test için 2")
test = int(input())

print(" ")

if test == 1:
    print(Fore.YELLOW + "Çalıştırılan test: " + "firma_bilgi, basarisiz_test", end="\n\n")  
    firma_bilgi.basarisiz(["", ""], ["", ""], ["", ""])


elif test == 2:
    print(Fore.YELLOW + "Çalıştırılan test: " + "firma_bilgi, basarili_test")
    firma_bilgi.basarili(["testdeneme"], ["denemekullanıcıadı"], ["aciklama"])
    print("")
    






