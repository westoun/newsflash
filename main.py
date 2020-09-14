#!/usr/bin/env python3

from androidhelper import sl4a
from bs4 import BeautifulSoup
import re
import requests
from time import sleep

NEWS_URL = "http://tagesschau.de"
NEXT_COMMANDS = ["weiter"]
MORE_COMMANDS = ["mehr"]
STOP_COMMANDS = ["stopp"]

# The following line became necessary when running on android.
# More information on this fix can be found at "https://github.com/qpython-android/qpython3/issues/61"
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMPLEMENTOFDEFAULT"


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


def speak(droid, text):
    droid.ttsSpeak(text)


def listen(droid):
    while droid.ttsIsSpeaking()[1]:
        sleep(0.5)

    try:
        result = droid.recognizeSpeech()[1]
        return result
    except Exception as e:
        print(str(e))


if __name__ == "__main__":

    droid = sl4a.Android()

    news = fetch_news()

    speak(droid, "Bereit für Na-Na-Na-Nachrichten?!")
    speak(droid, "Unterstützte Befehle sind 'mehr', 'weiter' und 'stopp'.")

    for item in news:

        speak(droid, item["title"])

        command = listen(droid)

        if command is not None:
            command = command.lower()

        if command in MORE_COMMANDS:
            speak(droid, item["description"])
        elif command in NEXT_COMMANDS:
            continue
        elif command in STOP_COMMANDS:
            break
        else:
            continue

    speak(droid, "Habe fertig!")
