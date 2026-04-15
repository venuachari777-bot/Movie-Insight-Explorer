import requests


API_KEY = "YOUR_KEY_HERE" 

def movie_search():
    movie = input("Enter movie name: ")
    url = f"http://www.omdbapi.com/?t={movie}&apikey={API_KEY}"
    
    data = requests.get(url).json()

    if data['Response'] == 'True':
        print(f"\n Movie: {data['Title']}")
        print(f" Collections: {data.get('BoxOffice', 'N/A')}")
        print(f" Rating: {data.get('imdbRating')}")
        
        # Songs YouTube link logic
        search_query = data['Title'].replace(" ", "+")
        print(f" Songs Link: https://www.youtube.com/results?search_query={search_query}+songs,trailer")
    else:
        print("not find movie!")

movie_search()
