#!/usr/bin/env python3

# from androidhelper import sl4a
from bs4 import BeautifulSoup
import re
import requests

NEWS_URL = "http://tagesschau.de"


def fetch_news():
    response = requests.get(NEWS_URL)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")

    news = []

    items = soup.find_all("div", class_="teaser")
    for item in items:
        title = item.find("h4", class_="headline")
        description = item.find("p", class_="teasertext")
        if title is not None and description is not None:
            title = title.text
            description = description.text
            description = re.sub("mehr$", "", description)

            news.append({
                "title": title,
                "description": description
            })

    return news


def read_instructions():
    "commands include next, more, stop, nothing"
    pass


def speak(text):
    pass


def listen():
    pass


if __name__ == "__main__":

    news = fetch_news()
    print(news)

    # for item in news:

    #     speak(item["title"])

    #     command = listen()
    #     command = command.lower()

    #     if command in ["more"]:
    #         speak(item["description"])
    #     elif command in ["next", "", None]:
    #         continue
    #     elif command in ["stop"]:
    #         break

    # speak("I am done speaking!")
