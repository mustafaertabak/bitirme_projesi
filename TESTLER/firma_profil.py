from selenium import webdriver

import colorama 
from colorama import Fore, Back, Style

import time

colorama.init()

def cprint(color, text):
    print(color + text)

    class firma-profil:

        def __init__(self, driver, url, dizi):         
            self.driver = driver
            self.url = url 
            self.driver.get(self.url)

            self.arr = dizi 
            self.e_mail = self.driver.find_element_by_id(self.dizi["exampleInputEmail1"])
            self.password = self.driver.find_element_by_id(self.dizi["exampleInputPassword1"])
            self.aciklama = self.driver.find_element_by_id(self.dizi["exampleFormControlTextarea1"])
            self.btn = self.driver.get_attribute(self.dizi["submit"])
        
        def basarili(self, mail, pas, aciklama):
            for i in range(len(mail)):
                self.e_mail.clear()
                self.password.clear()
                self.acikalama.clear()

                self.e_mail.send_keys(mail[i])
                self.password.send_keys(pas[i])
                self.aciklama.send_keys(aciklama[i])
                
                self.btn.click()

                sonuc = None 

                
        
           



            
            


