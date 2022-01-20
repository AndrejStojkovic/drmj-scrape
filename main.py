from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import json

# letters to scrape
letters = ['а', 'б', 'в', 'г', 'д', 'ѓ', 'е', 'ж', 'з', 'ѕ',
           'и', 'ј', 'к', 'л', 'љ', 'м', 'н', 'њ', 'о', 'п',
           'р', 'с', 'т', 'ќ', 'у', 'ф', 'х', 'ц', 'ч', 'џ', 'ш']

# If you want to scrape only certain letters comment the array above and uncomment below
# and add the letters you want to the array using Macedonian Keyboard support as above

#letters = ['а', 'к', 'л']

# Function used to scrape each letter (SPECIFIC TO THIS SITE, DON'T TOUCH)
# The dictionary on this site doesn't display all the words from a certain letter,
# Sso you need this function to go through every word from a letter
def scrape_letter(browser, letter):
    ranges = Select(browser.find_element(By.XPATH, "//select[@name='ranges']"))
    
    for index in range(len(ranges.options)):
        ranges = Select(browser.find_element(By.XPATH, "//select[@name='ranges']"))
        ranges.select_by_index(index)
        grab_words(browser, letter) 

# Function used to scrape each word (SPECIFIC TO THIS SITE, DON'T TOUCH)
def grab_words(browser, letter):
    lexems = Select(browser.find_element(By.XPATH, "//select[@name='lexems']"))
    words = lexems.options

    for word in words:
        w = word.text.split()
        
        fp = open('bukvi/' + letter + '.txt', 'a', encoding="utf-8")
        fp.write(w[0] + '\n')
        fp.close();
                
        print(w[0])

# Main function
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


