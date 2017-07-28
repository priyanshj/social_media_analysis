import requests
from bs4 import BeautifulSoup
import pandas as pd 
import csv

#page = requests.get("https://www.tripadvisor.in/Hotel_Review-g304555-d2151631-Reviews-Jaipur_Marriott_Hotel-Jaipur_Jaipur_District_Rajasthan.html#REVIEWS")

#soup = BeautifulSoup(page.content,'html.parser')
#reviews = soup.find(id="taplc_location_reviews_list_hotels_0")
#reviews_items = reviews.find_all(class_="review-container")

print("Till now, it is working fine")

numbers = [1,2,3,4,5]

def print_numbers(digits = []):
	for num in digits:
		print(num)


print_numbers(numbers)

def web_scrapper(pages = [],document = []):
	for page in pages:
		page_load = requests.get(page)
		print("page is loaded sucessfully")

		soup = BeautifulSoup(page_load.content,'html.parser')
		reviews = soup.find(id="taplc_location_reviews_list_hotels_0")
		reviews_items = reviews.find_all(class_="review-container")

		#document = []
		review_tags = reviews.select(".partial_entry")

		for rt in review_tags:
			document.append(rt.get_text())

	trivago_reviews = pd.DataFrame({"Hotel":"Hotel review",
			"Review":document
			})

	trivago_reviews.to_csv("my_file.csv")
			#print(rt.get_text())

		#print("task complete")


web_pages = ["https://www.tripadvisor.in/Hotel_Review-g304555-d2151631-Reviews-Jaipur_Marriott_Hotel-Jaipur_Jaipur_District_Rajasthan.html#REVIEWS",
             "https://www.tripadvisor.in/Hotel_Review-g297668-d618917-Reviews-Ranbanka_Palace-Jodhpur_Jodhpur_District_Rajasthan.html",
              "https://www.tripadvisor.in/Hotel_Review-g317096-d2238110-Reviews-Country_Inn_Suites_By_Carlson_Ajmer-Ajmer_Ajmer_District_Rajasthan.html",
              "https://www.tripadvisor.in/Hotel_Review-g317096-d9789718-Reviews-Hotel_KC_Inn-Ajmer_Ajmer_District_Rajasthan.html",
              "https://www.tripadvisor.in/Hotel_Review-g317096-d302386-Reviews-Bijay_Niwas_Palace-Ajmer_Ajmer_District_Rajasthan.html",
              "https://www.tripadvisor.in/Hotel_Review-g297672-d1853086-Reviews-Radisson_Blu_Udaipur_Palace_Resort_Spa-Udaipur_Udaipur_District_Rajasthan.html",
              "https://www.tripadvisor.in/Hotel_Review-g297672-d530387-Reviews-The_Lalit_Laxmi_Vilas_Palace_Udaipur-Udaipur_Udaipur_District_Rajasthan.html",
              "https://www.tripadvisor.in/Hotel_Review-g297672-d481923-Reviews-Hotel_Lakend-Udaipur_Udaipur_District_Rajasthan.html",
              "https://www.tripadvisor.in/Hotel_Review-g297668-d1597518-Reviews-The_Ummed_Jodhpur-Jodhpur_Jodhpur_District_Rajasthan.html",
              "https://www.tripadvisor.in/Hotel_Review-g297668-d7985097-Reviews-Lords_Inn_Jodhpur-Jodhpur_Jodhpur_District_Rajasthan.html",
              "https://www.tripadvisor.in/Hotel_Review-g304555-d307723-Reviews-Alsisar_Haveli-Jaipur_Jaipur_District_Rajasthan.html",
              "https://www.tripadvisor.in/Hotel_Review-g304555-d1027166-Reviews-Ramada_Jaipur-Jaipur_Jaipur_District_Rajasthan.html",
              "https://www.tripadvisor.in/Hotel_Review-g297667-d1754988-Reviews-Mystic_Jaisalmer_Hotel-Jaisalmer_Jaisalmer_District_Rajasthan.html",
              "https://www.tripadvisor.in/Hotel_Review-g297667-d1161971-Reviews-Hotel_Pleasant_Haveli-Jaisalmer_Jaisalmer_District_Rajasthan.html",
              "https://www.tripadvisor.in/Hotel_Review-g297667-d3584969-Reviews-Chokhi_Dhani_The_Palace_Hotel-Jaisalmer_Jaisalmer_District_Rajasthan.html",
              "https://www.tripadvisor.in/Hotel_Review-g297666-d306921-Reviews-Karni_Bhawan_Palace-Bikaner_Bikaner_District_Rajasthan.html",
              "https://www.tripadvisor.in/Hotel_Review-g297666-d2061352-Reviews-Hotel_Kishan_Palace-Bikaner_Bikaner_District_Rajasthan.html",
              "https://www.tripadvisor.in/Hotel_Review-g297666-d735550-Reviews-Hotel_Desert_Winds-Bikaner_Bikaner_District_Rajasthan.html",
              "https://www.tripadvisor.in/Hotel_Review-g319729-d1508094-Reviews-Hotel_Prem_Villas-Pushkar_Ajmer_District_Rajasthan.html",
              "https://www.tripadvisor.in/Hotel_Review-g319729-d8118197-Reviews-Hotel_Raj_Garden-Pushkar_Ajmer_District_Rajasthan.html"]

doc = []
web_scrapper(web_pages,doc)