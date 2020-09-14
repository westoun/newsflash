#!/usr/bin/env python3

from androidhelper import sl4a
from bs4 import BeautifulSoup
import re
import requests

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMPLEMENTOFDEFAULT"

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


def speak(droid, text):
    droid.ttsSpeak(text)


def listen(droid):
    try:
        result = droid.recognizeSpeech()[1]
        return result
    except Exception as e:
        print(str(e))


if __name__ == "__main__":

    droid = sl4a.Android()

    news = fetch_news()

    for item in news:

        speak(droid, item["title"])

        command = listen(droid)
        command = command.lower()

        if command in ["more"]:
            speak(item["description"])

        elif command in ["next", "", None]:
            continue

        elif command in ["stop"]:
            break

    speak(droid, "I am done speaking!")
