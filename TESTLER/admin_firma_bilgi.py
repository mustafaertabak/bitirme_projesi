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

class admin_firma_bilgi:

    def __init__(self, driver, url, url2, dizi):
        db = MySQLdb.connect(host= "127.0.0.1", user = "root", passwd = "", db= "deustaj", use_unicode=True, charset="utf8")
        self.cursor = db.cursor()
        self.cursor.execute("SELECT * FROM f_basvurular") 
        
        self.degerler = dizi 
        self.driver = driver 
        self.url2 = url2 
        self.url = url 
        self.driver.get(self.url)

        self.u_name = self.driver.find_element_by_id("username")
        self.u_pass = self.driver.find_element_by_id("pass")
        self.u_name.send_keys("7040000001")
        self.u_pass.send_keys("123456")
        self.driver.find_element_by_id("submit_button").click()
        time.sleep(2)
        
        self.driver.get(self.url2)
        time.sleep(2)

        self.driver.find_element_by_id("firma_kart").click()
        time.sleep(1.5)

        self.driver.find_element_by_id("show_info").click()
        time.sleep(1.5)
        self.b_isim = self.driver.find_element_by_id(self.degerler["bilgiler_isim"])
        self.b_gad = self.driver.find_element_by_id(self.degerler["bilgiler_giris_adi"])
        self.b_gbtn = self.driver.find_element_by_id(self.degerler["bilgiler_btn"])
        self.b_text = self.driver.find_element_by_id(self.degerler["bilgiler_text"])

    def basarisiz(self, frm_adi, frm_kadi, bilgi_text):
        for i in range (len(frm_adi)):
            
            self.b_isim.clear()
            self.b_gad.clear()
            self.b_text.clear()

            self.b_text.send_keys(bilgi_text[i])
            self.b_isim.send_keys(frm_adi[i])
            self.b_gad.send_keys(frm_kadi[i])
            self.b_gbtn.click()
            time.sleep(1.5)
            self.bilgi_btn = self.driver.find_element_by_class_name("btn-success").is_displayed()

            if self.bilgi_btn == False:
                dtm = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/admin-firma-bilgi.txt", "a") as file:
                    file.write(" " + "\n")
                    file.write(str(dtm))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Firma Profil sayfasının Bilgi Düzenle alanının BAŞARISIZ testi!")
                    file.write(" " + "\n")
                    file.write("Firmanın Adı : " + frm_adi[i])
                    file.write(" " + "\n")
                    file.write("Firmanın Kullanıcı Adı : " + frm_kadi[i])
                    file.write(" " + "\n")
                    file.write("Girilen Açıklama Bilgisi : " + bilgi_text[i])
                    file.write(" " + "\n")
                    file.write("Beklenen Sonuç: İŞLEM BAŞARISIZ!")
                    file.write(" " + "\n")
                    file.write("Alınan Sonuç: İŞLEM BAŞARISIZ!")
                    file.write(" " + "\n\n")
                    file.write("TEST BAŞARILI!")
                    file.write(" " + "\n\n")
                cprint(Fore.LIGHTBLUE_EX, "Test Çalıştırılma Tarih/Saat'i : " + str(dtm))
                print("")   
                cprint(Fore.LIGHTMAGENTA_EX, "GİRİŞ - " + str(i+1))   
                print("")
                cprint(Fore.LIGHTBLUE_EX, "Firmanın Adı : " + frm_adi[i])
                cprint(Fore.LIGHTBLUE_EX, "Firmanın Kullanıcı Adı : " + frm_kadi[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Açıklama Bilgisi : " + bilgi_text[i])
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç = İŞLEM BAŞARISIZ!")
                print("")
                cprint(Fore.GREEN, "Alınan Sonuç = İŞLEM BAŞARISIZ!")  
                print("")
                cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARILI!")
                print("\n") 
                time.sleep(1)

            else:
                dtm = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/admin-firma-bilgi.txt", "a") as file:
                    file.write(" " + "\n")
                    file.write(str(dtm))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Firma Profil sayfasının Bilgi Düzenle alanının BAŞARISIZ testi!")
                    file.write(" " + "\n")
                    file.write("Firmann Adı : " + frm_adi[i])
                    file.write(" " + "\n")
                    file.write("Firmamom Kullanıcı Adı : " + frm_kadi[i])
                    file.write(" " + "\n")
                    file.write("Girilen Açıklama Bilgisi : " + bilgi_text[i])
                    file.write(" " + "\n")
                    file.write("Beklenen Sonuç: İŞLEM BAŞARISIZ!")
                    file.write(" " + "\n")
                    file.write("Alınan Sonuç: İŞLEM BAŞARILI!")
                    file.write(" " + "\n\n")
                    file.write("TEST BAŞARISIZ!")
                    file.write(" " + "\n\n")         
                cprint(Fore.LIGHTBLUE_EX, "Test Çalıştırılma Tarih/Saat'i : " + str(dtm))
                print("")           
                cprint(Fore.LIGHTMAGENTA_EX, "Giriş - " +  str(i+1))
                print("")         
                cprint(Fore.LIGHTBLUE_EX, "Firmanın Adı : " + frm_adi[i])
                cprint(Fore.LIGHTBLUE_EX, "Firmanın Kullanıcı Adı : " + frm_kadi[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Açıklama Bilgisi : " + bilgi_text[i])
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç = İŞLEM BAŞARISIZ!")
                print("")
                cprint(Fore.RED, "Alınan Sonuç = İŞLEM BAŞARILI!")
                print("")
                cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARISIZ!")
                print("\n") 
                time.sleep(1)
        
        cprint(Fore.YELLOW, "Çıkmak için 'e' başarılı test için 'b' tuşlayın")
        a = input()
        if a == 'e':
            driver.close()
        elif a == 'b':
            self.driver.find_element_by_id("show_info").click()
            time.sleep(1)
            self.b_isim = self.driver.find_element_by_id(self.degerler["bilgiler_isim"])
            self.b_gad = self.driver.find_element_by_id(self.degerler["bilgiler_giris_adi"])
            self.b_gbtn = self.driver.find_element_by_id(self.degerler["bilgiler_btn"])
            self.b_text = self.driver.find_element_by_id(self.degerler["bilgiler_text"])
    
            admin_firma_bilgi.basarili(["testdeneme"], ["denemekullanıcıadı"], ["aciklama"])
        
    def basarili(self, frm_adi, frm_kadi, bilgi_text):
        db = MySQLdb.connect(host= "127.0.0.1", user = "root", passwd = "", db= "deustaj", use_unicode=True, charset="utf8")
        cursor = db.cursor()

        for i in range (len(frm_adi)):
            self.b_isim.clear()
            self.b_gad.clear()
            self.b_text.clear()

            self.b_text.send_keys(bilgi_text[i])
            self.b_isim.send_keys(frm_adi[i])
            self.b_gad.send_keys(frm_kadi[i])
            self.b_gbtn.click()
            time.sleep(1.5)

            self.bilgi_btn = self.driver.find_element_by_class_name("btn-success").click()
            time.sleep(2)
            cursor.execute("SELECT * FROM firmalar WHERE firma_isim = '%s' AND firma_giris_adi = '%s' AND firma_aciklama = '%s'" % (frm_adi[i], frm_kadi[i],bilgi_text[i]))

            if cursor.rowcount > 0:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/admin-firma-bilgi.txt", "a") as file:
                    file.write(" " + "\n")
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Firma Profil sayfasının Bilgi Düzenle alanının BAŞARILI testi!")
                    file.write(" " + "\n")
                    file.write("Firmann Adı : " + frm_adi[i])
                    file.write(" " + "\n")
                    file.write("Firmamom Kullanıcı Adı : " + frm_kadi[i])
                    file.write(" " + "\n")
                    file.write("Girilen Açıklama Bilgisi : " + bilgi_text[i])
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: İŞLEM BAŞARILI!")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: İŞLEM BAŞARILI!")
                    file.write(" " + "\n\n")
                    file.write("TEST BAŞARILI!")
                    file.write(" " + "\n\n")
                    
                cprint(Fore.YELLOW, "Test Çalıştırma Tarih/Saat'i : " + str(d))
                print("")
                cprint(Fore.LIGHTBLUE_EX, "Firmanın Adı : " + frm_adi[i])
                cprint(Fore.LIGHTBLUE_EX, "Firmanın Kullanıcı Adı : " + frm_kadi[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Açıklama Bilgisi : " + bilgi_text[i])
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç = İŞLEM BAŞARILI!")
                print("")
                cprint(Fore.GREEN, "Alınan Sonuç = İŞLEM BAŞARILI!")  
                print("")
                cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARILI!")
                print("\n") 
                time.sleep(1)
            else:     
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/admin-firma-bilgi.txt", "a") as file:
                    file.write(" " + "\n")
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Firma Profil sayfasının Bilgi Düzenle alanının BAŞARILI testi!")
                    file.write(" " + "\n")
                    file.write("Firmann Adı : " + frm_adi[i])
                    file.write(" " + "\n")
                    file.write("Firmamom Kullanıcı Adı : " + frm_kadi[i])
                    file.write(" " + "\n")
                    file.write("Girilen Açıklama Bilgisi : " + bilgi_text[i])
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: İŞLEM BAŞARILI!")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: İŞLEM BAŞARISIZ!")
                    file.write(" " + "\n\n")
                    file.write("TEST BAŞARISIZ!") 
                    file.write(" " + "\n\n")
                             
                cprint(Fore.YELLOW, "Test Çalıştırma Tarih/Saat'i : " + str(d))
                print("") 
                cprint(Fore.LIGHTBLUE_EX, "Firmanın Adı : " + frm_adi[i])
                cprint(Fore.LIGHTBLUE_EX, "Firmanın Kullanıcı Adı : " + frm_kadi[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Açıklama Bilgisi : " + bilgi_text[i])
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç = İŞLEM BAŞARILI!")
                print("")
                cprint(Fore.RED, "Alınan Sonuç = İŞLEM BAŞARISIZ!")  
                print("")
                cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARISIZ!")
                print("\n") 
                time.sleep(1)
        cprint(Fore.YELLOW, "Çıkmak için 'e' başarısız test için 'b' tuşlayın")
        a = input()
        if a == 'e':
            driver.close()
        elif a == 'b':
            self.driver.find_element_by_id("show_info").click()
            time.sleep(1)
            self.b_isim = self.driver.find_element_by_id(self.degerler["bilgiler_isim"])
            self.b_gad = self.driver.find_element_by_id(self.degerler["bilgiler_giris_adi"])
            self.b_gbtn = self.driver.find_element_by_id(self.degerler["bilgiler_btn"])
            self.b_text = self.driver.find_element_by_id(self.degerler["bilgiler_text"])
            time.sleep(2)
            admin_firma_bilgi.basarisiz(["", ""], ["", ""], ["", ""])

driver = webdriver.Chrome("C:\\xampp\\chromedriver.exe")

admin_firma_bilgi = admin_firma_bilgi(driver, "http://localhost/admin", "http://localhost/firmalar", {"bilgiler_isim": "bilgiler_isim", "bilgiler_giris_adi": "bilgiler_giris_adi", "bilgiler_btn": "bilgiler_btn", "bilgiler_text": "bilgiler_text"})

print(Fore.YELLOW + "Başarısız test içi 1, başarılı test için 2")
test = int(input())

print(" ")

if test == 1:
    print(Fore.YELLOW + "Çalıştırılan test: " + "admin_firma_bilgi, basarisiz_test", end="\n\n")  
    admin_firma_bilgi.basarisiz(["", ""], ["", ""], ["", ""])


elif test == 2:
    print(Fore.YELLOW + "Çalıştırılan test: " + "admin_firma_bilgi, basarili_test", end="\n\n")
    admin_firma_bilgi.basarili(["Vestel"], ["vestel_deneme"], ["Testaciklamadeneme"])
    print("")