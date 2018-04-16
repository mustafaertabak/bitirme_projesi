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

class bilgi_duzen:

    def __init__(self, driver, url, url2, dizi):
        self.driver = driver
        self.url = url
        self.url2 = url2
        self.driver.get(self.url)

        self.k_name = self.driver.find_element_by_id("username")
        self.k_pass = self.driver.find_element_by_id("pass")
        self.k_btn = self.driver.find_element_by_id("submit_button")
        
        self.k_name.send_keys("vestel")
        self.k_pass.send_keys("123456")
        self.k_btn.click()
        time.sleep(1)

        self.driver.get(self.url2)

        self.driver.find_element_by_id("info_edit").click()
        
        self.dizi = dizi
        self.frm_name = self.driver.find_element_by_id(self.dizi["name"])
        self.frm_kname = self.driver.find_element_by_id(self.dizi["kname"])
        self.frm_btn = self.driver.find_element_by_id(self.dizi["btn"])
    
    def basarisiz(self, u_name, u_kname):

        for i in range (len(u_name)):
            self.frm_name.clear()
            self.frm_kname.clear()

            self.frm_name.send_keys(u_name[i])
            self.frm_kname.send_keys(u_kname[i])
            self.frm_btn.click()
            time.sleep(1)

            self.show = self.driver.find_element_by_id(self.dizi["name"]).is_displayed()
            if self.show:
                cprint(Fore.RED, "BAŞARISIZ!")
            else:
                cprint(Fore.GREEN, "BAŞARILI!")

    def basarili(self, u_name, u_kname):

        for i in range (len(u_name)):
            self.frm_name.clear()
            self.frm_kname.clear()

            self.frm_name.send_keys(u_name[i])
            self.frm_kname.send_keys(u_kname[i])
            self.frm_btn.click()
            time.sleep(1)

            self.acc_btn = self.driver.find_element_by_class_name("btn-success")
            self.acc_btn.click()
            time.sleep(1.5)
            
            self.show = self.driver.find_element_by_id(self.dizi["name"]).is_displayed()
            if self.show:
                cprint(Fore.RED, "BAŞARISIZ!")
            else:
                cprint(Fore.GREEN, "BAŞARILI!")

driver = webdriver.Chrome()
bilgi_duzen = bilgi_duzen(driver,"http://localhost/firma-giris", "http://localhost/profil", {"name": "bilgiler_isim", "kname": "bilgiler_giris_adi", "btn": "bilgiler_btn"})
bilgi_duzen.basarili(["Vestel"], ["vestel"])






