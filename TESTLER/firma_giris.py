# Bu kısımda gerekli importları yaptık
from selenium import webdriver

import colorama 
from colorama import Fore, Back, Style

import datetime
import time

colorama.init()

# Textlerden renkli çıktı alabilmek için coloromayı init edip fonksiyon içinde tanımladık
def cprint(color, text):
    print(color + text)

# Burada ogrenci_giris sayfasını test edeceğimiz için genel bir "firma_giris" sınıfı açtık
class firma_giris:
     # Alttaki sınıfların miras alabilmeleri için init şeklinde def tanımladık ve bu defin içine ihtiyacımız olan değerleri aldık
    def __init__(self, driver, url,dizi):
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

            # Firma sınıfından aldığımız inputlara diziden değer gönderiyoruz 
            self.el_id.send_keys(u_name[i])
            self.el_pas.send_keys(u_pass[i])
            # Firma sınıfından aldığımız buttona tıklayarak girişe yönlendiriyoruz     
            self.sb_btn.click()
            # Kontol yapabilmek adına result değişkeni tanımladık 
            time.sleep(2)
            result = None

            # Kodların düzgün çalışması durumunda çalışacak komutlar
            try:
                 # Burada check değişkenine degerler dizisinden gelen elemanının id'sini alıyoruz
                self.check = self.driver.find_element_by_class_name(self.degerler["deger"]).is_displayed()
                result = True
            # Normal olmayan koşullarda çalışacak kodlar 
            except:
                result = False 
            # Eğer elemanın idsi bulunduysa yapılacak işlemler 
            if result:
                # Logların yazdırıldığı blok 
                date_t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/log-firma.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(date_t))
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
            # Firma sınıfından aldığımız inputlara diziden değer gönderiyoruz 
            self.el_id.send_keys(u_name[i])
            self.el_pas.send_keys(u_pass[i])
            # Firma sınıfından aldığımız buttona tıklayarak girişe yönlendiriyoruz
            self.sb_btn.click()        

            result = None
            
            # Kodların düzgün çalışması durumunda çalışacak komutlar 
            try:
                # Burada check değişkenine degerler dizisinden gelen elemanının id'sini alıyoruz
                self.check = self.driver.find_element_class_name(self.degerler["deger"]).is_displayed()
                result = True
            # Normal olmayan koşullarda çalışacak kodlar 
            except:
                result = False 
            
            # Eğer elemanın idsi bulunduysa yapılacak işlemler      
            if result:
                cprint(Fore.GREEN, "Giriş Başarılı")
            # Eğer elemanın idsi bulunamadıysa yapılacak işlemler  
            else:
                # Logları yazdırıyoruz 
                date_t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/log-firma.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(date_t))
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

# Firma giriş sınıfının parametre değerlerini atıyoruz 
firma_giris = firma_giris(driver, "http://localhost:100/firma-giris", {"username": "username", "pass": "pass", "deger": "dropdown-toggle", "submit_button": "submit_button"})

# Hangi testin çalıştırılacağını sorguluyoruz 
print(Fore.YELLOW + "Başarısız test için 1, başarılı test için 2") 
test = int(input())
print(" ")

# 1'e basılırsa yapılacak işlemler 
if test == 1:
    print(Fore.YELLOW + "Çalıştırılan test: " + "firma_giris, basarisiz_test")
    print("")
    # Firma_giris sınıfının içindeki basarisiz define degerleri gönderiyoruz 
    firma_giris.basarisiz(["20167070", "12345", "1379248"], ["5656", "6565", "35653235"])

# 2'ye basılırsa yapılacak işlemler 
if test == 2:
    print(Fore.YELLOW + "Çalıştırılan test: " + "firma_giris, basarili_test") 
    # Firma_giris sınıfının içindeki basarili define degerleri gönderiyoruz 
    firma_giris.basarili(["vestel"], ["123456"])
   
