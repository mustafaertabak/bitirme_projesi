# Gerekli importları bu kısımda yapıyoruz 
from selenium import webdriver
import MySQLdb
import hashlib
from hashlib import md5
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

class firma_sifre:
    
    def __init__(self, driver, url, url2, dizi, k_ad, k_sif):
        
        self.driver = driver 
        self.url = url 
        self.url_2 = url2 
        self.driver.get(self.url)
        self.k_ad = self.driver.find_element_by_id("username")
        self.k_sif = self.driver.find_element_by_id("pass")
        self.btn = self.driver.find_element_by_id("submit_button")

        self.k_ad.send_keys(k_ad)
        self.k_sif.send_keys(k_sif)
        self.btn.click()
        time.sleep(1.5)
        self.driver.get(self.url_2)
        self.driver.find_element_by_id("sifre_degis").click()

        self.degerler = dizi 

        self.old = self.driver.find_element_by_id(self.degerler["sif_old"])
        self.new = self.driver.find_element_by_id(self.degerler["sif_new"])
        self.new_b = self.driver.find_element_by_id(self.degerler["sif_new_b"])
        self.button = self.driver.find_element_by_id(self.degerler["sif_btn"])

    def basarisiz(self, old, new, new_b):
        for i in range (len(new)):
            self.old.clear()
            self.new.clear()
            self.new_b.clear()

            self.old.send_keys(old[i])
            self.new.send_keys(new[i])
            self.new_b.send_keys(new_b[i])
            self.button.click()
            time.sleep(2)

            self.disp = self.driver.find_element_by_id("sifre_w").is_displayed()
 
            if self.disp == False:
                self.driver.find_element_by_class_name("btn-success").click()
                time.sleep(1.5)
                self.disp = self.driver.find_element_by_id("sifre_w").is_displayed()

                if self.disp:
                    d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    with open("LOGS/firma-sifre.txt", "a") as file:
                        file.write(" " + "\n")   
                        file.write(str(d))
                        file.write(" " + "\n")
                        file.write("Yapılan test: Başarısız şifre testi")
                        file.write(" " + "\n")
                        file.write("Girilen Eski Şifre Değeri : " + old[i])
                        file.write(" " + "\n")
                        file.write("Girilen Yeni Şifre Değeri : " + new[i])
                        file.write(" " + "\n")
                        file.write("Girilen Yeni Şifre Değeri Tekrarı : " + new_b[i])
                        file.write(" " + "\n")
                        file.write("Beklenen sonuç: İŞLEM BAŞARISIIZ!")
                        file.write(" " + "\n") 
                        file.write("Alınan sonuç: İŞLEM BAŞARISIZ!")  
                        file.write(" " + "\n\n")      
                        file.write("TEST BAŞARILI!") 
                        file.write(" " + "\n\n") 
                    cprint(Fore.LIGHTBLUE_EX, "Test Çalıştırılma Tarih/Saati : " + str(d))
                    print("")
                    cprint(Fore.LIGHTMAGENTA_EX, "GİRİŞ - " + str(i+1))   
                    print("")
                    cprint(Fore.LIGHTBLUE_EX, "Girilen Eski Şifre Değeri : " + old[i])
                    cprint(Fore.LIGHTBLUE_EX, "Girilen Yeni Şifre Değeri : " + new[i])
                    cprint(Fore.LIGHTBLUE_EX, "Girilen Yeni Şifre Değeri Tekrarı : " + new_b[i])
                    print("")
                    cprint(Fore.YELLOW, "Beklenen Sonuç = İŞLEM BAŞARISIZ!")
                    print("")
                    cprint(Fore.GREEN, "Alınan Sonuç = İŞLEM BAŞARISIZ!")
                    print("")
                    cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARILI!")
                    print("")
                    time.sleep(0.5)
                else:
                    d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    with open("LOGS/firma-sifre.txt", "a") as file:
                        file.write(" " + "\n")   
                        file.write(str(d))
                        file.write(" " + "\n")
                        file.write("Yapılan test: Başarısız şifre testi")
                        file.write(" " + "\n")
                        file.write("Girilen Eski Şifre Değeri : " + old[i])
                        file.write(" " + "\n")
                        file.write("Girilen Yeni Şifre Değeri : " + new[i])
                        file.write(" " + "\n")
                        file.write("Girilen Yeni Şifre Değeri Tekrarı : " + new_b[i])
                        file.write(" " + "\n")
                        file.write("Beklenen sonuç: İŞLEM BAŞARISIZ!")
                        file.write(" " + "\n") 
                        file.write("Alınan sonuç: İŞLEM BAŞARILI!")  
                        file.write(" " + "\n\n")      
                        file.write("TEST BAŞARISIZ!") 
                        file.write(" " + "\n\n") 
                    cprint(Fore.LIGHTBLUE_EX, "Test Çalıştırılma Tarih/Saati : " + str(d))
                    print("")
                    cprint(Fore.LIGHTMAGENTA_EX, "GİRİŞ - " + str(i+1))   
                    print("")
                    cprint(Fore.LIGHTBLUE_EX, "Girilen Eski Şifre Değeri : " + old[i])
                    cprint(Fore.LIGHTBLUE_EX, "Girilen Yeni Şifre Değeri : " + new[i])
                    cprint(Fore.LIGHTBLUE_EX, "Girilen Yeni Şifre Değeri Tekrarı : " + new_b[i])
                    print("")
                    cprint(Fore.YELLOW, "Beklenen Sonuç = İŞLEM BAŞARISIZ!")
                    print("")
                    cprint(Fore.RED, "Alınan Sonuç = İŞLEM BAŞARILI!")
                    print("")
                    cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARISIZ!")
                    print("")
                    time.sleep(0.5)
            
            else:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/firma-sifre.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarısız şifre testi")
                    file.write(" " + "\n")
                    file.write("Girilen Eski Şifre Değeri : " + old[i])
                    file.write(" " + "\n")
                    file.write("Girilen Yeni Şifre Değeri : " + new[i])
                    file.write(" " + "\n")
                    file.write("Girilen Yeni Şifre Değeri Tekrarı : " + new_b[i])
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: İŞLEM BAŞARISIZ!")
                    file.write(" " + "\n") 
                    file.write("Alınan sonuç: İŞLEM BAŞARISIZ!")  
                    file.write(" " + "\n\n") 
                    file.write("TEST BAŞARILI!")    
                    file.write(" " + "\n\n")         
                cprint(Fore.LIGHTBLUE_EX, "Test Çalıştırılma Tarih/Saat'i : " + str(d))
                print("")
                cprint(Fore.LIGHTMAGENTA_EX, "GİRİŞ - " + str(i+1))   
                print("")
                cprint(Fore.LIGHTBLUE_EX, "Girilen Eski Şifre Değeri : " + old[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Yeni Şifre Değeri : " + new[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Yeni Şifre Değeri Tekrarı : " + new_b[i])
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç = İŞLEM BAŞARISIZ!")
                print("")
                cprint(Fore.GREEN, "Alınan Sonuç = İŞLEM BAŞARISIZ!")
                print("")
                cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARILI!")
                time.sleep(0.5)
        cprint(Fore.YELLOW, "Çıkmak için 'e' başarısız test için 'b' tuşlayın")
        a = input()
        if a == 'e':
            driver.close()
        elif a == 'b':
            self.driver.find_element_by_id("sifre_degis").click()
            time.sleep(1)
            self.old.clear()
            self.new.clear()
            self.new_b.clear()

            self.old = self.driver.find_element_by_id(self.degerler["sif_old"])
            self.new = self.driver.find_element_by_id(self.degerler["sif_new"])
            self.new_b = self.driver.find_element_by_id(self.degerler["sif_new_b"])
            self.button = self.driver.find_element_by_id(self.degerler["sif_btn"])
            time.sleep(2)
            firma_sifre.basarili([sifre])

    
    def basarili(self, old):
        db = MySQLdb.connect(host= "127.0.0.1", user = "root", passwd = "", db= "deustaj", use_unicode=True, charset="utf8")
        cursor = db.cursor()
        
        for i in range (len(old)):
            print("Yeni şifre gir")
            self.sifre = input()
            self.old.send_keys(old[i])
            self.new.send_keys(self.sifre)
            self.new_b.send_keys(self.sifre)     
            self.button.click()

            time.sleep(1)

            self.btn_success = self.driver.find_element_by_class_name("btn-success")
            self.btn_success.click() 
            time.sleep(2)
            
            self.hash_object = hashlib.md5(self.sifre.encode())

            cursor.execute("SELECT * FROM firmalar WHERE firma_sifre = '%s'" % (self.hash_object.hexdigest()))

            if cursor.rowcount > 0:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/firma-sifre.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarılı şifre testi")
                    file.write(" " + "\n")
                    file.write("Girilen Eski Şifre Değeri : " + old[i])
                    file.write(" " + "\n")
                    file.write("Girilen Yeni Şifre Değeri : " + self.sifre)
                    file.write(" " + "\n")
                    file.write("Girilen Yeni Şifre Değeri Tekrarı : " + self.sifre)
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: İŞLEM BAŞARILI!")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: İŞLEM BAŞARILI!")
                    file.write(" " + "\n")
                    file.write("TEST BAŞARILI!")
                    file.write(" " + "\n\n")
                cprint(Fore.LIGHTBLUE_EX, "Test Çalıştırılma Tarih/Saati : " + str(d))
                print("")
                cprint(Fore.LIGHTBLUE_EX, "Girilen Eski Şifre Değeri : " + old[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Yeni Şifre Değeri : " + self.sifre)
                cprint(Fore.LIGHTBLUE_EX, "Girilen Yeni Şifre Değeri Tekrarı : " + self.sifre)
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç = İŞLEM BAŞARILI!")
                print("")
                cprint(Fore.GREEN, "Alınan Sonuç = İŞLEM BAŞARILI!")
                print("")
                cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARILI!")
                print("")
                time.sleep(0.5)

            else:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/firma-sifre.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarılı şifre testi")
                    file.write(" " + "\n")
                    file.write("Girilen Eski Şifre Değeri : " + old[i])
                    file.write(" " + "\n")
                    file.write("Girilen Yeni Şifre Değeri : " + self.sifre)
                    file.write(" " + "\n")
                    file.write("Girilen Yeni Şifre Değeri Tekrarı : " + self.sifre)
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: İŞLEM BAŞARILI!")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: İŞLEM BAŞARISIZ!")
                    file.write(" " + "\n")
                    file.write("TEST BAŞARISIZ!")
                    file.write(" " + "\n\n")
                cprint(Fore.LIGHTBLUE_EX, "Test Çalıştırılma Tarih/Saati : " + str(d))
                print("")
                cprint(Fore.LIGHTBLUE_EX, "Girilen Eski Şifre Değeri : " + old[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Yeni Şifre Değeri : " + self.sifre)
                cprint(Fore.LIGHTBLUE_EX, "Girilen Yeni Şifre Değeri Tekrarı : " + self.sifre)
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç = İŞLEM BAŞARILI!")
                print("")
                cprint(Fore.RED, "Alınan Sonuç = İŞLEM BAŞARISIZ!")
                print("")
                cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARISIZ!")  
                time.sleep(0.5)
        cprint(Fore.YELLOW, "Çıkmak için 'e' başarısız test için 'b' tuşlayın")
        a = input()
        if a == 'e':
            driver.close()
        elif a == 'b':
            self.driver.find_element_by_id("sifre_degis").click()
            time.sleep(1)
            self.old = self.driver.find_element_by_id(self.degerler["sif_old"])
            self.new = self.driver.find_element_by_id(self.degerler["sif_new"])
            self.new_b = self.driver.find_element_by_id(self.degerler["sif_new_b"])
            self.button = self.driver.find_element_by_id(self.degerler["sif_btn"])
            time.sleep(2)
            firma_sifre.basarisiz([sifre,"1234518"], ["123456","232235"], ["123456","232235"])


driver = webdriver.Chrome("C:\\xampp\\chromedriver.exe")

print(Fore.CYAN + "Kullanıcı adı gir") 
kullanici_adi = input()
print(Fore.CYAN + "Sifre gir")
sifre = input()

firma_sifre = firma_sifre(driver, "http://localhost:100/firma-giris", "http://localhost:100/profil", {"sif_old": "old_pass", "sif_new": "new_pass_a", "sif_new_b": "new_pass_b","sif_btn": "sifre_btn"}, kullanici_adi, sifre)

 
print(Fore.YELLOW + "Başarısız test için 1, başarılı test için 2") 
test = int(input())

print(" ")


if test == 1:
    print(Fore.YELLOW + "Çalıştırılan test: " + "firma_sifre, basarisiz_test", end="\n\n")
    # Öğrenci_giris sınıfının içindeki basarisiz define degerleri gönderiyoruz 
    firma_sifre.basarisiz([sifre,"1234518"], ["12345","23235"], ["123456","232235"])


elif test == 2:
    print(Fore.YELLOW + "Çalıştırılan test: " + "firma_sifre, basarili_test")
    firma_sifre.basarili([sifre])
    print("")               
            

