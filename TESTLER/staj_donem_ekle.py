# Bu kısımda gerekli importları yaptık
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import MySQLdb
import hashlib
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

class staj_donemi_ekle:
    
    def __init__(self, driver, url, url2, arr):
        db = MySQLdb.connect(host= "127.0.0.1", user = "root", passwd = "", db= "deustaj", use_unicode=True, charset="utf8")
        self.cursor = db.cursor()
        db.commit()
        self.cursor.execute("SELECT * FROM stajdonemi")
        self.driver = driver
        self.url = url 
        self.driver.get(self.url)
        self.url_donem = url2
        self.arr = arr 

        self.a_name = self.driver.find_element_by_id("username")
        self.a_pass = self.driver.find_element_by_id("pass")
        self.a_btn = self.driver.find_element_by_id("submit_button")
        
        self.a_name.send_keys("7040000001")
        self.a_pass.send_keys("123456")
        self.a_btn.click()
        self.driver.get(self.url_donem)
        time.sleep(2)

        self.donem = self.driver.find_element_by_id(self.arr["sd"])
        self.drp_dwn = self.driver.find_element_by_id(self.arr["donem_btn"])
        self.drp_item = self.driver.find_element_by_xpath("//label[@for='r_id_c_b_1']")
        self.st_baslangic = self.driver.find_element_by_id(self.arr["staj_baslangic"])
        self.st_bitis = self.driver.find_element_by_id(self.arr["staj_bitis_d"])
        self.b_basla = self.driver.find_element_by_id(self.arr["basvuru_baslangici"])
        self.b_bitis = self.driver.find_element_by_id(self.arr["basvuru_bitis_d"])
        self.btn = self.driver.find_element_by_id(self.arr["sde_btn"])

    def basarili(self, staj_baslangic, staj_bitis_d, basvuru_baslangici, basvuru_bitis_d):
        db2 = MySQLdb.connect(host= "127.0.0.1", user = "root", passwd = "", db= "deustaj", use_unicode=True, charset="utf8")
        cursor_2 = db2.cursor()
        for i in range(len(basvuru_baslangici)):
            
            self.donem.click()
            self.drp_dwn.click()
            time.sleep(1.5)
            self.drp_item.click()         
    
            self.st_baslangic.send_keys(staj_baslangic[i])
            self.st_bitis.send_keys(staj_bitis_d[i])
            self.b_basla.send_keys(basvuru_baslangici[i])
            self.b_bitis.send_keys(basvuru_bitis_d[i])
            self.btn.click()
            time.sleep(1.5)
            self.driver.find_element_by_class_name("btn-success").click()
            time.sleep(3)
            db2.commit()
            cursor_2.execute("SELECT * FROM stajdonemi") 
        
        if cursor_2.rowcount > self.cursor.rowcount:
            print("Başarılı")
        else:
            print("Başarısız")

    def basarisiz(self, staj_baslangic, staj_bitis_d, basvuru_baslangici, basvuru_bitis_d):
           for i in range(len(basvuru_baslangici)):
            
            self.donem.click()
            self.drp_dwn.click()
            time.sleep(1.5)
            self.drp_item.click()         
    
            self.st_baslangic.send_keys(staj_baslangic[i])
            self.st_bitis.send_keys(staj_bitis_d[i])
            self.b_basla.send_keys(basvuru_baslangici[i])
            self.b_bitis.send_keys(basvuru_bitis_d[i])
            self.btn.click()
            self.ul = self.driver.find_element_by_id("sde_w").is_displayed()

            if self.ul:
                print("başarısız")
            
            else:
                print("başarılı")
                

driver = webdriver.Chrome("C:\\Users\\BERKE\\Desktop\\bitirme\\chromedriver.exe")

staj_donemi_ekle = staj_donemi_ekle(driver, "http://localhost:100/admin", "http://localhost:100/stajdonemi-ekle", {"sd": "sd_y_u", "donem_btn": "donem_btn", "staj_baslangic": "staj_baslangic", "staj_bitis_d": "staj_bitisi", "basvuru_baslangici": "basvuru_baslangici", "basvuru_bitis_d": "basvuru_bitisi", "sde_btn": "sde_btn"})


print(Fore.YELLOW + "Başarısız test için 1, başarılı test için 2") 
test = int(input())

print(" ")

if test == 1:
    print(Fore.YELLOW + "Çalıştırılan test: " + "staj_donem_ekle, basarisiz_test", end="\n\n")
    # Öğrenci_giris sınıfının içindeki basarisiz define degerleri gönderiyoruz 
    staj_donemi_ekle.basarisiz(["10-09-11","11-10-11"], ["10-09-11", "11-10-11"], ["01-10-1998","26-10-1998"], ["01-10", "10-11"])
    print("")

elif test == 2:
    print(Fore.YELLOW + "Çalıştırılan test: " + "staj_donem_ekle, basarili_test") 
    staj_donemi_ekle.basarili(["10-09-2018"] ,["30-09-2018"], ["01-10-2018"], ["29-10-2018"])
    print("")
    
