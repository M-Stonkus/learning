from bs4 import BeautifulSoup
import requests
#Gets the title, url and score of the highest score post on https://news.ycombinator.com/news

#Gets html code
response = requests.get("https://news.ycombinator.com/news")
soup=BeautifulSoup(response.text, 'html.parser')

#Scrapes text, url and score of all main page articles
a_text=[a.string for a in soup.select(selector=".titleline a")[::2]]
a_link=[a.get("href") for a in soup.select(selector=".titleline a")[::2]]
a_score=[a.string for a in soup.select(selector=".score")]
score_int = [int(a.split(" ")[0]) for a in a_score]

#Finds index of article with the highest score
score_max = max(score_int)
score_max_index = score_int.index(score_max)

#Prints the title, url and score of highest score article
print(a_text[score_max_index])
print(a_link[score_max_index])
print(a_score[score_max_index])