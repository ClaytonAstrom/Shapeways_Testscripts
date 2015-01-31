from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.common.action_chains import ActionChains

#Buy it use it break it fix it trash it change it mail upgrade it
#Basic add to cart function.  Nothing special.  Checks the page source for "Added to your cart"
def buyNow (webInstance):
	try:
		element = webInstance.find_element_by_xpath(r'//button').click()
		src = webInstance.page_source
		if re.search('Added to your cart', src) != 'None':
			return 'true'
		else:
			return 'not added'
	except:
		return 'false'
	
#Actually goes into the cart to make sure it's there.  Just to be safe.
#Also it removes it.	
def isIn (webInstance):
	try:
		element = webInstance.find_element_by_css_selector('span.icon-cart').click()
		time.sleep(1)
		element = webInstance.find_element_by_link_text('Remove').click()
		time.sleep(3)
		src = webInstance.page_source
		if re.search('Your cart is empty', src) != 'None':
			return 'true'
		else:
			return 'unable to remove'
	except:
		return 'not in cart'

#This was a bit of a nightmare.  Without the other functions, it's a bit useless, but it does favorite an item, honest!
def favoriteItem (webInstance):
	try:
		element = webInstance.find_element_by_xpath('//div[2]/section/div[3]/div/div/a').click()
		time.sleep(1)
		try:
			element = webInstance.find_element_by_css_selector('div.close-button').click()
			return 'sign in required'
		except:
			if 'favorites' in webInstance.current_url:
				try:
					time.sleep(3)
					element = webInstance.find_element_by_link_text('Remove').click()
					return 'removed'
				except:
					return 'unable to remove'
			else:
				return 'true'
		
	except:
		return 'false'

		
#Clicks contact seller.  Checks to make sure the user can, as in not unverified or not signed in or the like.
def contactSeller(webInstance):
	try:
		element = webInstance.find_element_by_link_text('Contact').click()
		src = webInstance.page_source
		if 'verification' in webInstance.current_url:
			return 'unverified'
		elif 'login' in webInstance.current_url:
			return 'sign in required'
			
		time.sleep(1)
		src = webInstance.page_source
		if re.search('Writing a private message', src) != 'None':
			return 'true'
		else:
			return 'mismatched page?'
		
	except:
		return 'false'

#Writes a bogus message, adds C:\NO.jpg as an attachment, and sends.
#Probably should make the picture optional, but it's a minor check and I want to finish a few other things right now
def writePM(webInstance, user, count):
	try:
		
		element = webInstance.find_element_by_css_selector('input[name="msg_subject"]').send_keys('Message #%d' % count)
		
		element = webInstance.find_element_by_id('txtb').send_keys('I am user %s and this is message #%s' % (user, count))
	
		element = webInstance.find_element_by_css_selector('input[name="attach_control"]').send_keys(r'C:\\NO.jpg')
		
		
		element = webInstance.find_element_by_css_selector('a.secondary-button').click()
		
		
		element = webInstance.find_element_by_xpath('//a[3]').click()
		time.sleep(2)
		
		
		if 'fldr=1' is webInstance.current_url:
			return 'true'
		else:
			return false
		
	except:
		return 'false'
		


#I'd like to implement this function, checking if something is favorited by viewing the user's favorite list.
#unfortunately there are more important things to test.	
#def isFavorited (webInstance):
#	try:
#		element = webInstance.find_element_by_xpath('//div[2]/section/div[3]/div/div/a').click()
#		time.sleep(1)
#		if 'favorites' in webInstance.current_url:
#			return 'already favorited'
#		else:
#			return 'not favorited'
#		
#	except:
#		return 'false'

#This, in theory, should be the exact same pattern as favoriteItem.  Don't be fooled.  It's not.
#Really in frequent and variable with results, may even be a bug in find_element class.
#Skipping for now, as well as list manager
#def wishItem (webInstance):
#	try:
#		element = webInstance.find_element_by_xpath('//div[2]/section/div[3]/div/div/a[2]').click()
#		time.sleep(1)
#		print('done sleeping')
#		if webInstance.find_element_by_css_selector('div.close-button').is_displayed():
#			print('it exists here?')
#			element = webInstance.find_element_by_css_selector('div.close-button').click()
#			return 'sign in required'
#		else:
#			print('skipped signin')
#			if 'wishlist' in webInstance.current_url:
#				print('in the loop')
#				try:
#					time.sleep(1)
#					element = webInstance.find_element_by_link_text('Remove').click()
#					return 'removed'
#				except:
#					return 'unable to remove'
#			else:
#				return 'true'
#		
#	except:
#		return 'false'
