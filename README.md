Project:  
  Scripting test against http://www.shapeways.com/product/DM8QHNHJS/taphandle

Functions:  
  Interact with most of the mechanics:
    Logging in
    Creating an account
    Placing items and removing them from cart
    Changing the material
    Posting comments and uploading pictures
    Contacting sellers
    Favoriting items
    Changing the currency

Tests:  
  As a signed on, verified user, these are the currently included unit tests:
    Add an item to cart and remove it
    Write a private message to the seller with a picture attached
    Post a comment with a picture attached
    Post a reply to a comment

Each test was performed with Chrome and Firefox

Setup:
	The environment was Windows 7, 64bit with Python 3.4.2.  Extra libraries are unittest 2 and selenium webdriver.  The can be acquired with the following pip commands:
pip install selenium
pip install unittest2
pip install unittest-xml-reporting

  The script itself can be run with python main.py

Logs:
	Logs and run results are stored in \Test-Reports as XML logs.

Closing notes:
	The site seems mechanically functional.  All tests reported positive.  The only issue that seem to be present are a few graphical and formatting issues.  Currency function is also missing for logged in users, though that may be intentional.  Core mechanics, however, such as posting comments, private messges, reply, and buy now are fully operational.
