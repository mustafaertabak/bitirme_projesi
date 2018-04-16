from selenium import webdriver

import colorama 
from colorama import Fore, Back, Style

import time

colorama.init()

def cprint(color, text):
    print(color + text)

    class code_correct:
        
        def __init__(self, driver, url, dizi):
            self.driver = driver 
            self.url = url 

            self.dizi = dizi 
            self.driver.get(self.url)
            self.input = self.driver.find_element_by_class_name(self.dizi["input"])
            self.btn = self.driver.find_element_by_class_name(self.dizi["btn"])

        def basarisiz(self, input_b):
            for i in range(len(input_b)):
                self.input.clear()
                
                self.input.send_keys(input_b[i])
                self.btn.click()
                
                sonuc = None 

                try:
                    self.control = self.driver.find_element_by_class_name("alert").is_displayed()
                    sonuc = True 
                except:
                    sonuc = False 

                if sonuc:
                    cprint(Fore.GREEN, "Kod girişi başarısız")
                else:
                    cprint(Fore.RED, "Kod girişi başarılı")
                    time.sleep(0.5)

driver = webdriver.Chrome("C:\\Users\\BERKE\\Downloads\\chromedriver.exe")

code_correct = code_correct(driver, "C:\\Users\\BERKE\\Desktop\\bitirme\\kod_onay.html", {"input": "input_h", "btn": "giris-btn"})

code_correct.basarisiz(["156556565", "56532326", "54565656"])