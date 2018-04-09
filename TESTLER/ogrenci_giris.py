from selenium import webdriver

import colorama 
from colorama import Fore, Back, Style

import time

colorama.init()

def cprint(color, text):
    print(color + text)

class ogrenci_giris:
   
    def __init__(self, driver, url,dizi):
       self.driver = driver
       self.url = url
       self.driver.get(self.url)

       self.degerler = dizi 
       self.el_id = self.driver.find_element_by_id(self.degerler["username"])
       self.el_pas = self.driver.find_element_by_id(self.degerler["pass"])
       self.sb_btn = self.driver.find_element_by_id(self.degerler["submit_button"])
      
    def basarili(self, u_name, u_pass):
        for i in range(len(u_name)):               
            self.el_id.clear()
            self.el_pas.clear()

            self.el_id.send_keys(u_name[i])
            self.el_pas.send_keys(u_pass[i])
            
            self.sb_btn.click()
            
            result = None

            try:
                self.check = self.driver.find_element_by_id(self.degerler["deger"]).is_displayed()
                result = True
            except:
                result = False 
            
            if result:
                cprint(Fore.GREEN, "Giriş Başarılı")
            else:
                cprint(Fore.RED, "Giriş Başarısız")
                time.sleep(0.5)
                self.el_id.clear()
                self.el_pas.clear()
    def basarisiz(self,u_name,u_pass):
        for i in range(len(u_name)):               
            self.el_id.clear()
            self.el_pas.clear()

            self.el_id.send_keys(u_name[i])
            self.el_pas.send_keys(u_pass[i])
            self.sb_btn.click()

            result = None

            try:
                self.check = self.driver.find_element_by_id(self.degerler["deger"]).is_displayed()
                result = True
            except:
                result = False 
                
            if result:
                cprint(Fore.GREEN, "Giriş Başarılı")
            else:
                cprint(Fore.RED, "Giriş Başarısız")
                time.sleep(0.5)
    
        
        

driver = webdriver.Chrome("C:\\Users\\BERKE\\Downloads\\chromedriver.exe")
ogrenci_giris = ogrenci_giris(driver, "http://localhost:8080/ogrenci-giris", {"username": "username", "pass": "pass", "deger": "logan", "submit_button": "submit_button"})

ogrenci_giris.basarisiz(["20167070", "12345", "1379248"], ["5656", "6565", "35653235"])
ogrenci_giris.basarili(["2016707002", "2016707005","1379248"], ["123456s", "123456", "35653235"])




 
        


