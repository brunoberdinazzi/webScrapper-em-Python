import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

def scrape_and_save_data(url):
    try:
        # Realize a raspagem da web 
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            # Extraia os dados desejados do site
            # Conecte-se ao banco de dados MongoDB
            client = MongoClient("mongodb://localhost:27017")
            db = client["web_scraper_db"]
            collection = db["web_scraper_db"]
            client.close()
            return True
        else:
            return False
    except Exception as e:
        print(f"Erro na raspagem e salvamento: {str(e)}")
        return False
