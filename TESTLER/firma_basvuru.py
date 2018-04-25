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

class firma_basvuru:

    def __init__(self, driver, url, dizi):
        db = MySQLdb.connect(host= "127.0.0.1", user = "root", passwd = "", db= "deustaj", use_unicode=True, charset="utf8")
        self.cursor = db.cursor()
        self.cursor.execute("SELECT * FROM f_basvurular") 
        print (self.cursor.rowcount)

        self.driver = driver
        self.url = url
        self.driver.get(self.url)
        self.degerler = dizi 
        time.sleep(1)
        
        self.b_mail = self.driver.find_element_by_id(self.degerler["basvuru_mail"])
        self.b_button = self.driver.find_element_by_id(self.degerler["basvuru_btn"])

    def basarisiz(self, mail):
        
        for i in range(len(mail)):
            self.b_mail.clear()
            self.b_mail.send_keys(mail[i])
            self.b_button.click()
            time.sleep(2)
            self.li_id = self.driver.find_element_by_id("f_basvuru_w").is_displayed()
            
            if self.li_id:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/firma-basvuru.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarısız e-mail başvuru testi")
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: Başarısız")
                    file.write(" " + "\n") 
                    file.write("Alınan sonuç: Başarısız")  
                    file.write(" " + "\n\n")      
                    file.write("TEST BAŞARILI")     
                cprint(Fore.RED, "Başarısız")
                time.sleep(0.5)
            else:
                cprint(Fore.GREEN, "Başarılı")
    
    def basarili(self,mail):
        db2 = MySQLdb.connect(host= "127.0.0.1", user = "root", passwd = "", db= "deustaj", use_unicode=True, charset="utf8")
        cursor2 = db2.cursor()
          
        for i in range(len(mail)):
            self.b_mail.send_keys(mail[i])
            self.b_button.click()
            self.driver.find_element_by_class_name("btn-success").click()
            self.disp = self.b_mail.is_displayed() 
            time.sleep(3)

            cursor2.execute("SELECT * FROM f_basvurular")
            print (cursor2.rowcount)

            if cursor2.rowcount > self.cursor.rowcount:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/firma-basvuru.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarılı e-mail başvuru testi")
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: Başarılı")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: Başarılı")
                    file.write(" " + "\n\n")
                cprint(Fore.GREEN, "Başarılı")                   
                time.sleep(0.5)
            else:
                cprint(Fore.RED, "Başarısız")

driver = webdriver.Chrome("C:\\Users\\BERKE\\Downloads\\chromedriver.exe")


firma_basvuru = firma_basvuru(driver, "http://localhost:100/firma-basvuru", {"basvuru_mail": "f_basvuru_mail", "basvuru_btn": "f_basvuru_btn"})

print(Fore.YELLOW + "Başarısız test için 1, başarılı test için 2") 
test = int(input())

print(" ")

if test == 1:
    print(Fore.YELLOW + "Çalıştırılan test: " + "firma_basvuru", "basarisiz_test", end="\n\n")
    # Öğrenci_giris sınıfının içindeki basarisiz define degerleri gönderiyoruz 
    firma_basvuru.basarisiz(["berke.com","1234518"])

elif test == 2:
    print(Fore.YELLOW + "Çalıştırılan test: " + "firma_basvuru", "basarili_test")
    firma_basvuru.basarili(["basvuru@gmail.com"])
    print("")
           

       