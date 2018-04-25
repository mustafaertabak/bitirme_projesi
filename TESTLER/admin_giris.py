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
                with open("LOGS/log-ogrenci.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarılı giriş testi")
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: Başarılı")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: Başarılı")
                    file.write(" " + "\n\n")        
                cprint(Fore.GREEN, "Giriş Başarılı")    
            else:         

                cprint(Fore.RED, "Giriş Başarısız")
                time.sleep(0.5)

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
                with open("LOGS/log-ogrenci.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarılı giriş testi")
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: Başarılı")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: Başarılı")
                    file.write(" " + "\n\n")        
                cprint(Fore.GREEN, "Giriş Başarılı")    
            else:         

                cprint(Fore.RED, "Giriş Başarısız")
                time.sleep(0.5)

driver = webdriver.Chrome("C:\\xampp\\chromedriver.exe")

admin_giris = admin_giris(driver, "http://localhost/admin", {"username": "username", "pass": "pass", "deger": "a-ilan-img", "submit_button": "submit_button"})

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
