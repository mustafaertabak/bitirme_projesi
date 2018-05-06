# Bu kısımda gerekli importları yaptık
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

class firma_ilan:
  # Alttaki sınıfların miras alabilmeleri için init şeklinde def tanımladık ve bu defin içine ihtiyacımız olan değerleri aldık
    def __init__(self, driver, url, url2, dizi, k_ad, k_sif):
        db = MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "", db = "deustaj", use_unicode=True, charset="utf8")
        self.cursor = db.cursor()
        self.cursor.execute("SELECT * FROM ilanlar")

        # Değer atamalarını yaptık 
        self.driver = driver
        self.url2 = url2
        self.url = url
        self.driver.get(self.url)
        # Degerleri birden fazla göndereceğimiz için dizi şeklinde atadık 
        self.degerler = dizi    
        # Diziden gelen değerler ile eşleşen input idlerini bulduk ve değişkenlere atadık
        self.el_id = self.driver.find_element_by_id("username")
        self.el_pas = self.driver.find_element_by_id("pass")
        self.sb_btn = self.driver.find_element_by_id("submit_button")
        
        self.el_id.send_keys(k_ad)
        self.el_pas.send_keys(k_sif)
        self.sb_btn.click()
        time.sleep(1)
        self.driver.get(self.url2)
        self.driver.find_element_by_id("ilani_ekle").click()

        self.ilan_kisi = self.driver.find_element_by_id(self.degerler["ilan_kisi"])
        self.ilan_baslik = self.driver.find_element_by_id(self.degerler["ilan_baslik"])
        self.ilan_mail = self.driver.find_element_by_id(self.degerler["ilan_mail"])
        self.ilan_adres = self.driver.find_element_by_id(self.degerler["ilanlar_adres"])
        self.ilan_text = self.driver.find_element_by_id(self.degerler["ilanlar_text"])  
        self.buton = self.driver.find_element_by_id(self.degerler["ilan_gonder"])
        
        time.sleep(1)

    def basarili(self, ilan_baslik, ilan_mail, ilan_adres, ilan_text, ilan_kisi):
        db2 = MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "", db = "deustaj", use_unicode=True, charset="utf8")
        cursor2 = db2.cursor()
        
        for i in range(len(ilan_baslik)): 
            self.ilan_baslik.clear()
            self.ilan_mail.clear()
            self.ilan_text.clear()
            self.ilan_adres.clear()
            
            self.ilan_baslik.send_keys(ilan_baslik[i])
            self.ilan_mail.send_keys(ilan_mail[i])
            self.ilan_kisi.send_keys(ilan_kisi[i])
            self.drop = self.driver.find_element_by_id("bolum_btn").click()       
            time.sleep(1.5)
            self.driver.find_element_by_xpath("//label[@for='r_id_c_b_1']").click()
            time.sleep(1)
            self.drop_donem = self.driver.find_element_by_id("donem_btn").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//label[@for='r_id_c_d_1']").click()
            
            self.value_donem = self.driver.find_element_by_id("donem_btn").text
            self.vlue = self.driver.find_element_by_id("bolum_btn").text
            self.ilan_adres.send_keys(ilan_adres[i])
            self.ilan_text.send_keys(ilan_text[i])
            
            self.buton.click()
            time.sleep(1.5)

            self.btn_scs = self.driver.find_element_by_class_name("btn-success").click()
            time.sleep(2)
            db2.commit()
            time.sleep(2)
           
            #self.query = cursor.execute("SELECT bolum_id FROM bolumler WHERE bolum_isim = '%s'" % (self.text_id))

            #cursor.execute("SELECT * FROM ilanlar WHERE ilan_baslik = '%s' AND ilan_aciklama = '%s' AND ilan_basvuru_mail = '%s' AND ilan_is_adres = '%s' AND ilan_bolumid = '%s'"  % (ilan_baslik[i], ilan_text[i], ilan_mail[i], ilan_adres[i], self.query))

            #cursor2.execute("SELECT * FROM bolumler INNER JOIN ilanlar ON bolumler.bolum_id = ilanlar.ilan_bolumid WHERE ilanlar.ilan_baslik = '%s' AND ilanlar.ilan_aciklama = '%s' AND ilanlar.ilan_basvuru_mail = '%s' AND ilanlar.ilan_is_adres = '%s' AND ilanlar.ilan_bolumid = bolumler.bolum_id"  %  (ilan_baslik[i], ilan_text[i], ilan_mail[i], ilan_adres[i]))
            cursor2.execute("SELECT * FROM ilanlar")
    
            if cursor2.rowcount > self.cursor.rowcount:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/firma-ilan-ekle.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarılı İlan Ekleme Testi")
                    file.write(" " + "\n")
                    file.write("Girilen ilan Başlığı : " + ilan_baslik[i])
                    file.write(" " + "\n")
                    file.write("Girilen Firma E-Mail : " + ilan_mail[i])
                    file.write(" " + "\n")
                    file.write("Seçilen Bölüm Adı : " + self.vlue)
                    file.write(" " + "\n")
                    file.write("Seçilen Staj Dönemi : " + self.value_donem)
                    file.write(" " + "\n")
                    file.write(" " + "\n")
                    file.write("Girilen Kontenjan Sayısı : " + ilan_kisi[i])
                    file.write(" " + "\n")
                    file.write("Girilen ilan Adresi : " + ilan_adres[i])
                    file.write(" " + "\n")
                    file.write("Girilen Açıklama Bilgisi : " + ilan_text[i])
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: Başarılı")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: Başarılı")
                    file.write(" " + "\n\n")
                    file.write("TEST BAŞARILI!")
                    file.write(" " + "\n\n")
                cprint(Fore.YELLOW, "Test Çalıştırılma Tarih/Saat'i : " + str(d))
                print("")   
                cprint(Fore.LIGHTBLUE_EX, "Girilen İlan Başlığı : " + ilan_baslik[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Firma E-mail : " + ilan_mail[i])
                cprint(Fore.LIGHTBLUE_EX, "Seçilen Bolum Adı : " + self.vlue)
                cprint(Fore.LIGHTBLUE_EX, "Seçilen Staj Dönemi : " + self.value_donem)
                print("")
                cprint(Fore.LIGHTBLUE_EX, "Girilen Kontenjan Sayısı : " + ilan_kisi[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen İlan Adresi : " + ilan_adres[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Açıklama Bilgisi : " + ilan_text[i])
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç = İŞLEM BAŞARILI!")
                print("")
                cprint(Fore.GREEN, "Alınan Sonuç = İŞLEM BAŞARILI!")
                print("\n")
                cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARILI!")
                print("\n") 
                time.sleep(1)
            else:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/firma-ilan-ekle.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarılı İlan Ekleme Testi")
                    file.write(" " + "\n")
                    file.write("Girilen ilan Başlığı : " + ilan_baslik[i])
                    file.write(" " + "\n")
                    file.write("Girilen Firma E-Mail : " + ilan_mail[i])
                    file.write(" " + "\n")
                    file.write("Seçilen Bölüm Adı : " + self.vlue)
                    file.write(" " + "\n")
                    file.write("Girilen ilan Adresi : " + ilan_adres[i])
                    file.write(" " + "\n")
                    file.write("Girilen Açıklama Bilgisi : " + ilan_text[i])
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: BAŞARILI!")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: BAŞARISIZ!")
                    file.write(" " + "\n\n")
                cprint(Fore.YELLOW, "Test Çalıştırılma Tarih/Saat'i : " + str(d))
                print("")   
                cprint(Fore.LIGHTBLUE_EX, "Girilen İlan Başlığı : " + ilan_baslik[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Firma E-mail : " + ilan_mail[i])
                cprint(Fore.LIGHTBLUE_EX, "Seçilen Bolum Adı : " + self.vlue)
                cprint(Fore.LIGHTBLUE_EX, "Girilen İlan Adresi : " + ilan_adres[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Açıklama Bilgisi : " + ilan_text[i])
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç = İŞLEM BAŞARILI!")
                print("")
                cprint(Fore.RED, "Alınan Sonuç = İŞLEM BAŞARISIZ!") 
                print("\n")
                cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARISIZ!") 
                print("\n") 
                time.sleep(2)
        cprint(Fore.YELLOW, "Çıkmak için 'e' başarısız test için 'b' tuşlayın")
        a = input()
        if a == 'e':
            driver.close()
        elif a == 'b':
            self.driver.find_element_by_id("ilani_ekle").click()
            time.sleep(2)
            self.ilan_baslik = self.driver.find_element_by_id(self.degerler["ilan_baslik"])
            self.ilan_mail = self.driver.find_element_by_id(self.degerler["ilan_mail"])
            self.ilan_adres = self.driver.find_element_by_id(self.degerler["ilanlar_adres"])
            self.ilan_text = self.driver.find_element_by_id(self.degerler["ilanlar_text"])  
            self.ilan_kisi = self.driver.find_element_by_id(self.degerler["ilan_kisi"])
            self.buton = self.driver.find_element_by_id(self.degerler["ilan_gonder"])
            time.sleep(2)
            firma_ilan.basarisiz(["bilgisayar", "makine"], ["5656", "6565"], ["adress", "adress2"], ["ac", "ac2"], ["asdas", "9"])

    def basarisiz(self, ilan_baslik, ilan_mail, ilan_adres, ilan_text, ilan_kisi):
        db2 = MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "", db = "deustaj", use_unicode=True, charset="utf8")
        cursor = db2.cursor()
        cursor2 = db2.cursor()
        cursor2.execute("SELECT * FROM ilanlar")

        for i in range(len(ilan_baslik)):
             
            self.ilan_baslik.clear()
            self.ilan_mail.clear()
            self.ilan_text.clear()
            self.ilan_adres.clear()
            self.ilan_kisi.clear()

            self.ilan_baslik.send_keys(ilan_baslik[i])
            self.ilan_mail.send_keys(ilan_mail[i])
            self.ilan_kisi.send_keys(ilan_kisi[i])
            self.drop = self.driver.find_element_by_id("bolum_btn").click()       
            time.sleep(1.5)
            self.driver.find_element_by_xpath("//label[@for='r_id_c_b_1']").click()
            time.sleep(1)
            self.drop_donem = self.driver.find_element_by_id("donem_btn").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//label[@for='r_id_c_d_1']").click()
            
            self.value_donem = self.driver.find_element_by_id("donem_btn").text
            self.vlue = self.driver.find_element_by_id("bolum_btn").text
            self.ilan_adres.send_keys(ilan_adres[i])
            self.ilan_text.send_keys(ilan_text[i])
            
            self.buton.click()
            time.sleep(1.5)
            self.btn_scs = self.driver.find_element_by_class_name("btn-success").is_displayed()
            time.sleep(2)
            db2.commit()
            time.sleep(2)
            cursor.execute("SELECT * FROM ilanlar")

            #cursor.execute("SELECT * FROM bolumler INNER JOIN ilanlar ON bolumler.bolum_id = ilanlar.ilan_bolumid WHERE ilanlar.ilan_baslik = '%s' AND ilanlar.ilan_aciklama = '%s' AND ilanlar.ilan_basvuru_mail = '%s' AND ilanlar.ilan_is_adres = '%s' AND ilanlar.ilan_bolumid = bolumler.bolum_id"  %  (ilan_baslik[i], ilan_text[i], ilan_mail[i], ilan_adres[i]))

            if cursor2.rowcount == cursor.rowcount:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/firma-ilan-ekle.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarısız şifre testi")
                    file.write(" " + "\n")
                    file.write("Girilen ilan Başlığı : " + ilan_baslik[i])
                    file.write(" " + "\n")
                    file.write("Girilen Firma E-Mail : " + ilan_mail[i])
                    file.write(" " + "\n")
                    file.write("Seçilen Bölüm Adı : " + self.vlue)
                    file.write(" " + "\n")
                    file.write("Seçilen Staj Dönemi : " + self.value_donem)
                    file.write(" " + "\n")
                    file.write("Girilen ilan Adresi : " + ilan_adres[i])
                    file.write(" " + "\n")
                    file.write("Girilen Kontenjan Sayısı : " + ilan_kisi[i])
                    file.write(" " + "\n")
                    file.write("Girilen Açıklama Bilgisi : " + ilan_text[i])
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: İŞLEM BAŞARISIZ!")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: İŞLEM BAŞARISIZ!")
                    file.write(" " + "\n\n")
                    file.write("TEST BAŞARILI!")
                    file.write(" " + "\n\n")
                cprint(Fore.LIGHTMAGENTA_EX, "GİRİŞ - " + str(i+1))   
                print("")
                cprint(Fore.YELLOW, "Test Çalıştırılma Tarih/Saat'i : " + str(d))
                print("")
                cprint(Fore.LIGHTBLUE_EX, "Girilen İlan Başlığı : " + ilan_baslik[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Firma E-mail : " + ilan_mail[i])
                cprint(Fore.LIGHTBLUE_EX, "Seçilen Bolum Adı : " + self.vlue)
                cprint(Fore.LIGHTBLUE_EX, "Seçilen Staj Dönemi : " + self.value_donem)
                print("")
                cprint(Fore.LIGHTBLUE_EX, "Girilen Kontenjan Sayısı : " + ilan_kisi[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen İlan Adresi : " + ilan_adres[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Açıklama Bilgisi : " + ilan_text[i])
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç = İŞLEM BAŞARISIZ!")
                print("")
                cprint(Fore.GREEN, "Alınan Sonuç = İŞLEM BAŞARISIZ!")  
                print("\n")
                cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARILI!") 
                print("\n") 
                time.sleep(1)
            else:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/firma-ilan-ekle.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarısız ilan ekleme testi")
                    file.write(" " + "\n")
                    file.write("Girilen ilan Başlığı : " + ilan_baslik[i])
                    file.write(" " + "\n")
                    file.write("Girilen Firma E-Mail : " + ilan_mail[i])
                    file.write(" " + "\n")
                    file.write("Seçilen Bölüm Adı : " + self.vlue)
                    file.write(" " + "\n")
                    file.write("Girilen ilan Adresi : " + ilan_adres[i])
                    file.write(" " + "\n")
                    file.write("Girilen Açıklama Bilgisi : " + ilan_text[i])
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: İŞLEM BAŞARISIZ!")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: İŞLEM BAŞARILI")
                    file.write(" " + "\n\n")
                    file.write("TEST BAŞARISIZ!")
                    file.write(" " + "\n\n")
                cprint(Fore.LIGHTMAGENTA_EX, "GİRİŞ - " + str(i+1))   
                print("")
                cprint(Fore.YELLOW, "Test Çalıştırılma Tarih/Saat'i : " + str(d))
                print("")
                cprint(Fore.LIGHTBLUE_EX, "Girilen İlan Başlığı : " + ilan_baslik[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Firma E-mail : " + ilan_mail[i])
                cprint(Fore.LIGHTBLUE_EX, "Seçilen Bolum Adı : " + self.vlue)
                cprint(Fore.LIGHTBLUE_EX, "Girilen İlan Adresi : " + ilan_adres[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Açıklama Bilgisi : " + ilan_text[i])
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç = İŞLEM BAŞARISIZ!")
                print("")
                cprint(Fore.RED, "Alınan Sonuç = İŞLEM BAŞARILI!") 
                print("\n")
                cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARISIZ!")  
                print("\n") 
                time.sleep(1)
        cprint(Fore.YELLOW, "Çıkmak için 'e' başarılı test için 'b' tuşlayın")
        a = input()
        if a == 'e':
            driver.close()
        elif a == 'b':
            time.sleep(2)

            self.ilan_baslik.clear()
            self.ilan_mail.clear()
            self.ilan_text.clear()
            self.ilan_adres.clear()
            self.ilan_kisi.clear()

            self.ilan_baslik = self.driver.find_element_by_id(self.degerler["ilan_baslik"])
            self.ilan_mail = self.driver.find_element_by_id(self.degerler["ilan_mail"])
            self.ilan_adres = self.driver.find_element_by_id(self.degerler["ilanlar_adres"])
            self.ilan_text = self.driver.find_element_by_id(self.degerler["ilanlar_text"])  
            self.buton = self.driver.find_element_by_id(self.degerler["ilan_gonder"])
            self.ilan_kisi = self.driver.find_element_by_id(self.degerler["ilan_kisi"])
            time.sleep(2)
            firma_ilan.basarili(["makine"], ["berkeertan@gmail.com"], ["adres"], ["aciklama"], ["2"])
                  
driver = webdriver.Chrome("C:\\xampp\\chromedriver.exe")


print(Fore.CYAN + "Kullanıcı adı gir") 
kullanici_adi = input()
print(Fore.CYAN + "Sifre gir")
sifre = input()

firma_ilan = firma_ilan(driver, "http://localhost:100/firma-giris", "http://localhost:100/profil", {"ilan_baslik": "ilan_baslik", "ilan_mail": "ilan_mail", "ilanlar_adres": "ilanlar_adres", "ilanlar_text": "ilanlar_text", "ilan_gonder": "ilan_gonder", "ilan_kisi": "ilanlar_kisi"}, kullanici_adi, sifre)

print(Fore.YELLOW + "Başarısız test için 1, başarılı test için 2") 
test = int(input())
print(" ")

# 1'e basılırsa yapılacak işlemler 
if test == 1:
    print(Fore.YELLOW + "Çalıştırılan test: " + "Firma ilan ekle, basarisiz_test", end="\n\n")
    print("")
    # Firma_giris sınıfının içindeki basarisiz define degerleri gönderiyoruz 
    firma_ilan.basarisiz(["bilgisayar", "makine"], ["5656", "6565"], ["adress", "adress2"], ["ac", "ac2"], ["asdasda", "9"])

# 2'ye basılırsa yapılacak işlemler 
if test == 2:
    print(Fore.YELLOW + "Çalıştırılan test: " + "Firma ilan ekle, basarili_test", end="\n\n") 
    # Firma_giris sınıfının içindeki basarili define degerleri gönderiyoruz 
    firma_ilan.basarili(["makine"], ["berkeertan@gmail.com"], ["adres"], ["aciklama"], ["2"])