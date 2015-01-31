import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import account_AccessFuncs
import change_Options
import seller_Interact
import public_Interact
import external_Actions
import xmlrunner



class tapHandle_Tests(unittest.TestCase):

#Changing currency in each browser 5 times, from United States, to United Kingdom, back to United states, while not logged on (option is not at all available while logged in)
#Noticed this was inconsistent, would disappear sometimes.  Test results, however, prove otherwise.

#Leaving IE out of test cases.  WebDriver was causing some issues with validity of test data.
	def skip_currencyStress_Firefox(self):
		driver = webdriver.Firefox()
		driver.get('http://www.shapeways.com/product/DM8QHNHJS/taphandle')
		try:
			element = driver.find_element_by_css_selector('span.close-box').click()
		except:
			print('nothing to close')
		self.assertTrue(change_Options.changeCurr(driver, 'United States', 'United Kingdom', 10))
		driver.quit()
		
	def skip_currencyStress_Chrome(self):
		driver = webdriver.Chrome()
		driver.get('http://www.shapeways.com/product/DM8QHNHJS/taphandle')
		try:
			element = driver.find_element_by_css_selector('span.close-box').click()
		except:
			print('nothing to close')
		self.assertTrue(change_Options.changeCurr(driver, 'United States', 'United Kingdom', 10))
		driver.quit()
		
#Phrasing!  Communicative tools pull from a lot of different areas.  It's also one of the most dynamic areas, good thing to test first
		
	def test_privateMessage_Firefox(self):
		driver = webdriver.Firefox()
		driver.get('http://www.shapeways.com/product/DM8QHNHJS/taphandle')	
		try:
			element = driver.find_element_by_css_selector('span.close-box').click()
		except:
			print('nothing to close')
		user = '0user0_ca_test'
		account_AccessFuncs.signIn(driver, user, user)
		account_AccessFuncs.isLoggedOn(driver)
		seller_Interact.contactSeller(driver)
		self.assertTrue(seller_Interact.writePM(driver, user, 1))
		driver.quit()
		
	def test_privateMessage_Chrome(self):
		driver = webdriver.Chrome()
		driver.get('http://www.shapeways.com/product/DM8QHNHJS/taphandle')
		try:
			element = driver.find_element_by_css_selector('span.close-box').click()
		except:
			print('nothing to close')
		user = '0user0_ca_test'
		account_AccessFuncs.signIn(driver, user, user)
		account_AccessFuncs.isLoggedOn(driver)
		seller_Interact.contactSeller(driver)
		self.assertTrue(seller_Interact.writePM(driver, user, 1))
		driver.quit()

#Public comments and picture uploads
		
	def test_publicComment_Firefox(self):
		driver = webdriver.Firefox()
		driver.get('http://www.shapeways.com/product/DM8QHNHJS/taphandle')
		try:
			element = driver.find_element_by_css_selector('span.close-box').click()
		except:
			print('nothing to close')
		user = '0user0_ca_test'
		account_AccessFuncs.signIn(driver, user, user)
		account_AccessFuncs.isLoggedOn(driver)
		self.assertTrue(public_Interact.writeComment(driver, user, 1))
		driver.quit()
		
	def test_publicComment_Chrome(self):
		driver = webdriver.Chrome()
		driver.get('http://www.shapeways.com/product/DM8QHNHJS/taphandle')
		try:
			element = driver.find_element_by_css_selector('span.close-box').click()
		except:
			print('nothing to close')
		user = '0user0_ca_test'
		account_AccessFuncs.signIn(driver, user, user)
		account_AccessFuncs.isLoggedOn(driver)
		self.assertTrue(public_Interact.writeComment(driver, user, 1))
		driver.quit()
	
#Like comments, but with more!
	
	def test_publicComment_Firefox(self):
		driver = webdriver.Firefox()
		driver.get('http://www.shapeways.com/product/DM8QHNHJS/taphandle')
		try:
			element = driver.find_element_by_css_selector('span.close-box').click()
		except:
			print('nothing to close')
		user = '0user0_ca_test'
		account_AccessFuncs.signIn(driver, user, user)
		account_AccessFuncs.isLoggedOn(driver)
		self.assertTrue(public_Interact.writeReply(driver, user, 1))
		driver.quit()
		
	def test_publicComment_Chrome(self):
		driver = webdriver.Chrome()
		driver.get('http://www.shapeways.com/product/DM8QHNHJS/taphandle')
		try:
			element = driver.find_element_by_css_selector('span.close-box').click()
		except:
			print('nothing to close')
		user = '0user0_ca_test'
		account_AccessFuncs.signIn(driver, user, user)
		account_AccessFuncs.isLoggedOn(driver)
		self.assertTrue(public_Interact.writeReply(driver, user, 1))
		driver.quit()

#Get in loser, we're going shopping!  An ecommerce website is useless without cart functionality.

	def test_checkOut_Firefox(self):
		driver = webdriver.Firefox()
		driver.get('http://www.shapeways.com/product/DM8QHNHJS/taphandle')
		try:
			element = driver.find_element_by_css_selector('span.close-box').click()
		except:
			print('nothing to close')
		user = '0user0_ca_test'
		seller_Interact.buyNow(driver)
		self.assertTrue(seller_Interact.isIn(driver))
		driver.quit()
	
	def test_checkOut_Chrome(self):
		driver = webdriver.Chrome()
		driver.get('http://www.shapeways.com/product/DM8QHNHJS/taphandle')
		try:
			element = driver.find_element_by_css_selector('span.close-box').click()
		except:
			print('nothing to close')
		user = '0user0_ca_test'
		seller_Interact.buyNow(driver)
		self.assertTrue(seller_Interact.isIn(driver))
		driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
		failfast=False, buffer=False, catchbreak=False)














		#testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
		#failfast=False, buffer=False, catchbreak=False



























#GRAVEYARD!  Not much down here other than a myriad of print lines to help me debug.




#Global DRIVER variable to pass our current instance of webdriver around the script
#DRIVER = None
#'%s@mailinator.com' % user
#def makeReturnDriver(browser):
#	global DRIVER
#	if browser is 'firefox': 
#		DRIVER = DRIVER or webdriver.Firefox()  #return driver if it exists or start a new firefox instance
#		return DRIVER
#	elif browser is 'chrome':
#		DRIVER = DRIVER or webdriver.Chrome()   #return driver if it exists or start a new chrome instance
#		return DRIVER
#	elif browser is 'ie':
#		DRIVER = DRIVER or webdriver.Ie()		#return driver if it exists or start a new IE instance
#		return DRIVER


		
		

		
#user = '0user8_ca_test'
#password = '0user8_ca_test'
#count = 1
#driver = makeReturnDriver('firefox')
#driver.get('http://www.shapeways.com/product/DM8QHNHJS/taphandle')
try:
	element = driver.find_element_by_css_selector('span.close-box').click()
except:
	print('nothing to close')

#	
#print(seller_Interact.buyNow(driver))
#print(seller_Interact.isIn(driver))

#print (change_Options.changeColor(driver, 'black', 'mat'))
#print (change_Options.changeColor(driver, 'white', 'mat'))
#print (change_Options.changeColor(driver, 'black', 'thumb'))
#print (change_Options.changeColor(driver, 'white', 'thumb'))
#print(change_Options.changeCurr(driver, 'United Kingdom'))


#account_AccessFuncs.makeAccount(driver, user, password)

#print(account_AccessFuncs.is_LoggedOn(driver))
#print(driver.current_url)
#print(account_AccessFuncs.signIn(driver, user, password))
#print(seller_Interact.favoriteItem(driver))
#print(seller_Interact.wishItem(driver))
#print(seller_Interact.contactSeller(driver))
#print(seller_Interact.writePM(driver, user, count))
#print(public_Interact.writeComment(driver, user, count))
#print(public_Interact.writeReply(driver, user, count))
#print(driver.current_url)
#print(account_AccessFuncs.is_LoggedOn(driver))

#if account_AccessFuncs.is_LoggedOn(driver) == 'true':
#	print('user has signed on')
#elif account_AccessFuncs.errorCheck(driver) != 'None':
#	print('user has entered invalid name or password')
#print(external_Actions.activateAccount(driver, user))
	

#account_AccessFuncs.signOut(driver)

#if account_AccessFuncs.is_LoggedOn(driver) == 'true':
#	print('user has not signed out')
#elif account_AccessFuncs.is_LoggedOn(driver) == 'false':
#	print('user has signed out')