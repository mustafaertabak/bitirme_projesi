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

colorama.init()
def cprint(color, text):
    print(color + text)

class firma_ilan_duzenle:

    def __init__(self, driver, url, url2, dizi, k_ad,k_sif):
        self.driver = driver
        self.url = url
        self.url2 = url2
        self.driver.get(self.url)

        self.degerler = dizi  

        self.u_name = self.driver.find_element_by_id("username")
        self.u_pass = self.driver.find_element_by_id("pass")
        self.g_btn = self.driver.find_element_by_id("submit_button")

        self.u_name.send_keys(k_ad)
        self.u_pass.send_keys(k_sif)
        self.g_btn.click()
        time.sleep(1)
        self.driver.get(self.url2)
        self.driver.find_element_by_id("ilanduzenle_btn").click()
        time.sleep(0.5)

        self.driver.find_element_by_id("ilan_duzenle").click()
        time.sleep(0.5)

        self.ilan_baslik = self.driver.find_element_by_id(self.degerler["ilan_baslik"])
        self.ilan_mail = self.driver.find_element_by_id(self.degerler["ilan_mail"])
        self.ilan_text = self.driver.find_element_by_id(self.degerler["ilanlar_text"])
        self.ilan_adres = self.driver.find_element_by_id(self.degerler["ilanlar_adres"])
        self.buton = self.driver.find_element_by_id(self.degerler["ilan_gonder"])
    
    def basarili(self, ilan_baslik, ilan_mail, ilan_text,ilan_adres):
        db = MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "", db = "deustaj", use_unicode=True, charset="utf8")
        cursor = db.cursor()

        for i in range(len(ilan_baslik)):
            self.ilan_baslik.clear()
            self.ilan_mail.clear()
            self.ilan_text.clear()
            self.ilan_adres.clear()

            self.ilan_baslik.send_keys(ilan_baslik[i])
            self.ilan_mail.send_keys(ilan_mail[i])
            self.ilan_adres.send_keys(ilan_adres[i])
            self.drop = self.driver.find_element_by_id("drop_id2").click()
            time.sleep(1.5)

            self.driver.find_element_by_xpath("//label[@for='r_id_c_b_u_1']").click()
            time.sleep(1)  
            self.vlue = self.driver.find_element_by_id("chk_bolumler_u").text    

            self.ilan_text.send_keys(ilan_text[i])
            self.buton.click()
            time.sleep(1)
            self.btn_sccs = self.driver.find_element_by_class_name("btn-success").click()
            time.sleep(1)

            cursor.execute("SELECT * FROM bolumler INNER JOIN ilanlar ON bolumler.bolum_id = ilanlar.ilan_bolumid WHERE ilanlar.ilan_baslik = '%s' AND ilanlar.ilan_aciklama = '%s' AND ilanlar.ilan_basvuru_mail = '%s' AND ilanlar.ilan_is_adres = '%s' AND ilanlar.ilan_bolumid = bolumler.bolum_id"  %  (ilan_baslik[i], ilan_text[i], ilan_mail[i], ilan_adres[i]))

            if cursor.rowcount > 0:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/firma-ilan-duzenle.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarılı İlan Güncelleme Testi")
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: BAŞARILI!")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: BAŞARILI!")
                    file.write(" " + "\n\n")
                cprint(Fore.LIGHTBLUE_EX, "Girilen İlan Başlığı : " + ilan_baslik[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Firma E-mail : " + ilan_mail[i])
                cprint(Fore.LIGHTBLUE_EX, "Seçilen Bolum Adı : " + self.vlue)
                cprint(Fore.LIGHTBLUE_EX, "Girilen İlan Adresi : " + ilan_adres[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Açıklama Bilgisi : " + ilan_text[i])
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç = İŞLEM BAŞARILI!")
                print("")
                cprint(Fore.GREEN, "Alınan Sonuç = İŞLEM BAŞARILI!")  
                print("\n") 
                time.sleep(1)
            else:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/firma-ilan-duzenle.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarılı şifre testi")
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: BAŞARILI!")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: BAŞARISIZ!")
                    file.write(" " + "\n\n")
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
                time.sleep(1)
        cprint(Fore.YELLOW, "Çıkmak için 'e' başarısız test için 'b' tuşlayın")
        a = input()
        if a == 'e':
            driver.close()
        elif a == 'b':
            self.driver.find_element_by_id("ilanduzenle_btn").click()
            time.sleep(1.5)
            self.driver.find_element_by_id("ilan_duzenli")
            time.sleep(2)
            self.ilan_baslik = self.driver.find_element_by_id(self.degerler["ilan_baslik"])
            self.ilan_mail = self.driver.find_element_by_id(self.degerler["ilan_mail"])
            self.ilan_text = self.driver.find_element_by_id(self.degerler["ilanlar_text"])
            self.ilan_adres = self.driver.find_element_by_id(self.degerler["ilanlar_adres"])
            self.buton = self.driver.find_element_by_id(self.degerler["ilan_gonder"])
            time.sleep(2)
            firma_ilan_duzenle.basarisiz(["bilgisayar", "makine"], ["5656", "6565"], ["ac", "ac2"], ["adress", "adress2"])
    
    def basarisiz(self, ilan_baslik, ilan_mail, ilan_text, ilan_adres):
        db = MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "", db = "deustaj", use_unicode=True, charset="utf8")
        cursor = db.cursor()

        for i in range(len(ilan_baslik)):
            self.ilan_baslik.clear()
            self.ilan_mail.clear()
            self.ilan_text.clear()
            self.ilan_adres.clear()

            self.ilan_baslik.send_keys(ilan_baslik[i])
            self.ilan_mail.send_keys(ilan_mail[i])
            self.ilan_adres.send_keys(ilan_adres[i])
            self.ilan_text.send_keys(ilan_text[i])
            self.buton.click()
            time.sleep(1)

            self.btn_scs = self.driver.find_element_by_class_name("btn-success").is_displayed()

            cursor.execute("SELECT * FROM bolumler INNER JOIN ilanlar ON bolumler.bolum_id = ilanlar.ilan_bolumid WHERE ilanlar.ilan_baslik = '%s' AND ilanlar.ilan_aciklama = '%s' AND ilanlar.ilan_basvuru_mail = '%s' AND ilanlar.ilan_is_adres = '%s' AND ilanlar.ilan_bolumid = bolumler.bolum_id"  %  (ilan_baslik[i], ilan_text[i], ilan_mail[i], ilan_adres[i]))

            if cursor.rowcount > 0:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/firma-ilan-duzenle.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarısız İlan Duzenleme Testi")
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: BAŞARISIZ")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: BAŞARILI!")
                    file.write(" " + "\n\n")
                cprint(Fore.LIGHTMAGENTA_EX, "GİRİŞ - " + str(i+1))   
                print("")
                cprint(Fore.LIGHTBLUE_EX, "Girilen İlan Başlığı : " + ilan_baslik[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Firma E-mail : " + ilan_mail[i])
                cprint(Fore.LIGHTBLUE_EX, "Seçilen Bolum Adı : ")
                cprint(Fore.LIGHTBLUE_EX, "Girilen İlan Adresi : " + ilan_adres[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Açıklama Bilgisi : " + ilan_text[i])
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç = İŞLEM BAŞARISIZ!")
                print("")
                cprint(Fore.RED, "Alınan Sonuç = İŞLEM BAŞARILI!")  
                print("\n") 
                time.sleep(1)

            else:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/firma-ilan-ekle.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarısız İlan Duzenleme Testi")
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: Başarısız")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: Başarısız")
                    file.write(" " + "\n\n")
                cprint(Fore.LIGHTMAGENTA_EX, "GİRİŞ - " + str(i+1))   
                print("")
                cprint(Fore.LIGHTBLUE_EX, "Girilen İlan Başlığı : " + ilan_baslik[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Firma E-mail : " + ilan_mail[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen İlan Adresi : " + ilan_adres[i])
                cprint(Fore.LIGHTBLUE_EX, "Girilen Açıklama Bilgisi : " + ilan_text[i])
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç = İŞLEM BAŞARISIZ!")
                print("")
                cprint(Fore.GREEN, "Alınan Sonuç = İŞLEM BAŞARISIZ!")  
                print("\n") 
                time.sleep(1)
        cprint(Fore.YELLOW, "Çıkmak için 'e' başarılı test için 'b' tuşlayın")
        a = input()
        if a == 'e':
            driver.close()
        elif a == 'b':
            self.driver.find_element_by_id("ilanduzenle_btn").click()
            time.sleep(1.5)
            self.driver.find_element_by_id("ilan_duzenle")
            time.sleep(2)
            self.ilan_baslik = self.driver.find_element_by_id(self.degerler["ilan_baslik"])
            self.ilan_mail = self.driver.find_element_by_id(self.degerler["ilan_mail"])
            self.ilan_text = self.driver.find_element_by_id(self.degerler["ilanlar_text"])
            self.ilan_adres = self.driver.find_element_by_id(self.degerler["ilanlar_adres"])
            self.buton = self.driver.find_element_by_id(self.degerler["ilan_gonder"])
            time.sleep(2)
            firma_ilan_duzenle.basarili(["Bilgisayar"], ["mustafa@hotmail.com"], ["aciklamaDENEME"], ["adresDENEME"])

driver = webdriver.Chrome("C:\\xampp\\chromedriver.exe")

print(Fore.CYAN + "Kullanıcı adı gir") 
kullanici_adi = input()
print(Fore.CYAN + "Sifre gir")
sifre = input()

firma_ilan_duzenle = firma_ilan_duzenle(driver, "http://localhost/firma-giris", "http://localhost/profil", {"ilan_baslik": "ilan_baslik_u", "ilan_mail": "ilan_mail_u", "ilanlar_text": "ilanlar_text_u", "ilanlar_adres": "ilanlar_adres_u", "ilan_gonder": "ilan_gonder_u"}, kullanici_adi, sifre) 

print(Fore.YELLOW + "Başarısız test için 1, başarılı test için 2") 
test = int(input())
print(" ")


if test == 1:
    print(Fore.YELLOW + "Çalıştırılan test: " + "Firma ilan düzenle, basarisiz_test", end="\n\n")
    print("")

    firma_ilan_duzenle.basarisiz(["bilgisayar", "makine"], ["5656", "6565"], ["ac", "ac2"], ["adress", "adress2"])


if test == 2:
    print(Fore.YELLOW + "Çalıştırılan test: " + "Firma ilan düzenle, basarili_test", end="\n\n") 
    
    firma_ilan_duzenle.basarili(["Bilgisayar"], ["mustafa@hotmail.com"], ["aciklamaDENEME"], ["adresDENEME"])












