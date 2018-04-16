# Gerekli importları bu kısımda yapıyoruz 
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


class ogrenci_sifre:
    

    def __init__(self, driver, url, url2, dizi):
    
        self.driver = driver 
        self.url = url 
        self.url_2 = url2
        self.driver.get(self.url)
        self.k_id = self.driver.find_element_by_id("username")
        self.k_pas = self.driver.find_element_by_id("pass")
        self.btn = self.driver.find_element_by_id("submit_button")

        self.k_id.send_keys("2016707005")
        self.k_pas.send_keys("123456")
        self.btn.click()
        time.sleep(1.5)
        self.driver.get(self.url_2)
        self.driver.find_element_by_id("sifre_degis").click()
        
        self.degerler = dizi 

        self.old = self.driver.find_element_by_id(self.degerler["sif_old"])
        self.new = self.driver.find_element_by_id(self.degerler["sif_new"])
        self.new_b = self.driver.find_element_by_id(self.degerler["sif_new_b"])
        self.button = self.driver.find_element_by_id(self.degerler["sifre_btn"])

    def basarisiz(self, old, new, new_b):    
        for i in range (len(new)):

            self.old.clear()
            self.new.clear()
            self.new_b.clear()

            self.old.send_keys(old[i])
            self.new.send_keys(new[i])
            self.new_b.send_keys(new_b[i])
            self.button.click()
            time.sleep(1)

            self.show = self.driver.find_element_by_id("sifre").is_displayed()
             
            if self.show == False:
                cprint(Fore.GREEN, "Giriş Başarılı")
            else:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/log-ogrsif.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarısız şifre testi")
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: Başarısız")
                    file.write(" " + "\n") 
                    file.write("Alınan sonuç: Başarısız")  
                    file.write(" " + "\n\n")           
                cprint(Fore.RED, "Giriş Başarısız")
                time.sleep(0.5)

    def basarili(self, old, new, new_b):
        for i in range (len(new)):
            self.old.send_keys(old[i])
            self.new.send_keys(new[i])
            self.new_b.send_keys(new_b[i])
            self.button.click()
            time.sleep(1)

        self.btn_success = self.driver.find_element_by_class_name("btn-success")
        self.btn_success.click() 
        time.sleep(2)
        self.show = self.driver.find_element_by_id("sifre").is_displayed()

        if self.show == False:
            d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("LOGS/log-ogrsif.txt", "a") as file:
                file.write(" " + "\n")   
                file.write(str(d))
                file.write(" " + "\n")
                file.write("Yapılan test: Başarılı şifre testi")
                file.write(" " + "\n")
                file.write("Beklenen sonuç: Başarılı")
                file.write(" " + "\n")
                file.write("Alınan sonuç: Başarılı")
                file.write(" " + "\n\n")
            cprint(Fore.GREEN, "Giriş Başarılı")
                               
            time.sleep(0.5)
        else:
            cprint(Fore.RED, "Giriş Başarısız")
                
        

driver = webdriver.Chrome("C:\\Users\\BERKE\\Downloads\\chromedriver.exe")

ogrenci_sifre = ogrenci_sifre(driver, "http://localhost:100/ogrenci-giris", "http://localhost:100/profil", {"sif_old": "old_pass", "sif_new": "new_pass_a", "sif_new_b": "new_pass_b","sifre_btn": "sifre_btn"})

 
print(Fore.BLUE + "Başarısız test için 1, başarılı test için 2") 
test = int(input())

print(" ")


if test == 1:
    print(Fore.YELLOW + "Çalıştırılan test: " + "ogrenci_sifre, basarisiz_test", end="\n\n")
    # Öğrenci_giris sınıfının içindeki basarisiz define degerleri gönderiyoruz 
    ogrenci_sifre.basarisiz(["123452","123456"], ["123","213"], ["123","12364"])


elif test == 2:
    print(Fore.YELLOW + "Çalıştırılan test: " + "ogrenci_sifre, basarili_test")
    ogrenci_sifre.basarili(["123456"], ["123456"], ["123456"])
    print("")
    
    


