import requests
import os
from dotenv import load_dotenv

load_dotenv()

endpoint = "https://api.themoviedb.org/3/"

headers: dict[str, str] = {
    "accept": "appliaction/json", 
    "Authorization": f"Bearer {os.getenv("ACCESS_TOKEN")}"
}

def fetch_data(url: str):
    try:
        response: requests.Response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        return data
    except requests.RequestException as e:
        print(e)

def movie_title_lookup(title: str):
    url: str = endpoint + f"search/movie?query={title}"

    data = fetch_data(url)
        
    return data.get("results")

def get_movie_details(movie_id: int):
    url: str = endpoint + f"movie/{movie_id}"

    data = fetch_data(url)

    return data

if __name__ == "__main__":
    movie_title_lookup("Avatar")
    get_movie_details(75780)