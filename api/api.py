import requests
import os
from dotenv import load_dotenv

load_dotenv()

endpoint = "https://api.themoviedb.org/3/"

headers: dict[str, str] = {
    "accept": "appliaction/json", 
    "Authorization": f"Bearer {os.getenv("ACCESS_TOKEN")}"
}

def movie_lookup(title: str):
    url: str = endpoint + f"search/movie?query={title}"
    try:
        response: requests.Response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        return data
    except requests.RequestException as e:
        print(e)

if __name__ == "__main__":
    movie_lookup("Avatar")