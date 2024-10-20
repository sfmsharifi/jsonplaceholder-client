import requests
from typing import List, Dict
import json

class APIClient:
    # Base URL for the JSONPlaceholder API
    URL: str = "https://jsonplaceholder.typicode.com"

    # Fetches and returns a list of users, albums and posts from the API
    def get_users(self) -> List[Dict]:
        response = requests.get(self.URL + "/users")
        response.raise_for_status()  # Check if the request was successful
        return response.json()  # Return the JSON content as Python objects
    
    def get_albums(self) -> List[Dict]:
        response = requests.get(self.URL + "/albums")
        response.raise_for_status() 
        return response.json()  

    def get_posts(self) -> List[Dict]:
        response = requests.get(self.URL + "/posts")
        response.raise_for_status()  
        return response.json()  


api_client = APIClient()  # Create an instance of the APIClient class

# Fetch and display the list of users, albums and posts
users = api_client.get_users()
print("Here are the users we found:")
print(json.dumps(users, indent=2))  # Use indentation to create a more visually clear and readable output

albums = api_client.get_albums()
print("\nAnd here are the albums:")
print(json.dumps(albums, indent=2)) 

posts = api_client.get_posts()
print("\nFinally, these are the posts:")
print(json.dumps(posts, indent=2))  
