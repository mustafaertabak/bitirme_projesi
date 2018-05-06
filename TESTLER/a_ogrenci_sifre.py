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


class ogrenci_sifre:
    

    def __init__(self, driver, url, url2, dizi):
    
        self.driver = driver 
        self.url = url 
        self.url_2 = url2
        self.driver.get(self.url)
        self.k_id = self.driver.find_element_by_id("username")
        self.k_pas = self.driver.find_element_by_id("pass")
        self.btn = self.driver.find_element_by_id("submit_button")

        self.k_id.send_keys("7040000001")
        self.k_pas.send_keys("123456")
        self.btn.click()
        time.sleep(1.5)
        self.driver.get(self.url_2)

        self.driver.find_element_by_id("ogr_ad").click()
        
        time.sleep(1.5)
        self.ogr_no = self.driver.find_element_by_id("ogr_num").text
        self.driver.find_element_by_xpath("//button[@data-content='sifre']").click()
         
        
        self.degerler = dizi 

        self.new = self.driver.find_element_by_id(self.degerler["sif_new"])
        self.new_b = self.driver.find_element_by_id(self.degerler["sif_new_b"])
        self.button = self.driver.find_element_by_id(self.degerler["sifre_btn"])
       
    def basarisiz(self, new, new_b):    
        for i in range (len(new)):
            self.new.clear()
            self.new_b.clear()
            

            self.new.send_keys(new[i])
            self.new_b.send_keys(new_b[i])
            self.button.click()
            time.sleep(2)     

            self.disp = self.driver.find_element_by_id("sifre_w").is_displayed()
            result = None

            if self.disp:
                result = True
            else:
                result = False
          
            if result == False:
                self.driver.find_element_by_class_name("btn-success").click()
                time.sleep(1.5)
                self.disp = self.driver.find_element_by_id("sifre_w").is_displayed()

                if self.disp:
                    d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    with open("LOGS/log-ogrsif.txt", "a") as file:
                        file.write(" " + "\n")   
                        file.write(str(d))
                        file.write(" " + "\n")
                        file.write("Yapılan test: Başarısız şifre testi")
                        file.write(" " + "\n")
                        file.write("Girilen Yeni Şifre Değeri : " + new[i])
                        file.write(" " + "\n")
                        file.write("Girilen Yeni Şifre Değeri Tekrarı : " + new_b[i])
                        file.write(" " + "\n")
                        file.write("Beklenen sonuç: GİRİŞ BAŞARISIZ!")
                        file.write(" " + "\n") 
                        file.write("Alınan sonuç: GİRİŞ BAŞARISIZ!")  
                        file.write(" " + "\n") 
                        file.write("TEST BAŞARILI!")  
                        file.write(" " + "\n\n")   
                    cprint(Fore.LIGHTBLUE_EX, "Test Çalıştırılma Tarih/Saati : " + str(d))
                    print("")
                    cprint(Fore.LIGHTMAGENTA_EX, "Giriş - " + str(i+1))    
                    print("")
                    cprint(Fore.LIGHTBLUE_EX, "Girilen Yeni Şifre Değeri : " + new[i])
                    cprint(Fore.LIGHTBLUE_EX, "Girilen Yeni Şifre Değeri Tekrarı : " + new_b[i])
                    print("")
                    cprint(Fore.YELLOW, "Beklenen Sonuç = GİRİŞ BAŞARISIZ!")
                    print("")
                    cprint(Fore.GREEN, "Alınan Sonu. = GİRİŞ BAŞARISIZ!")
                    print("")
                    cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARILI!")
                    print("")
                    time.sleep(0.5)
                
                else:
                    d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    with open("LOGS/log-ogrsif.txt", "a") as file:
                        file.write(" " + "\n")   
                        file.write(str(d))
                        file.write(" " + "\n")
                        file.write("Yapılan test: Başarısız şifre testi")
                        file.write(" " + "\n")
                        file.write("Girilen Yeni Şifre Değeri : " + new[i])
                        file.write(" " + "\n")
                        file.write("Girilen Yeni Şifre Değeri Tekrarı : " + new_b[i])
                        file.write(" " + "\n")
                        file.write("Beklenen sonuç: GİRİŞ BAŞARISIZ!")
                        file.write(" " + "\n") 
                        file.write("Alınan sonuç: GİRİŞ BAŞARILI!")  
                        file.write(" " + "\n\n") 
                        file.write("TEST BAŞARISIZ!")  
                        file.write(" " + "\n\n")   
                    cprint(Fore.LIGHTBLUE_EX, "Test Çalıştırılma Tarih/Saati : " + str(d))
                    print("")
                    cprint(Fore.LIGHTMAGENTA_EX, "Giriş - " + str(i+1))    
                    cprint(Fore.LIGHTBLUE_EX, "Girilen Yeni Şifre Değeri : " + new[i])
                    cprint(Fore.LIGHTBLUE_EX, "Girilen Yeni Şifre Değeri Tekrarı : " + new_b[i])
                    print("")
                    cprint(Fore.YELLOW, "Beklenen Sonuç = GİRİŞ BAŞARISIZ!")
                    print("")
                    cprint(Fore.RED, "Alınan Sonu. = GİRİŞ BAŞARILI!")
                    print("")
                    cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARISIZ!")
                    print("")
                    time.sleep(0.5)
                        
            else:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/log-ogrsif.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarısız şifre testi")
                    file.write(" " + "\n")
                    file.write("Girilen Yeni Şifre Değeri : " + new[i])
                    file.write(" " + "\n")
                    file.write("Girilen Yeni Şifre Değeri Tekrarı : " + new_b[i])
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: GİRİŞ BAŞARISIZ!")
                    file.write(" " + "\n") 
                    file.write("Alınan sonuç: GİRİŞ BAŞARISIZ!")  
                    file.write(" " + "\n\n") 
                    file.write("TEST BAŞARILI!")  
                    file.write(" " + "\n\n")   
                cprint(Fore.LIGHTBLUE_EX, "Test Çalıştırılma Tarih/Saati : " + str(d))
                print("")
                cprint(Fore.LIGHTMAGENTA_EX, "Giriş - " + str(i+1))    
                cprint(Fore.LIGHTBLUE_EX, "Girilen Yeni Şifre Değeri : " + new[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Yeni Şifre Değeri Tekrarı : " + new_b[i])
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç = GİRİŞ BAŞARISIZ!")
                print("")
                cprint(Fore.GREEN, "Alınan Sonu. = GİRİŞ BAŞARISIZ!")
                print("")
                cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARILI!")
                print("")
                time.sleep(0.5)
        cprint(Fore.YELLOW, "Çıkmak için 'e' başarılı test için 'b' tuşlayın")
        a = input()
        if a == 'e':
            driver.close()
        elif a == 'b':
            time.sleep(1)

            self.new = self.driver.find_element_by_id(self.degerler["sif_new"])
            self.new_b = self.driver.find_element_by_id(self.degerler["sif_new_b"])
            self.button = self.driver.find_element_by_id(self.degerler["sifre_btn"])
            time.sleep(2)
            ogrenci_sifre.basarili(["123456"], ["123456"])
                
                
    def basarili(self, new, new_b):
        db = MySQLdb.connect(host= "127.0.0.1", user = "root", passwd = "", db= "deustaj", use_unicode=True, charset="utf8")
        cursor = db.cursor()
        for i in range (len(new)):

 
            self.new.clear()
            self.new_b.clear()

            self.new.send_keys(new[i])
            self.new_b.send_keys(new_b[i])     
            self.button.click()
            time.sleep(1)
    
            self.btn_success = self.driver.find_element_by_class_name("btn-success")
            self.btn_success.click() 
            time.sleep(2)
            
            self.hash_object = hashlib.md5(new[i].encode())
            print(self.ogr_no)
            cursor.execute("SELECT * FROM ogr WHERE ogr_sifre = '%s' AND ogr_no = '%s'" % (self.hash_object.hexdigest(), self.ogr_no))
            
            if cursor.rowcount > 0:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/log-ogrsif.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarılı şifre testi")
                    file.write(" " + "\n")
                    file.write("Girilen Yeni Şifre Değeri : " + new[i])
                    file.write(" " + "\n")
                    file.write("Girilen Yeni Şifre Değeri Tekrarı : " + new_b[i])
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: GİRİŞ BAŞARILI!")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: GİRİŞ BAŞARILI!")
                    file.write(" " + "\n\n")
                    file.write("TEST BAŞARILI")
                    file.write(" " + "\n\n")
                cprint(Fore.LIGHTBLUE_EX, "Test Çalıştırılma Tarih/Saati : " + str(d))
                print("")
                cprint(Fore.LIGHTMAGENTA_EX, "Giriş - " + str(i+1))    
                cprint(Fore.LIGHTBLUE_EX, "Girilen Yeni Şifre Değeri : " + new[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Yeni Şifre Değeri Tekrarı : " + new_b[i])
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç = GİRİŞ BAŞARILI!")
                print("")
                cprint(Fore.GREEN, "Alınan Sonu. = GİRİŞ BAŞARILI!")
                print("")
                cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARILI!")
                print("")
                time.sleep(0.5)
                                
            else:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/log-ogrsif.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarılı şifre testi")
                    file.write(" " + "\n")
                    file.write("Girilen Yeni Şifre Değeri : " + new[i])
                    file.write(" " + "\n")
                    file.write("Girilen Yeni Şifre Değeri Tekrarı : " + new_b[i])
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: GİRİŞ BAŞARILI!")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: GİRİŞ BAŞARISIZ!")
                    file.write(" " + "\n\n")
                    file.write("TEST BAŞARISIZ!")
                    file.write(" " + "\n\n")
                cprint(Fore.LIGHTBLUE_EX, "Test Çalıştırılma Tarih/Saati : " + str(d))
                print("")
                cprint(Fore.LIGHTMAGENTA_EX, "Giriş - " + str(i+1))    
                cprint(Fore.LIGHTBLUE_EX, "Girilen Yeni Şifre Değeri : " + new[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Yeni Şifre Değeri Tekrarı : " + new_b[i])
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç = GİRİŞ BAŞARILI!")
                print("")
                cprint(Fore.RED, "Alınan Sonuç = GİRİŞ BAŞARISIZ!")
                print("")
                cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARISIZ!")
                print("")
                time.sleep(0.5)
        cprint(Fore.YELLOW, "Çıkmak için 'e' başarısız test için 'b' tuşlayın")
        a = input()
        if a == 'e':
            driver.close()
        elif a == 'b':
            time.sleep(1)
            self.new = self.driver.find_element_by_id(self.degerler["sif_new"])
            self.new_b = self.driver.find_element_by_id(self.degerler["sif_new_b"])
            self.button = self.driver.find_element_by_id(self.degerler["sifre_btn"])
            time.sleep(2)
            ogrenci_sifre.basarisiz(["123452","1234518"], ["123456","232235"])
                
driver = webdriver.Chrome("C:\\xampp\\chromedriver.exe")

ogrenci_sifre = ogrenci_sifre(driver, "http://localhost:100/admin", "http://localhost:100/ogrenciler", {"sif_new": "new_pass_a", "sif_new_b": "new_pass_b", "sifre_btn": "sifre_btn"})

 
print(Fore.YELLOW + "Başarısız test için 1, başarılı test için 2") 
test = int(input())

print(" ")


if test == 1:
    print(Fore.YELLOW + "Çalıştırılan test: " + "ogrenci_sifre, basarisiz_test", end="\n\n")
    # Öğrenci_giris sınıfının içindeki basarisiz define degerleri gönderiyoruz 
    ogrenci_sifre.basarisiz(["123452","1234518"], ["123456","232235"])


elif test == 2:
    print(Fore.YELLOW + "Çalıştırılan test: " + "ogrenci_sifre, basarili_test")
    ogrenci_sifre.basarili(["123456"], ["123456"])
    print("")
    
    


