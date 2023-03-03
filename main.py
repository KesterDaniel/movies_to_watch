import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

movie_titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]

for i in range(1, len(movie_titles)+1):
    with open("movies.txt", "a", encoding="utf-8") as movie_file:
        movie_file.write(f"{movie_titles[-i]}\n")






