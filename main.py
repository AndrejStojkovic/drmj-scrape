from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import json

letters = ['а', 'б', 'в', 'г', 'д', 'ѓ', 'е', 'ж', 'з', 'ѕ',
           'и', 'ј', 'к', 'л', 'љ', 'м', 'н', 'њ', 'о', 'п',
           'р', 'с', 'т', 'ќ', 'у', 'ф', 'х', 'ц', 'ч', 'џ', 'ш']

def scrape_letter(browser, letter):
    ranges = Select(browser.find_element(By.XPATH, "//select[@name='ranges']"))
    
    for index in range(len(ranges.options)):
        ranges = Select(browser.find_element(By.XPATH, "//select[@name='ranges']"))
        ranges.select_by_index(index)
        grab_words(browser, letter) 
        
    #time.sleep(2)

def grab_words(browser, letter):
    lexems = Select(wait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//select[@name='lexems']"))))
    words = lexems.options

    for word in words:
        w = word.text.split()
        
        fp = open('bukvi/' + letter + '.txt', 'a', encoding="utf-8")
        fp.write(w[0] + '\n')
        fp.close();
                
        print(w[0])

def main():
    for letter in letters:
        browser = webdriver.Chrome()
        browser.get('http://drmj.eu/letter/' + letter)

        fp = open('bukvi/' + letter + '.txt', 'w')
        
        scrape_letter(browser, letter)
        
        browser.close()

main()

print('Done')
input('Press Enter to exit')


