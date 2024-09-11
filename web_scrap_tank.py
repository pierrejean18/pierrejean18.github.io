import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import csv

URL ="https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html"

response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    def extract_tank_info(text):
        pattern = re.compile(r'\(([^,]+), ([^)]+)\)')
        matches = pattern.findall(text)
        return matches
    tank_links = {}
    tank_sections = soup.find_all('ul')
    
    for section in tank_sections:
        tank_items = section.find_all('li')
        
        for tank_item in tank_items:
            tank_info_text = tank_item.text.strip()
            if ':' in tank_info_text:
                tank_model, tank_details = tank_info_text.split(':', 1)
                tank_model = tank_model.strip()
            else:
                tank_model = tank_info_text.strip()
                tank_details = ""
            
            tanks = extract_tank_info(tank_details)
            
            links = tank_item.find_all('a', href=True)
            
            if tank_model not in tank_links:
                tank_links[tank_model] = []
            
            for (tank_id, tank_status), link in zip(tanks, links):
                tank_links[tank_model].append((tank_status.strip(), link['href']))
    
    with open('tank_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Modèle du tank", "État du tank", "Lien vers l'image ou vidéo"])
        
        for tank_model, tanks in tank_links.items():
            for tank_status, link in tanks:
                writer.writerow([tank_model, tank_status, link])

    print("Les données des tanks ont été enregistrées dans 'tank_data.csv'.")

else:
    print("La requête a échoué avec le code :", response.status_code)

