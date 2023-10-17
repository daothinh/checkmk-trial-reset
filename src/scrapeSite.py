import requests
from bs4 import BeautifulSoup
from colors import red, green, yellow
import sys



def scrapeWeb(host, site):  # Fetches remaining time
    hosts = host
    sites = site
    time = 'time'
    scrape_url = f'http://{hosts}/{sites}/check_mk/login.py'  # URL for the login page to be scraped for infos
    try:
        response = requests.get(scrape_url)
        response.raise_for_status()  # Check status HTTP
        soup = BeautifulSoup(response.content, 'html.parser')

        remaining_time_elements = soup.find_all(class_="remaining_time")  # Searches for the class remaining_time

        remaining_times = [element.get_text() for element in remaining_time_elements]

        for remaining_time in remaining_times:  # Saves into remaining_time
            remaining_time = remaining_time
            with open(time, 'w') as file:  # Writing time to file for the service to use
                file.write(remaining_time)
            numeric_part = ''.join(filter(str.isdigit, remaining_time))  # Searches for digits in the string and saves them used for comparison
            number = int(numeric_part)

            if number >= 20:  # Visuals for printouts
                return green + remaining_time
            elif 20 > number >= 10:
                return yellow + remaining_time
            elif number < 10:
                return red + remaining_time
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        sys.exit(1)
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


def scrapeVers(host, site):	#fetches version
	hosts = host
	sites = site
	scrape_url = f'http://{hosts}/{sites}/check_mk/login.py' #login page to scrape
	response = requests.get(scrape_url)

	soup = BeautifulSoup(response.content, 'html.parser')

	foot_element = soup.find(id = "foot")	#search for the id foot

	if foot_element:
		foot_text = foot_element.get_text()	#extract the text
		version = foot_text.split(':')[1].split('-')[0].strip() #strip the part i want 
		return version