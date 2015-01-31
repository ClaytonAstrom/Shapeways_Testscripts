from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.common.action_chains import ActionChains


#Just posting a comment with a picture and replying to comments.  Again, uploads C:\NO.jpg, incase anyone runs into a missing file issue
def writeComment(webInstance, user, count):
	try:
		element = webInstance.find_element_by_name('commentText').click()
		element = webInstance.find_element_by_name('commentText').send_keys('User %s with public message #%s' % (user, count))
		time.sleep(3)
		element = webInstance.find_element_by_name('uploadedPicture').send_keys(r'C:\\NO.jpg')
		time.sleep(1)
		element = webInstance.find_element_by_css_selector('button.submit-comment.right').click()
		return 'true'
	except:
		return 'false'
		
def writeReply(webInstance, user, count):
	try:
		element = webInstance.find_element_by_css_selector('a.subtle-button-inset.small').click()
		element = webInstance.find_element_by_name('commentText').send_keys(' Reply #%s' % count)
		element = webInstance.find_element_by_css_selector('button.submit-comment.right').click()
		
		return 'true'
		
	except:
		return 'false'