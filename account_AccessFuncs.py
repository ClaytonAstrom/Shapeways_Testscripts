from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.common.action_chains import ActionChains

#Function to sign on.  Checks are done in isLoggedOn
def signIn(webInstance, user, password):
	try:
		webInstance.find_element_by_link_text('Sign In').click()
		WebDriverWait(webInstance, 10).until(EC.presence_of_element_located((By.ID, 'login_username')))
		element = webInstance.find_element_by_id('login_username').send_keys(user)
		element = webInstance.find_element_by_id('login_password').send_keys(password)
		element = webInstance.find_element_by_css_selector('#form1 > input.join-button-sw').click()
		time.sleep(3)
		return 'true'
	except:
		return 'unsuccessful login:  unknown'
#Sign out function cannot find the dropdown.  Tried by name, id, text, css, xpath, and even some js calls.  Going to have to let this one go		
#def signOut(webInstance):
#	try:
#		webInstance.find_element_by_xpath(r'//div[@id=\'header\']/div[6]/div/ul/li[8]/a').click() 
#		return 'true'
#
#	except:
#		return 'could not sign user out'
	 
	 
#Just a script to generate accounts.  May come in handy
def makeAccount(webInstance, user, password, email):
	try:
		webInstance.find_element_by_link_text('Join').click()
		WebDriverWait(webInstance, 10).until(EC.presence_of_element_located((By.ID, 'sign_up_email')))
		element = webInstance.find_element_by_id('sign_up_email').send_keys(email)
		element = webInstance.find_element_by_id('sign_up_username').send_keys(user)
		element = webInstance.find_element_by_id('sign_up_password').send_keys(password)
		element = webInstance.find_element_by_css_selector('input.join-button-sw.breathe-vertical').click()
		time.sleep(3)
		return 'true'
	except:
		return 'false'

#Checks the URL for https.  Shouldn't have it if we're not logged in
def isLoggedOn(webInstance):
	
	try:
		if 'https' in webInstance.current_url:
			return 'true'
		
	except:
		return 'false'

#I don't think I need this function for much, but I thought I would use it more at the time.  Checks down the login in for different errors, if we're stuck there
def errorCheck(webInstance):
	
	src = webInstance.page_source
	if re.search(r'couldn\'t verify', src) == 'None':
		if re.search(r'look valid', src) == 'None':
			if re.search(r'Minimum 5', src) == 'None':
				if re.search(r'Max 30', src) == 'None':
					return('None')
				else:
					return('>30')
			else:
				return ('<5')
		else:
			return('bad email')
	else:
		return('bad creds')