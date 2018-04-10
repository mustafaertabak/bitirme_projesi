from selenium import webdriver

import colorama 
from colorama import Fore, Back, Style

import time

colorama.init()

def cprint(color, text):
    print(color + text)

    class kod_onay:
        
        def __init__(self, driver, url, dizi):
            self.driver = driver 
            self.url = url 

            self.dizi = dizi 
            self.driver.get(self.url)
            self.input = self.driver.find_element_by_id(self.dizi["exampleInputPassword1"])
            self.btn = self.driver.get_attirbute(self.dizi["btn"])

        def basarisiz(self, input_b):
            for i in range(len(input_b)):
                self.input.clear()
                
                self.input.send_keys(input_b[i])
                self.btn.click()
                
                sonuc = None 

                try:
                    self.control = self.driver.get_attirbute("alert").is_displayed()
                    sonuc = True 
                except:
                    sonuc = False 

                if sonuc:
                    cprint(Fore.GREEN, "Kod girişi başarısız")
                else:
                    cprint(Fore.RED, "Kod girişi başarılı")
                    time.sleep(0.5)

river = webdriver.Chrome("C:\\Users\\BERKE\\Downloads\\chromedriver.exe")

kod_onay = kod_onay(driver, "C:/Users/BERKE/Desktop/bitirme/kod-onay.html", {"input": "exampleInputPassword1"})

kod_onay.basarisiz(["156556565", "56532326", "54565656"])