from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.common.action_chains import ActionChains

#Call me paranoid, but the currency disappears.  My tests say otherwise, but I've got my eye on you, you tiny bundle of flags.
#Does a couple of loops to flip the currency back and forth, loosely spoken it seems to go away after a couple of changes.  
def changeCurr(webInstance, beginCount, changeCount, loops):
	try:
		for x in range (0, loops):
			#time.sleep(3)
			element = webInstance.find_element_by_css_selector('span.country-flag').click()
			element = webInstance.find_element_by_id('autocompleteCountry').send_keys(changeCount)
			element = webInstance.find_element_by_id('submitChangeCountryCurrency').click()
			time.sleep(3)
			element = webInstance.find_element_by_css_selector('span.country-flag').click()
			element = webInstance.find_element_by_id('autocompleteCountry').send_keys(beginCount)
			element = webInstance.find_element_by_id('submitChangeCountryCurrency').click()
			time.sleep(3)
		
		return true
		
		#At one point it was a good idea to make sure the currency was being changed and not just spinning its wheels with the same input.
		#I think I disagree with that now, so I've commented this out
		#src = webInstance.page_source
		#if re.search(changeCount, src) != 'None':
		#	return 'true'
		#else:
		#	return 'country not changed'
			
	except:
		return 'false'
#Just makes sure that the colors change when clicking another one.  It works fine, but here it is if anyone needs it
#Checks against page URL
def changeColor(webInstance, colorChange, matorthumb):
	try:
		if colorChange == 'black' and matorthumb == 'mat':
			element = webInstance.find_element_by_xpath(r'//div[2]/section/div/div/div/div/div/div/div/a[2]/div/img').click()
			if '7360379' in webInstance.current_url:
				return 'true'
			else:
				return 'false'
		elif colorChange == 'white' and matorthumb == 'mat':
			element = webInstance.find_element_by_xpath(r'//div[2]/section/div/div/div/div/div/div/div/a/div/img').click()
			if '7360377' in webInstance.current_url:
				return 'true'
			else:
				return 'false'
		elif colorChange == 'black' and matorthumb == 'thumb':
			element = webInstance.find_element_by_xpath(r'//a[3]/img').click()
			if '7360379' in webInstance.current_url:
				return 'true'
			else:
				return 'false'
				
		elif colorChange == 'white' and matorthumb == 'thumb':
			element = webInstance.find_element_by_xpath(r'//a[4]/img').click()
			if '7360377' in webInstance.current_url:
				return 'true'
			else:
				return 'false'
		else:
			return 'bad params'
	except:
		return 'false'