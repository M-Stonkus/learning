from bs4 import BeautifulSoup
import requests

#Scrapes the list of top 100 movie by empire
#Enjoyed them, but how are Marvel movies on here

data=requests.get("https://www.empireonline.com/movies/features/best-movies-2/").text

soup=BeautifulSoup(data, "html.parser")

movie_list = [movie.text for movie in soup.select("h2 strong")]
movie_list = movie_list[::-1]
with open("movies.txt", 'a') as file:
    #Clears previous entries
    file.seek(0)
    file.truncate()
    #Writes data
    for movie in movie_list:
        file.write(f"{movie} n")