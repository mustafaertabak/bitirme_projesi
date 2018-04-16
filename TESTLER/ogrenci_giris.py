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

# Burada ogrenci_giris sayfasını test edeceğimiz için genel bir "ogrenci_giris" sınıfı açtık
class ogrenci_giris:
   # Alttaki sınıfların miras alabilmeleri için init şeklinde def tanımladık ve bu defin içine ihtiyacımız olan değerleri aldık
    def __init__(self, driver, url, dizi):
    # Değer atamalarını yaptık 
       self.driver = driver
       self.url = url
       self.driver.get(self.url)
    # Degerleri birden fazla göndereceğimiz için dizi şeklinde atadık 
       self.degerler = dizi 
    # Diziden gelen değerler ile eşleşen input idlerini bulduk ve değişkenlere atadık
       self.el_id = self.driver.find_element_by_id(self.degerler["username"])
       self.el_pas = self.driver.find_element_by_id(self.degerler["pass"])
       self.sb_btn = self.driver.find_element_by_id(self.degerler["submit_button"])
      
    # Sadece başarılı sonuçlar göndereceğimiz test defini açtık   
    def basarili(self, u_name, u_pass):
        # i'den u_name değişkeninin uzunluğuna kadar bir döngü oluşturduk 
        for i in range(len(u_name)):               
            self.el_id.clear()
            self.el_pas.clear()

            # Ögrenci sınıfından aldığımız inputlara diziden değer gönderiyoruz 
            self.el_id.send_keys(u_name[i])
            self.el_pas.send_keys(u_pass[i])           
            # Ögrenci sınıfından aldığımız buttona tıklayarak girişe yönlendiriyoruz
            self.sb_btn.click()
            # Sayfa açıldıktan sonra değerleri okuyabilmek adına zaman aşımı uyguladık
            time.sleep(2)
            # Kontol yapabilmek adına result değişkeni tanımladık 
            result = None

            # Kodların düzgün çalışması durumunda çalışacak komutlar 
            try:
                # Burada way değişkenine degerler dizisinden gelen elemanının id'sini alıyoruz
                self.way = driver.find_element_by_id(self.degerler["deger"])
                result = True    
                # Normal olmayan koşullarda çalışacak kodlar                      
            except:
                result = False
            # Eğer elemanın idsi bulunduysa yapılacak işlemler 
            if result:
                # Logların yazdırıldığı blok 
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
                # Eğer elemanın idsi bulunamadıysa yapılacak işlemler 
                cprint(Fore.RED, "Giriş Başarısız")
                time.sleep(0.5)

    # Sadece başarısız değeleri gönderdiğimiz test defini oluşturduk
    def basarisiz(self,u_name,u_pass):
        for i in range(len(u_name)): 
            # Birden fazla değer gönderdiğimizden dolayı sonraki değerler için inputları boşalttık              
            self.el_id.clear()
            self.el_pas.clear()
            # Ögrenci sınıfından aldığımız inputlara diziden değer gönderiyoruz
            self.el_id.send_keys(u_name[i])
            self.el_pas.send_keys(u_pass[i])
            # Ögrenci sınıfından aldığımız buttona tıklayarak girişe yönlendiriyoruz
            self.sb_btn.click()

            result = None
            # Kodların düzgün çalışması durumunda çalışacak komutlar 
            try:
                # Burada way değişkenine degerler dizisinden gelen elemanının id'sini alıyoruz
                self.way = self.driver.find_element_by_id(self.degerler["deger"])
                result = True
            # Normal olmayan koşullarda çalışacak kodlar    
            except:
                result = False 
            # Eğer elemanın idsi bulunduysa yapılacak işlemler    
            if result == True:
                cprint(Fore.GREEN, "Giriş Başarılı")
            # Eğer elemanın idsi bulunamadıysa yapılacak işlemler  
            else:
                # Logları yazdırıyoruz 
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/log-ogrenci.txt", "a") as file:
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
# Driver değişkenine chromedriver yolunu atıyoruz 
driver = webdriver.Chrome("C:\\Users\\BERKE\\Downloads\\chromedriver.exe")

# Öğrenci giriş sınıfının parametre değerlerini atıyoruz 
ogrenci_giris = ogrenci_giris(driver, "http://localhost:100/ogrenci-giris", {"username": "username", "pass": "pass", "deger": "baslik_id", "submit_button": "submit_button"})

# Hangi testin çalıştırılacağını sorguluyoruz 
print(Fore.BLUE + "Başarısız test için 1, başarılı test için 2") 
test = int(input())

print(" ")

# 1'e basılırsa yapılacak işlemler 
if test == 1:
    print(Fore.YELLOW + "Çalıştırılan test: " + "ogrenci_giris, basarisiz_test", end="\n\n")
    # Öğrenci_giris sınıfının içindeki basarisiz define degerleri gönderiyoruz 
    ogrenci_giris.basarisiz(["20167070", "12345", "1379248"], ["5656", "6565", "35653235"])

    
# 1'e basılırsa yapılacak işlemler 
elif test == 2:
    print(Fore.YELLOW + "Çalıştırılan test: " + "ogrenci_giris, basarili_test")
    print("")
    # Öğrenci_giris sınıfının içindeki basarili define degerleri gönderiyoruz 
    ogrenci_giris.basarili(["2016707005"],["123456"])
   






 
        


