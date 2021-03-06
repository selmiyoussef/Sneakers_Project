#####Created a folder on my Desktop called, "WebScrapingProject"
#####Opened SublimeText, create a new file and it as 'setup.py'
#####Typed the following intructions: 


from selenium import webdriver
# 1st import: Allows you to launch/initiate a browser

from selenium.webdriver.common.by import By
#2nd import: Allows you to search for things using specific parameters.

from selenium.webdriver.support.ui import WebDriverWait
#3rd import: Allows you to wait for a page to load.

from selenium.webdriver.support import expected_conditions as EC
#4th import: Specify what you are looking for on a specific page in order to determine that the webpage has loaded.

from selenium.common.exceptions import TimeoutException
#5th import: Handling a timeout situation


import time
import csv
import re

usernameStr = '0xxyyzz00@gmail.com'
passwordStr = 'xyzT!Tan1c'


driver = webdriver.Chrome()
#Initializes a Chrome Browser or creates a new instance of Chrome

driver.get('https://stockx.com/login')

username = driver.find_element_by_id('login[username]')
username.send_keys(usernameStr)
# nextButton = driver.find_element_by_id('next')
# nextButton.click()

password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'login[password]')))
password.send_keys(passwordStr)
 
signInButton = driver.find_element_by_id('login-button')
signInButton.click()

#Long list of urls from which we want to scrafe info. 35 top selling sneakers from the most popular collection of Adidas, Nike, Air Jordan
long_url_list = ["https://stockx.com/air-jordan-1-retro-black-blue-2017",     #1     {### Air Jordan: One ###}
			"https://stockx.com/air-jordan-1-retro-mid-new-love-2017",
			"https://stockx.com/jordan-1-retro-bred-2016",
			"https://stockx.com/jordan-1-retro-yin-yang-black",
			"https://stockx.com/air-jordan-1-retro-all-star-2017",
			"https://stockx.com/air-jordan-1-retro-top-3",
			"https://stockx.com/jordan-1-retro-yin-yang-white",
			"https://stockx.com/air-jordan-1-retro-black-toe-2016",
			"https://stockx.com/air-jordan-1-retro-high-gold-top-3",
			"https://stockx.com/air-jordan-1-retro-high-og-metallic-red-2017",
			"https://stockx.com/air-jordan-1-retro-high-off-white-chicago",
			"https://stockx.com/air-jordan-1-retro-high-wings",
			"https://stockx.com/air-jordan-1-retro-reverse-shattered-backboard",
			"https://stockx.com/jordan-1-retro-chicago-2015",
			"https://stockx.com/air-jordan-1-retro-high-flyknit-bred",
			"https://stockx.com/air-jordan-1-retro-essentials-sail",
			"https://stockx.com/air-jordan-1-retro-high-og-royal-2017-gs",
			"https://stockx.com/jordan-1-retro-unc",
			"https://stockx.com/air-jordan-1-retro-high-red-suede",
			"https://stockx.com/jordan-1-retro-shattered-backboard",    #20
			"https://stockx.com/jordan-1-retro-metallic-navy-2016",
			"https://stockx.com/air-jordan-1-retro-high-gatorade-cyber",
			"https://stockx.com/air-jordan-1-retro-black-perforated",
			"https://stockx.com/air-jordan-1-retro-high-blue-suede",
			"https://stockx.com/air-jordan-1-retro-essentials-black",
			"https://stockx.com/air-jordan-1-retro-high-og-quai54",
			"https://stockx.com/air-jordan-1-retro-high-los-primeros",
			"https://stockx.com/air-jordan-1-retro-high-gatorade-orange-peel",
			"https://stockx.com/air-jordan-1-retro-storm-blue",
			"https://stockx.com/jordan-1-retro-bronze-medal",          #30
			"https://stockx.com/jordan-1-retro-david-letterman",  
			"https://stockx.com/jordan-1-retro-cyber-monday",
			"https://stockx.com/air-jordan-1-retro-bred-2016-gs",
			"https://stockx.com/air-jordan-1-retro-high-re2pect-derek-jeter",
			"https://stockx.com/air-jordan-1-retro-high-gatorade-blue-lagoon",  #35   
			"https://stockx.com/adidas-yeezy-boost-350-v2-beluga-2-0",     #1     {### Adidas: Yeezy ###}  
			"https://stockx.com/adidas-yeezy-boost-350-v2-cream-white",
			"https://stockx.com/adidas-yeezy-boost-350-v2-blue-tint",
			"https://stockx.com/adidas-yeezy-boost-350-v2-white-core-black-red",
			"hhttps://stockx.com/adidas-yeezy-powerphase-calabasas-core-white",
			"https://stockx.com/adidas-yeezy-boost-350-v2-steeple-grey-beluga-solar-red",
			"https://stockx.com/adidas-yeezy-boost-350-v2-core-black-white",
			"https://stockx.com/adidas-yeezy-boost-350-v2-semi-frozen-yellow",
			"https://stockx.com/adidas-yeezy-powerphase-calabasas-grey",
			"https://stockx.com/adidas-yeezy-boost-350-v2-core-black-red-2017",
			"https://stockx.com/adidas-yeezy-boost-350-v2-core-black-green",
			"https://stockx.com/adidas-yeezy-wave-runner-700-solid-grey",
			"https://stockx.com/adidas-yeezy-boost-350-v2-core-black-red",
			"hhttps://stockx.com/adidas-yeezy-boost-350-v2-core-black-red-2017-i",
			"https://stockx.com/adidas-yeezy-boost-350-v2-core-black-copper",
			"https://stockx.com/adidas-yeezy-boost-350-oxford-tan",
			"https://stockx.com/adidas-yeezy-boost-350-moonrock",
			"https://stockx.com/adidas-yeezy-boost-750-chocolate-light-brown-gum",
			"https://stockx.com/adidas-yeezy-boost-750-light-grey-glow-in-the-dark",
			"https://stockx.com/adidas-yeezy-boost-350-pirate-black-2016",    #20
			"https://stockx.com/adidas-yeezy-boost-350-v2-cream-white-i",
			"https://stockx.com/adidas-yeezy-boost-350-turtledove",
			"https://stockx.com/adidas-yeezy-boost-750-triple-black",
			"https://stockx.com/adidas-yeezy-boost-350-pirate-black-2015",
			"https://stockx.com/adidas-yeezy-350-cleat-turtledove",
			"https://stockx.com/adidas-yeezy-boost-950-peyote",
			"https://stockx.com/adidas-yeezy-boost-950-pirate-black",
			"https://stockx.com/adidas-yeezy-boost-750-light-brown",
			"https://stockx.com/adidas-yeezy-boost-350-pirate-black-i",
			"https://stockx.com/adidas-yeezy-boost-350-turtle-dove-i",          #30
			"https://stockx.com/adidas-yeezy-boost-950-chocolate",  
			"https://stockx.com/adidas-yeezy-boost-950-moonrock",
			"https://stockx.com/adidas-yeezy-boost-950-pirate-black-w",
			"https://stockx.com/adidas-yeezy-boost-950-moonrock-w",
			"https://stockx.com/adidas-yeezy-powerphase-calabasas-core-black",  #35
			"https://stockx.com/nike-air-max-97-silver-bullet-2016",     #1     {### Nike: Air Max ###}   
			"https://stockx.com/nike-air-max-97-undftd-black",
			"https://stockx.com/nike-air-max-97-metallic-gold-2017",
			"https://stockx.com/nike-air-max-90-off-white",
			"https://stockx.com/nike-air-max-97-undftd-white",
			"https://stockx.com/nike-air-max-1-anniversary-red-2017-restock",
			"https://stockx.com/nike-air-vapormax-pure-platinum",
			"https://stockx.com/nike-air-vapormax-off-white",
			"https://stockx.com/nike-air-vapormax-triple-black-2pt0",
			"https://stockx.com/nike-air-max-1-atmos-2017",
			"https://stockx.com/nike-air-max-97-off-white",
			"https://stockx.com/nike-air-max-1-master",
			"https://stockx.com/nike-air-vapormax-dark-grey",
			"https://stockx.com/nike-air-max-97-ultra-17-skepta",
			"https://stockx.com/nike-air-max-1-ultra-sport-red-2017",
			"https://stockx.com/nike-air-vapormax-triple-black-3pt0",
			"https://stockx.com/nike-air-max-plus-metallic-golds",
			"https://stockx.com/nike-air-vapormax-midnight-navy",
			"https://stockx.com/nike-air-max-1-anniversary-royal-2017-restock",
			"https://stockx.com/air-max-1-atmos-safari-2016",    #20
			"https://stockx.com/nike-air-max-1-anniversary-obsidian",
			"https://stockx.com/nike-air-max-97-og-black-volt",
			"https://stockx.com/nike-air-max-98-gundam-2018",
			"https://stockx.com/nike-nike-air-max-1-sport-royal-2017",
			"https://stockx.com/nike-air-vapormax-clot-bright-crimson",
			"https://stockx.com/nike-air-vapormax-be-true-2017",
			"https://stockx.com/nike-air-vapormax-og-white-red",
			"https://stockx.com/nike-air-max-90-ultra-flyknit-2pt0-infrared",
			"https://stockx.com/nike-air-max-97-silver-bullet-2016-w",
			"https://stockx.com/nike-air-max-97-country-camo-usa",          #30
			"https://stockx.com/nike-air-max-97-summit-white",  
			"https://stockx.com/air-max-90-og-infrared-2015",
			"https://stockx.com/nike-air-max-plus-silver-bullet",
			"https://stockx.com/nike-air-vapormax-copper",
			"https://stockx.com/nike-air-max-90-ultra-2pt0-doernbecher-oregon-ducks"]  #35

#####Use scrapy shell to test if xpath works
#####Typed the following: 

csv_file = open('SNeakers_StockX.csv', 'w')
writer = csv.writer(csv_file)
writer.writerow(['Model','Color','Retail_Price', 'Release_Date', 'Price_Premium', 'Avg_Sale_Price', 'Date of Sale', 'Time of Sale', 'Sneaker Size', 'Sale Price'])



def SneakersInfoScraper():
	time.sleep(2)


	Model_name = driver.find_element_by_xpath('//h1[@class="name"]').text
	#Retrieves the name of the Model
	print(Model_name)
	print('='*50)

	Color_Sneaker = driver.find_element_by_xpath('//div[@class="detail"][2]/span').text
	#Retrieves the color of the sneaker
	print(Color_Sneaker)
	print('='*50)

	Retail_Price = driver.find_element_by_xpath('//div[@class="detail"][3]/span').text
	#Retrieves the release date of the model
	print(Retail_Price)
	print('='*50)

	Release_date = driver.find_element_by_xpath('//div[@class="detail"][4]/span').text
	#Retrieves the release date of the model
	print(Release_date)
	print('='*50)


#####{ OTHER PRICE INFO ABOUT SNEAKER }#####

	OtherPriceInfo = driver.find_elements_by_xpath('//div[@class="gauges"]')

	for Each_Price_Info in OtherPriceInfo:

		Price_Premium = Each_Price_Info.find_element_by_xpath('.//div[@class="gauge-container"][2]//div[@class="gauge-value"]').text
		print(Price_Premium)
		print('='*50)

		Avg_Sale_Price = Each_Price_Info.find_element_by_xpath('.//div[@class="gauge-container"][3]//div[@class="gauge-value"]').text
		print(Avg_Sale_Price)
		print('='*50)



#####{ SALES HISTORY OF SNEAKER }#####

	driver.find_element_by_xpath('//div[@class="last-sale-block"]//a').click()
	#Clicks the button, "View All Sales" 

	time.sleep(3)
	#Wait time of 3 seconds before the following lines of code are executed

	try:
		button = driver.find_element_by_xpath('//div[@class="modal-content"]//button[@class="btn"]')
		if button.text == "OKAY, I UNDERSTAND":
			button.click()
	except:
		pass
	#Clicks the button, "OKAY, I UNDERSTAND"


	Sales_History = driver.find_elements_by_xpath('//table[@class="activity-table table table-condensed table-striped "]/tbody//tr')
	
	for Each_Sales_History in Sales_History: 

		Date_of_Sale = Each_Sales_History.find_element_by_xpath('./td[1]').text
		#Retrieves the date of each sale
		print(Date_of_Sale)
		print('='*50)

		Time_of_Sale = Each_Sales_History.find_element_by_xpath('./td[2]').text
		#Retrieves the time of each sale 
		print(Time_of_Sale)
		print('='*50)

		Size_Sneaker = Each_Sales_History.find_element_by_xpath('./td[3]').text
		#Retrieves the size of each sneaker sold
		print(Size_Sneaker)
		print('='*50)

		Sale_Price = Each_Sales_History.find_element_by_xpath('./td[4]').text
		#retrieves the price of each sneaker sold
		print(Sale_Price)
		print('='*50)


		Sneakers_dict = {}


		Sneakers_dict['Model'] = Model_name
		Sneakers_dict['Color'] = Color_Sneaker
		Sneakers_dict['Retail_Price'] = Retail_Price
		Sneakers_dict['Release_Date'] = Release_date
		Sneakers_dict['Price_Premium'] = Price_Premium
		Sneakers_dict['Avg_Sale_Price'] = Avg_Sale_Price
		Sneakers_dict['Date_of_Sale'] = Date_of_Sale
		Sneakers_dict['Time_of_Sale'] = Time_of_Sale
		Sneakers_dict['Size_Sneaker'] = Size_Sneaker
		Sneakers_dict['Sale_Price'] = Sale_Price
		writer.writerow(Sneakers_dict.values())


try:


	for each_url in long_url_list:
		driver.get(each_url)
		SneakersInfoScraper()

except Exception as e:
	print(e)
	csv_file.close()
	driver.close()


#####Open command line. Type the following
#Go the folder "WebScrapingProject" where you have 'setup.py' saved then type to see if this spider works/scrape info:
#       python setup.py
