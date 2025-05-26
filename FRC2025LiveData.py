import requests
import time

API_TOKEN = ''
BASE_URL = 'https://frc-api.firstinspires.org/v3.0'

def get_competition_data(year, event_code):
    headers = {
        'Authorisation': f'Bearer {API_TOKEN}',
        'Accept': 'application/json'
    }
    
    url = f'{BASE_URL}/{year}/events/{event_code}/matches'
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None

def continuously_update_match_data(year, event_code, update_interval=10):
    while True:
        competition_data = get_competition_data(year, event_code)
        
        if competition_data:
            print("Updated Competition Data:")
            for match in competition_data['Matches']:
                print(f"Match {match['matchNumber']}: {match['description']}")
        else:
            print("No data found")
        
        time.sleep(update_interval)

year = 2025
event_code = ''
continuously_update_match_data(year, event_code)