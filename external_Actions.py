from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.common.action_chains import ActionChains

#Inconsistent script, I'm not going to implement it.  Seems to wait often for facebook.com and as.eu.angsrvr.com, which verification almost always goes against.

#Anyway what the script *should* do is click the "Please verify your account to comment" link at the bottm, then resend activation link (common failure point).  Then it will shoot out to
#mailinator, log in, open the email, and (should) click the activation link.  That also is kind of a wash.  Probably could revisit someday and translate the email to raw format, then
#pick the url.  For now this is inconsequential
def activateAccount(webInstance, user):
	try:
		element = webInstance.find_element_by_css_selector('div.comment-prompt.clearfix  > a').click() #This is the line that says "Please verify your account first"
		time.sleep(1) 																					
		element = webInstance.find_element_by_name('resend').click()									#Failure point 1, resend activation link
		webInstance.get('http://mailinator.com/')
		time.sleep(3)
		element = webInstance.find_element_by_id('inboxfield').send_keys('%s@mailinator.com' % user)    #Good old mailinator.  Throw away site for emails, no passwords.
		element = webInstance.find_element_by_css_selector('btn.btn.btn-success').click()				#Confirm the login
		time.sleep(1)
		element = webInstance.find_element_by_css_selector('div.from.ng-binding').click()				#Open the latest email
		element = webInstance.find_element_by_xpath('//a/font').click()									#Failure point 2, can't click this to save my life
		time.sleep(2)
		if 'thank-you' in webInstance.current_url:														#Just checking that we hit the right page after we confirm
			return 'true'
		else:
			return 'not verified'
	except:
		return 'false'
		
#I was going to add extra functions in here to test case the facebook, pinterest, twitter, and embedded options.  But I think they're largely functional.  Maybe a future feature