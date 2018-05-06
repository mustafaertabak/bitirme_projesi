# Gerekli importları bu kısımda yapıyoruz 
from selenium import webdriver
import MySQLdb
import hashlib
from hashlib import md5
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

class e_mail:

    def __init__(self, driver, url, url2, dizi):
        self.degerler = dizi 
        self.driver = driver 
        self.kayit_url = url2 
        self.url = url 
        self.driver.get(self.url)
        self.k_id = self.driver.find_element_by_id("username")
        self.k_p = self.driver.find_element_by_id("pass")
        self.k_id.send_keys("7040000001")
        self.k_p.send_keys("123456")
        self.driver.find_element_by_id("submit_button").click()
        time.sleep(2)
        self.driver.get(self.kayit_url)
        self.e_mail = self.driver.find_element_by_id(self.degerler["mail"])

    def basarili(self, mail, firma_isim, firma_giris_adi, firma_sifre_a, firma_sifre_b):
        db = MySQLdb.connect(host= "127.0.0.1", user = "root", passwd = "", db= "deustaj", use_unicode=True, charset="utf8")
        cursor = db.cursor()
        cursor_firma_kod = db.cursor()
        firma_before_insert = db.cursor()
        firma_after_insert = db.cursor()
        firma_before_insert.execute("SELECT * FROM firmalar")

        self.app_btn = self.driver.find_element_by_id("f_basvuru_btn")
        self.e_mail.send_keys(mail)
        self.app_btn.click()
        self.driver.find_element_by_class_name("btn-success").click()
        db.commit()
        time.sleep(5)
        self.togg = self.driver.find_element_by_class_name("navbar-toggler").is_displayed()
        if self.togg:
            self.driver.find_element_by_class_name("navbar-toggler").click()
            time.sleep(1.5)
            self.driver.find_element_by_xpath("//button[@data-toggle='dropdown']").click()
            self.driver.find_element_by_class_name("border-bottom-0").click()
        else:
            time.sleep(2)
            self.driver.find_element_by_xpath("//button[@data-toggle='dropdown']").click()
            self.driver.find_element_by_class_name("border-bottom-0").click()


        cursor.execute("SELECT f_basvuru_url FROM f_basvurular WHERE f_basvuru_id = (SELECT MAX(f_basvuru_id) FROM f_basvurular)")
        time.sleep(2)
        result = cursor.fetchall()
        for i in result:
            self.driver.get("http://localhost/firma-kayit$url=" + i[0])
            time.sleep(2)

        cursor_firma_kod.execute("SELECT f_basvuru_kod FROM f_basvurular WHERE f_basvuru_url = '%s'" % (i[0]))
        result_kod = cursor_firma_kod.fetchall()
        db.commit()

        for y in result_kod:
            self.kod_input = self.driver.find_element_by_id("f_basvuru_onay")
            self.kod_input.send_keys(y[0])
            self.driver.find_element_by_id("f_basvuru_kod_btn").click()
            time.sleep(2)
        
        self.dizi = {"firma_isim_2": "firma_isim", "firma_giris_adi_2": "firma_giris_adi", "firma_sifre_a_2": "firma_sifre_a", "firma_sifre_b_2": "firma_sifre_b", "f_basvuru_tamamla_btn": "f_basvuru_tamamla_btn"}
        self.f_ad = self.driver.find_element_by_id(self.dizi["firma_isim_2"])
        self.k_ad = self.driver.find_element_by_id(self.dizi["firma_giris_adi_2"])
        self.pw = self.driver.find_element_by_id(self.dizi["firma_sifre_a_2"])
        self.pw_con = self.driver.find_element_by_id(self.dizi["firma_sifre_b_2"])
        self.submit_btn = self.driver.find_element_by_id(self.dizi["f_basvuru_tamamla_btn"])

        for i in range(len(firma_isim)):
            self.f_ad.send_keys(firma_isim[i])
            self.k_ad.send_keys(firma_giris_adi[i])
            self.pw.send_keys(firma_sifre_a[i])
            self.pw_con.send_keys(firma_sifre_b[i])
            self.submit_btn.click()
            
            time.sleep(3)
            firma_after_insert.execute("SELECT * FROM firmalar")
        
            if firma_after_insert.rowcount > firma_before_insert.rowcount:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/firma-email-hesap.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarılı firma kayıt testi")
                    file.write(" " + "\n")
                    file.write("Firma başvuru mail adresi alındı : " + mail[i])
                    file.write(" " + "\n")
                    file.write("Mail adresine kod gönderildi.")
                    file.write(" " + "\n")
                    file.write("Kod girişi test edildi ve firma kayıt işlemi tamamlandı.")
                    file.write(" " + "\n")
                    file.write("Oluşturulan firmanın adı : " + firma_isim[i])
                    file.write(" " + "\n")
                    file.write("Oluşturulan firmanın kullanıcı adı : " + firma_giris_adi[i])
                    file.write(" " + "\n")
                    file.write("Oluşturulan firmanın şifresi : " + firma_sifre_a[i])
                    file.write(" " + "\n")
                    file.write("Oluşturulan firmanın şifresi(TEKRAR) : " + firma_sifre_b[i])
                    file.write(" " + "\n")
                    file.write("Firma bilgileri alındı. Yeni firma oluşturma işlemi tamamlandı!")
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: İŞLEM BAŞARILI!")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: İŞLEM BAŞARILI!")
                    file.write(" " + "\n\n")
                    file.write("TEST BAŞARILI!")
                    file.write(" " + "\n\n")
                cprint(Fore.YELLOW, "Test Çalıştırma Tarih/Saat'i : " + str(d))
                print("")
                cprint(Fore.CYAN, "Yaplan Test : Başarılı firma kayıt testi.")
                cprint(Fore.LIGHTBLUE_EX, "Firma başvuru mail adresi alındı : " + mail[i])
                cprint(Fore.LIGHTBLUE_EX, "Mail Adresine kod gönderildi!")
                cprint(Fore.LIGHTBLUE_EX, "Kod giriş test edildi ve firma kayıt işlemi tamamlandı!")
                cprint(Fore.LIGHTBLUE_EX, "Oluşturulan firmanın adı : " + firma_isim[i])
                cprint(Fore.LIGHTBLUE_EX, "Oluşturulan firmanın kullanıcı adı : " + firma_giris_adi[i])
                cprint(Fore.LIGHTBLUE_EX, "Oluşturulan firmanın şifresi : " + firma_sifre_a[i])
                cprint(Fore.LIGHTBLUE_EX, "Oluşturulan firmanın şifresi(TEKRAR) : " + firma_sifre_b[i])
                print("")
                cprint(Fore.CYAN, "Firma bilgileri alındı. Yeni firma oluşturma işlemi tamamlandı!")
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç : İŞLEM BAŞARILI!")
                print("")
                cprint(Fore.GREEN, "Alınan Sonuç : İŞLEM BAŞARILI!")
                print("")
                cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARILI!")
                print("")
                time.sleep(0.5)
    
            else:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/firma-email-hesap.txt", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarılı firma kayıt testi")
                    file.write(" " + "\n")
                    file.write("Firma başvuru mail adresi alındı : " + mail[i])
                    file.write(" " + "\n")
                    file.write("Mail adresine kod gönderildi.")
                    file.write(" " + "\n")
                    file.write("Kod girişi test edildi ve firma kayıt işlemi tamamlandı.")
                    file.write(" " + "\n")
                    file.write("Oluşturulan firmanın adı : " + firma_isim[i])
                    file.write(" " + "\n")
                    file.write("Oluşturulan firmanın kullanıcı adı : " + firma_giris_adi[i])
                    file.write(" " + "\n")
                    file.write("Oluşturulan firmanın şifresi : " + firma_sifre_a[i])
                    file.write(" " + "\n")
                    file.write("Oluşturulan firmanın şifresi(TEKRAR) : " + firma_sifre_b[i])
                    file.write(" " + "\n")
                    file.write("Firma bilgilerinde bir hata oluştu! Lütfen Girilen Verileri Kontrol Edin!")
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: İŞLEM BAŞARILI!")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: İŞLEM BAŞARISIZ!")
                    file.write(" " + "\n\n")
                    file.write("TEST BAŞARISIZ!")
                    file.write(" " + "\n\n")
                cprint(Fore.YELLOW, "Test Çalıştırma Tarih/Saat'i : " + str(d))
                print("")
                cprint(Fore.CYAN, "Yaplan Test : Başarılı firma kayıt testi.")
                cprint(Fore.LIGHTBLUE_EX, "Firma başvuru mail adresi alındı : " + mail[i])
                cprint(Fore.LIGHTBLUE_EX, "Mail Adresine kod gönderildi!")
                cprint(Fore.LIGHTBLUE_EX, "Kod giriş test edildi ve firma kayıt işlemi tamamlandı!")
                cprint(Fore.LIGHTBLUE_EX, "Oluşturulan firmanın adı : " + firma_isim[i])
                cprint(Fore.LIGHTBLUE_EX, "Oluşturulan firmanın kullanıcı adı : " + firma_giris_adi[i])
                cprint(Fore.LIGHTBLUE_EX, "Oluşturulan firmanın şifresi : " + firma_sifre_a[i])
                cprint(Fore.LIGHTBLUE_EX, "Oluşturulan firmanın şifresi(TEKRAR) : " + firma_sifre_a[i])
                print("")
                cprint(Fore.CYAN, "Firma bilgilerinde bir hata oluştu! Lütfen Girilen Verileri Kontrol Edin!")
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç : İŞLEM BAŞARILI!")
                print("")
                cprint(Fore.RED, "Alınan Sonuç : İŞLEM BAŞARISIZ!")
                print("")
                cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARISIZ!")
                print("")
                time.sleep(0.5)
            
    def basarisiz(self, mail_2, firma_isim, firma_giris_adi, firma_sifre_a, firma_sifre_b):
        db = MySQLdb.connect(host= "127.0.0.1", user = "root", passwd = "", db= "deustaj", use_unicode=True, charset="utf8")
        cursor = db.cursor()
        count = 1
        cursor_firma_kod = db.cursor()
        cursor_record = db.cursor()
        
        self.app_btn = self.driver.find_element_by_id("f_basvuru_btn")

        for i in range(len(mail_2)):
            self.e_mail.clear()
            self.e_mail.send_keys(mail_2[i])
            time.sleep(1.5)
            self.app_btn.click()
            self.disp_ul = self.driver.find_element_by_id("f_basvuru_w").is_displayed()
            
                
            if self.disp_ul:
                d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("LOGS/firma-email-hesap", "a") as file:
                    file.write(" " + "\n")   
                    file.write(str(d))
                    file.write(" " + "\n")
                    file.write("Yapılan test: Başarısız firma kayıt testi")
                    file.write(" " + "\n")
                    file.write("Firma başvuru mail adresi alındı : "  +  mail_2[i])
                    file.write(" " + "\n")
                    file.write("Mail adresine kod gönderildi.")
                    file.write(" " + "\n")
                    file.write("Kod girişi test edildi ve firma kayıt işlemi tamamlandı.")
                    file.write(" " + "\n")
                    file.write("Oluşturulan firmanın adı : " + firma_isim[i])
                    file.write(" " + "\n")
                    file.write("Oluşturulan firmanın kullanıcı adı : " + firma_giris_adi[i])
                    file.write(" " + "\n")
                    file.write("Oluşturulan firmanın şifresi : " + firma_sifre_a[i])
                    file.write(" " + "\n")
                    file.write("Oluşturulan firmanın şifresi(TEKRAR) : " + firma_sifre_b[i])
                    file.write(" " + "\n")
                    file.write("Firma bilgilerinde bir hata oluştu! Lütfen Girilen Verileri Kontrol Edin!")
                    file.write(" " + "\n")
                    file.write("Beklenen sonuç: İŞLEM BAŞARISIZ!")
                    file.write(" " + "\n")
                    file.write("Alınan sonuç: İŞLEM BAŞARISIZ!")
                    file.write(" " + "\n\n")
                    file.write("TEST BAŞARILI!")
                    file.write(" " + "\n\n")
                cprint(Fore.YELLOW, "Test Çalıştırma Tarih/Saat'i : " + str(d))
                print("")
                cprint(Fore.CYAN, "Yaplan Test : Başarısız firma kayıt testi.")
                cprint(Fore.LIGHTBLUE_EX, "Firma başvuru mail adresi alındı : "  +  mail_2[i])
                cprint(Fore.LIGHTBLUE_EX, "Mail Adresine kod gönderildi!")
                cprint(Fore.LIGHTBLUE_EX, "Kod giriş test edildi ve firma kayıt işlemi tamamlandı!")
                cprint(Fore.LIGHTBLUE_EX, "Oluşturulan firmanın adı : " + firma_isim[i])
                cprint(Fore.LIGHTBLUE_EX, "Oluşturulan firmanın kullanıcı adı : " + firma_giris_adi[i])
                cprint(Fore.LIGHTBLUE_EX, "Oluşturulan firmanın şifresi : " + firma_sifre_a[i])
                cprint(Fore.LIGHTBLUE_EX, "Oluşturulan firmanın şifresi(TEKRAR) : " + firma_sifre_b[i])
                print("")
                cprint(Fore.CYAN, "Firma bilgilerinde bir hata oluştu! Lütfen Girilen Verileri Kontrol Edin!")
                print("")
                cprint(Fore.YELLOW, "Beklenen Sonuç : İŞLEM BAŞARISIZ!")
                print("")
                cprint(Fore.GREEN, "Alınan Sonuç : İŞLEM BAŞARISIZ!")
                print("")
                cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARILI!")
                print("")
                time.sleep(0.5)
            else:
                self.driver.find_element_by_class_name("btn-success").click()
                db.commit()
                time.sleep(6)
                self.togg = self.driver.find_element_by_class_name("navbar-toggler").is_displayed()
                if self.togg:
                    self.driver.find_element_by_class_name("navbar-toggler").click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath("//button[@data-toggle='dropdown']").click()
                    self.driver.find_element_by_class_name("border-bottom-0").click()
                    time.sleep(4)
                else:
                    self.driver.find_element_by_xpath("//button[@data-toggle='dropdown']").click()
                    self.driver.find_element_by_class_name("border-bottom-0").click()
                    time.sleep(2)
        
                cursor.execute("SELECT f_basvuru_url FROM f_basvurular WHERE f_basvuru_id = (SELECT MAX(f_basvuru_id) FROM f_basvurular)")
                time.sleep(2)
                result = cursor.fetchall()

                for i in result:
                    self.driver.get("http://localhost/firma-kayit$url=" + i[0])
                    time.sleep(2)

                cursor_firma_kod.execute("SELECT f_basvuru_kod FROM f_basvurular WHERE f_basvuru_url = '%s'" % (i[0]))
                result_kod = cursor_firma_kod.fetchall()
                db.commit()

                for y in result_kod:
                    self.kod_input = self.driver.find_element_by_id("f_basvuru_onay")
                    self.kod_input.send_keys(y[0])
                    self.driver.find_element_by_id("f_basvuru_kod_btn").click()
                    time.sleep(2)

                self.dizi = {"firma_isim_2": "firma_isim", "firma_giris_adi_2": "firma_giris_adi", "firma_sifre_a_2": "firma_sifre_a", "firma_sifre_b_2": "firma_sifre_b", "f_basvuru_tamamla_btn": "f_basvuru_tamamla_btn"}
                self.f_ad = self.driver.find_element_by_id(self.dizi["firma_isim_2"])
                self.k_ad = self.driver.find_element_by_id(self.dizi["firma_giris_adi_2"])
                self.pw = self.driver.find_element_by_id(self.dizi["firma_sifre_a_2"])
                self.pw_con = self.driver.find_element_by_id(self.dizi["firma_sifre_b_2"])
                self.submit_btn = self.driver.find_element_by_id(self.dizi["f_basvuru_tamamla_btn"])

                for i in range(len(firma_isim)):
                    self.k_ad.clear()
                    self.f_ad.clear()
                    self.pw_con.clear()
                    self.pw.clear()
                    self.f_ad.send_keys(firma_isim[i])
                    self.k_ad.send_keys(firma_giris_adi[i])
                    self.pw.send_keys(firma_sifre_a[i])
                    self.pw_con.send_keys(firma_sifre_b[i])
                    self.submit_btn.click()
                    time.sleep(2)

                    cursor_record.execute("SELECT f_basvuru_kod_onay FROM f_basvurular WHERE f_basvuru_kod_onay = 1")
                
                    if cursor_record == False:        
                        d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        with open("LOGS/firma-email-hesap", "a") as file:   
                            file.write(" " + "\n")   
                            file.write(str(d))
                            file.write(" " + "\n")
                            file.write("Yapılan test: Başarısız firma kayıt testi")
                            file.write(" " + "\n")
                            file.write("Firma başvuru mail adresi alındı.")
                            file.write(" " + "\n")
                            file.write("Mail adresine kod gönderildi.")
                            file.write(" " + "\n")
                            file.write("Kod girişi test edildi ve firma kayıt işlemi tamamlanamadı.")
                            file.write(" " + "\n")
                            file.write("Girilen kod hatalı!")
                            file.write(" " + "\n")
                            file.write("Beklenen sonuç: İŞLEM BAŞARISIZ!")
                            file.write(" " + "\n")
                            file.write("Alınan sonuç: İŞLEM BAŞARISIZ!")
                            file.write(" " + "\n\n")
                            file.write("TEST BAŞARILI!")
                            file.write(" " + "\n\n") 
                        cprint(Fore.YELLOW, "Test Çalıştırma Tarih/Saat'i : " + str(d))
                        print("")
                        cprint(Fore.CYAN, "Yaplan Test : Başarısız firma kayıt testi.")
                        print("")
                        cprint(Fore.LIGHTBLUE_EX, "Firma başvuru mail adresi alındı!")
                        cprint(Fore.LIGHTBLUE_EX, "Mail Adresine kod gönderildi!")
                        cprint(Fore.LIGHTBLUE_EX, "Kod giriş test edildi ve firma kayıt işlemi tamamlanamadı.")
                        cprint(Fore.RED, "Girilen Kod Hatalı!")
                        print("")
                        cprint(Fore.YELLOW, "Beklenen Sonuç : İŞLEM BAŞARISIZ!")
                        print("")
                        cprint(Fore.GREEN, "Alınan Sonuç : İŞLEM BAŞARISIZ!")
                        print("")
                        cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARILI!")
                        print("")
                        time.sleep(0.5)
                                        
                    else:
                        d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        with open("LOGS/firma-email-hesap", "a") as file:
                            file.write(" " + "\n")   
                            file.write(str(d))
                            file.write(" " + "\n")
                            file.write("Yapılan test: Başarısız firma kayıt testi")
                            file.write(" " + "\n")
                            file.write("Firma başvuru mail adresi alındı : "  +  mail_2[i])
                            file.write(" " + "\n")
                            file.write("Mail adresine kod gönderildi.")
                            file.write(" " + "\n")
                            file.write("Kod girişi test edildi ve firma kayıt işlemi tamamlandı.")
                            file.write(" " + "\n")
                            file.write("Oluşturulan firmanın adı : " + firma_isim[i])
                            file.write(" " + "\n")
                            file.write("Oluşturulan firmanın kullanıcı adı : " + firma_giris_adi[i])
                            file.write(" " + "\n")
                            file.write("Oluşturulan firmanın şifresi : " + firma_sifre_a[i])
                            file.write(" " + "\n")
                            file.write("Oluşturulan firmanın şifresi(TEKRAR) : " + firma_sifre_b[i])
                            file.write(" " + "\n")
                            file.write("Firma bilgilerinde bir hata oluştu! Lütfen Girilen Verileri Kontrol Edin!")
                            file.write(" " + "\n")
                            file.write("Beklenen sonuç: İŞLEM BAŞARISIZ!")
                            file.write(" " + "\n")
                            file.write("Alınan sonuç: İŞLEM BAŞARISIZ!")
                            file.write(" " + "\n\n")
                            file.write("TEST BAŞARILI!")
                            file.write(" " + "\n\n") 
                        cprint(Fore.YELLOW, "Test Çalıştırma Tarih/Saat'i : " + str(d))
                        print("")
                        cprint(Fore.CYAN, "Yaplan Test : Başarılı firma kayıt testi.")
                        cprint(Fore.LIGHTBLUE_EX, "Firma başvuru mail adresi alındı : "  +  mail_2[i])
                        cprint(Fore.LIGHTBLUE_EX, "Mail Adresine kod gönderildi!")
                        cprint(Fore.LIGHTBLUE_EX, "Kod giriş test edildi ve firma kayıt işlemi tamamlandı!")
                        cprint(Fore.LIGHTBLUE_EX, "Oluşturulan firmanın adı : " + firma_isim[i])
                        cprint(Fore.LIGHTBLUE_EX, "Oluşturulan firmanın kullanıcı adı : " + firma_giris_adi[i])
                        cprint(Fore.LIGHTBLUE_EX, "Oluşturulan firmanın şifresi : " + firma_sifre_a[i])
                        cprint(Fore.LIGHTBLUE_EX, "Oluşturulan firmanın şifresi(TEKRAR) : " + firma_sifre_b[i])
                        print("")
                        cprint(Fore.CYAN, "Firma bilgilerinde bir hata oluştu! Lütfen Girilen Verileri Kontrol Edin!")
                        print("")
                        cprint(Fore.YELLOW, "Beklenen Sonuç : İŞLEM BAŞARISIZ!")
                        print("")
                        cprint(Fore.GREEN, "Alınan Sonuç : İŞLEM BAŞARISIZ!")
                        print("")
                        cprint(Fore.LIGHTMAGENTA_EX, "TEST BAŞARILI!")
                        print("")
                        time.sleep(0.5)

            while (count < len(mail_2)):
                self.driver.get(self.url)
                time.sleep(2)
                self.k_id = self.driver.find_element_by_id("username")
                self.k_p = self.driver.find_element_by_id("pass")
                self.k_id.send_keys("7040000001")
                self.k_p.send_keys("123456")
                self.driver.find_element_by_id("submit_button").click()
                time.sleep(2)
                self.driver.get("http://localhost/firma-kayit-baglantisi-olustur")
                time.sleep(2)
                self.e_mail = self.driver.find_element_by_id(self.degerler["mail"])
                self.app_btn = self.driver.find_element_by_id("f_basvuru_btn")
                count +=1
        
            
        
driver = webdriver.Chrome("C:\\xampp\\chromedriver.exe")
e_mail = e_mail(driver, "http://localhost/admin" , "http://localhost/firma-kayit-baglantisi-olustur",{"mail": "f_basvuru_mail"})

print(Fore.YELLOW + "Başarısız test için 1, başarılı test için 2") 
test = int(input())
print(" ")

# 1'e basılırsa yapılacak işlemler 
if test == 1:
    print(Fore.YELLOW + "Çalıştırılan test: " + "Firma kayıt, basarisiz_test")
    print("")
    # Firma_giris sınıfının içindeki basarisiz define degerleri gönderiyoruz 
    e_mail.basarisiz(["berke@gmail.com", "berke@gmail.com"], ["berke","ertan"], ["ertan", " "], ["123456", "12345"], ["5662", "1235"])

# 2'ye basılırsa yapılacak işlemler 
if test == 2:
    print(Fore.YELLOW + "Çalıştırılan test: " + "Firma kayıt, basarili_test") 
    # Firma_giris sınıfının içindeki basarili define degerleri gönderiyoruz 
    e_mail.basarili(["berke@gmail.com"],["berke"], ["berke"], ["123456788"], ["123456788"])


