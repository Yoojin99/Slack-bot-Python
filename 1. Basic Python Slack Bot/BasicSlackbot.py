# -*- coding: utf8 -*- 

import datetime

import requests

def slack_data() :
    # write your webhook url here
    url = "Webhookurl"

    # replace here with data you want to send slack
    text = (
        "안녕하세요? ^^"
        )

    payload = {
        "text": text
    }

    requests.post(url, json=payload)

if __name__ == "__main__":
    slack_data()