# Gerekli importları bu kısımda yapıyoruz 
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

class ogrenci_bilgi:

    def __init__(self, driver, url, url2, dizi, k_ad, k_sif):
        
        self.driver = driver
        self.url = url
        self.url_2 = url2
        self.driver.get(self.url)

        self.k_id = self.driver.find_element_by_id("username")
        self.k_pas = self.driver.find_element_by_id("pass")
        self.btn = self.driver.find_element_by_id("submit_button")

        
        self.k_id.send_keys(k_ad)
        self.k_pas.send_keys(k_sif)
        self.btn.click()
        time.sleep(1.5)
        self.driver.get(self.url_2)
        self.driver.find_element_by_id("show_info").click()
        
        self.degerler = dizi 

        self.mail = self.driver.find_element_by_id(self.degerler["mail_bilgi"])
        self.tel = self.driver.find_element_by_id(self.degerler["tel"])
        self.g_btn = self.driver.find_element_by_id(self.degerler["btn"])

    def basarisiz(self, mail, tel):
        for i in range (len(mail)):      
            self.mail.clear()
            self.tel.clear()

            self.mail.send_keys(mail[i])
            self.tel.send_keys(tel[i])
            self.g_btn.click()
            time.sleep(1)
            self.show = self.driver.find_element_by_id(self.degerler["btn"]).is_displayed()

            if self.show == True:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/log-ogr-bilgi.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarısız bilgi testi")
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: Başarısız")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: Başarısız")
                    file.write(" " + "\n\n")
                cprint(Fore.RED, "Basarisiz")
            
            else:
                cprint(Fore.GREEN, "Basarili")
    
    def basarili(self, mail, tel):
        db = MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "", db = "deustaj")
        cursor = db.cursor()

        for i in range (len(mail)):      
            self.mail.clear()
            self.tel.clear()

            self.mail.send_keys(mail[i])
            self.tel.send_keys(tel[i])
            self.g_btn.click()
            time.sleep(1)

            self.acc_btn = self.driver.find_element_by_class_name("btn-success").click()
            time.sleep(2)
            cursor.execute("SELECT * FROM ogr WHERE ogr_mail = '%s' and ogr_cep_no = '%s'" %  (mail[i], tel[i]))

            if cursor.rowcount > 0:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/log-ogr-bilgi.txt", "a") as file:
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

print(Fore.CYAN + "Kullanıcı adı gir") 
kullanici_adi = input()
print(Fore.CYAN + "Sifre gir")
sifre = input()

ogrenci_bilgi = ogrenci_bilgi(driver, "http://localhost:80/ogrenci-giris", "http://localhost:80/profil", {"mail_bilgi": "bilgiler_mail", "tel": "bilgiler_tel", "btn": "bilgiler_btn"}, kullanici_adi, sifre)


print(Fore.YELLOW + "Başarısız test için 1, başarılı test için 2") 
test = int(input())

print(" ")


if test == 1:
    print(Fore.YELLOW + "Çalıştırılan test: " + "ogrenci_bilgi, basarisiz_test", end="\n\n")  
    ogrenci_bilgi.basarisiz(["denemedeneme.com","asdasdsa"], ["56562","454562"])


elif test == 2:
    print(Fore.YELLOW + "Çalıştırılan test: " + "ogrenci_bilgi, basarili_test")
    ogrenci_bilgi.basarili(["deneme@deneme.com"], ["05512020194"])
    print("")
    
    

