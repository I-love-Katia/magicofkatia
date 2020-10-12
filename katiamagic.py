'''
Symbol of Trident--> steadfastness and preserverance; a will to conquer. 

'''
import sys 
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
import wget 
def magicofkatia():     
   # driver = webdriver.Chrome(ChromeDriverManager().install()
    options = webdriver.ChromeOptions()
    profile = {"download.default_directory": "C:\\SeleniumTests\\PDF","download.prompt_for_download": True,"download.directory_upgrade": True, "download.extensions_to_open": "applications/pdf"}                                            
    options.add_experimental_option("prefs", profile)           
    chrome_path=r'C:\Users\arkar\Desktop\Pythonskill\chromedriver_win32\chromedriver.exe'
    driver = webdriver.Chrome(chrome_path,chrome_options=options)
    ID=range(140000)
    c=ID[0:300:10]
    for c in ID:
        try:
            driver.implicitly_wait(10)
            a=driver.get('http://users.cecs.anu.edu.au/~hongdong/')
            link=driver.find_element_by_partial_link_text('.pdf')
            
            for link in a: 
                clicks=link.click()
                
                
                
        except:
            pass
        
        
        
        
    
    
    
   
