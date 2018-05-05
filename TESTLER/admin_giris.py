# Bu kısımda gerekli importları yaptık
from selenium import webdriver
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

class admin_giris:

    def __init__(self, driver, url, dizi):
        self.driver = driver
        self.url = url
        self.driver.get(self.url)

        self.dizi = dizi

        self.a_name = self.driver.find_element_by_id(self.dizi["username"])
        self.a_pass = self.driver.find_element_by_id(self.dizi["pass"])
        self.a_btn = self.driver.find_element_by_id(self.dizi["submit_button"])

    def basarili(self, a_name, a_pass):

        for i in range(len(a_name)):
            self.a_name.clear()
            self.a_pass.clear()

            self.a_name.send_keys(a_name[i])
            self.a_pass.send_keys(a_pass[i])

            self.a_btn.click()
            time.sleep(2)

            result = None

            try:
                self.way = driver.find_element_by_class_name(self.dizi["deger"]).is_displayed()
                result = True    
                  
            except:
                result = False

            if result:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/log-admin.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarılı giriş testi")
                    file.write(" " + "\n")
                    file.write("Girilen Kullanıcı Adı : " + a_name[i])
                    file.write(" " + "\n")
                    file.write("Girilen Kullanıcı Şifresi : " + a_name[i])
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: GİRİŞ BAŞARILI!")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: GİRİŞ BAŞARALI!")
                    file.write(" " + "\n\n")
                    file.write("TEST BAŞARILI!")
                    file.write(" " + "\n\n")
                cprint(Fore.LIGHTBLUE_EX, "Test Çalıştırılma Tarih/Saati : " + str(d))
                print("")
                cprint(Fore.LIGHTBLUE_EX, "Girilen Kullanıcı Adı : " + a_name[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Kullanıcı Şifresi : " + a_pass[i])
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç = GİRİŞ BAŞARILI!")
                print("")
                cprint(Fore.GREEN, "Alınan Sonuç = GİRİŞ BAŞARILI!")
                print("")
                cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARILI!")      
                time.sleep(1)
            else:    
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/log-admin.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarısız giriş testi")
                    file.write(" " + "\n")
                    file.write("Girilen Kullanıcı Adı : " + a_name[i])
                    file.write(" " + "\n")
                    file.write("Girilen Kullanıcı Şifresi : " + a_name[i])
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: GİRİŞ BAŞARILI!")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: GİRİŞ BAŞARISIZ!")
                    file.write(" " + "\n\n")
                    file.write("TEST BAŞARISIZ!")
                    file.write(" " + "\n\n")  
                cprint(Fore.LIGHTBLUE_EX, "Test Çalıştırılma Tarih/Saati : " + str(d))
                print("")    
                cprint(Fore.LIGHTBLUE_EX, "Girilen Kullanıcı Adı : " + a_name[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Kullanıcı Şifresi : " + a_pass[i])
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç = GİRİŞ BAŞARILI!")
                print("")
                cprint(Fore.RED, "Alınan Sonuç = GİRİŞ BAŞARISIZ!")
                print("")
                cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARISIZ!")  
                time.sleep(1)
        cprint(Fore.YELLOW, "Çıkmak için 'e' başarısız test için 'b' tuşlayın")
        a = input()
        if a == 'e':
            driver.close()
        elif a == 'b':
            self.togg = self.driver.find_element_by_class_name("navbar-toggler").is_displayed()
            if self.togg:
                self.driver.find_element_by_class_name("navbar-toggler").click()
                time.sleep(1.5)
                self.driver.find_element_by_xpath( "//button[@data-toggle='dropdown']").click()
                time.sleep(1.5)
                self.driver.find_element_by_id("cik").click()
                time.sleep(1)
                self.driver.get(self.url)
                self.a_name = self.driver.find_element_by_id(self.dizi["username"])
                self.a_pass = self.driver.find_element_by_id(self.dizi["pass"])
                self.a_btn = self.driver.find_element_by_id(self.dizi["submit_button"])
                admin_giris.basarisiz(["70400056", "adasfsa"],["123456", "2345486"])
            else:
                self.driver.find_element_by_xpath( "//button[@data-toggle='dropdown']").click()
                self.driver.find_element_by_id("cik").click()
                time.sleep(1)
                self.driver.get(self.url)
                self.a_name = self.driver.find_element_by_id(self.dizi["username"])
                self.a_pass = self.driver.find_element_by_id(self.dizi["pass"])
                self.a_btn = self.driver.find_element_by_id(self.dizi["submit_button"])
                admin_giris.basarisiz(["70400056", "adasfsa"],["123456", "2345486"])

    def basarisiz(self, a_name, a_pass):
        for i in range(len(a_name)):
            self.a_name.clear()
            self.a_pass.clear()

            self.a_name.send_keys(a_name[i])
            self.a_pass.send_keys(a_pass[i])

            self.a_btn.click()
            time.sleep(2)

            result = None

            try:
                self.way = driver.find_element_by_class_name(self.dizi["deger"]).is_displayed()
                result = True
            
            except:
                result = False

            if result:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/log-admin.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarısız giriş testi")
                    file.write(" " + "\n")
                    file.write("Girilen Kullanıcı Adı : " + a_name[i])
                    file.write(" " + "\n")
                    file.write("Girilen Kullanıcı Şifresi : " + a_name[i])
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: GİRİŞ BAŞARISIZ")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: GİRİŞ BAŞARILI!")
                    file.write(" " + "\n\n")
                    file.write("TEST BAŞARISIZ!")
                    file.write(" " + "\n\n")     
                cprint(Fore.LIGHTBLUE_EX, "Test Çalıştırılma Tarih/Saati : " + str(d))
                print("")
                cprint(Fore.LIGHTMAGENTA_EX, "GİRİŞ - " + str(i+1))   
                print("")
                cprint(Fore.LIGHTBLUE_EX, "Girilen Kullanıcı Adı : " + a_name[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Kullanıcı Şifresi : " + a_pass[i])
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç = GİRİŞ BAŞARISIZ!")
                print("")
                cprint(Fore.RED, "Alınan Sonuç = GİRİŞ BAŞARILI!")
                print("")
                cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARISIZ!")    
                print("\n") 
                time.sleep(1)

            else:  
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/log-admin.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarısız giriş testi")
                    file.write(" " + "\n")
                    file.write("Girilen Kullanıcı Adı : " + a_name[i])
                    file.write(" " + "\n")
                    file.write("Girilen Kullanıcı Şifresi : " + a_name[i])
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: GİRİŞ BAŞARISIZ!")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: GİRİŞ BAŞARISIZ!")
                    file.write(" " + "\n\n")
                    file.write("TEST BAŞARILI!")
                    file.write(" " + "\n\n")  
                cprint(Fore.LIGHTBLUE_EX, "Test Çalıştırılma Tarih/Saati : " + str(d))
                print("")
                cprint(Fore.LIGHTMAGENTA_EX, "Giriş - " +  str(i+1))
                print("")         
                cprint(Fore.LIGHTBLUE_EX, "Girilen Kullanıcı Adı : " + a_name[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Kullanıcı Şifresi : " + a_pass[i])
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç = GİRİŞ BAŞARISIZ!")
                print("")
                cprint(Fore.GREEN, "Alınan Sonuç = GİRİŞ BAŞARISIZ!")
                print("")
                cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARILI!")  
                print("\n") 
                time.sleep(1)

        cprint(Fore.YELLOW, "Çıkmak için 'e' başarılı test için 'b' tuşlayın")
        a = input()
        if a == 'e':
            driver.close()
        elif a == 'b':
            self.a_name = self.driver.find_element_by_id(self.dizi["username"])
            self.a_pass = self.driver.find_element_by_id(self.dizi["pass"])
            self.a_btn = self.driver.find_element_by_id(self.dizi["submit_button"])
            admin_giris.basarili(["7040000001"],["123456"])

# Driver değişkenine chromedriver yolunu atıyoruz 
driver = webdriver.Chrome("C:\\Users\\BERKE\\Desktop\\bitirme\\chromedriver.exe")

admin_giris = admin_giris(driver, "http://localhost:100/admin", {"username": "username", "pass": "pass", "deger": "a-ilan-img", "submit_button": "submit_button"})

print(Fore.YELLOW + "Başarısız test için 1, başarılı test için 2") 
test = int(input())

print(" ")


if test == 1:
    print(Fore.YELLOW + "Çalıştırılan test: " + "admin_giris, basarisiz_test", end="\n\n")

    admin_giris.basarisiz(["20167070", "12345", "1379248"], ["5656", "6565", "35653235"])

    

elif test == 2:
    print(Fore.YELLOW + "Çalıştırılan test: " + "admin_giris, basarili_test")
    print("")

    admin_giris.basarili(["7040000001"],["123456"])
