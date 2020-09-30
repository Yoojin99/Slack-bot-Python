# Slack-bot-Python
:robot:Slack bot with python. Get data directly by using bigquery with python. Write/Read data into/from Google spreadsheet.📊 

## 소개

### 이걸 할 수 있어요

1. **Python으로 Slack bot 만들기**. 원하는 특정 시간에 원하는 메세지를 보내는 슬랙봇을 만들 수 있습니다.
2. **Bigquery의 데이터를 third-party를 이용하지 않고 Python으로 가져오기**.
3. **Google Spreadsheet에 python으로 데이터 읽기/쓰기**

### 폴더 및 파일 설명

```
.
├── 1. Basic Python Slack Bot
│   └── BasicSlackBot.py # 기본 슬랙 파이썬 봇. 간단한 텍스트를 설정하여 슬랙에 보냅니다.
├── 2. Python-Bigquery 
│   └── BigqueryBot.py # Bigquery 데이터를 python을 이용하여 바로 가져옵니다.
└── 3. Python-Google Spreadsheet
    └── SpreadsheetBot.py # Google spreadsheet에 데이터를 쓰거나, 데이터를 읽습니다.
```

### 따라하기 및 설명

:closed_book: [1. Basic Python Slack Bot](https://github.com/Yoojin99/Slack-bot-Python/tree/master/1.%20Basic%20Python%20Slack%20Bot)

:orange_book: [2. Python-Bigquery](https://github.com/Yoojin99/Slack-bot-Python/tree/master/2.%20Python-Bigquery)

:ledger: [3. Python-Google Spreadsheet](https://github.com/Yoojin99/Slack-bot-Python/tree/master/3.%20Python-Google%20Spreadsheet#2-python-code-%EC%9E%91%EC%84%B1)

:green_book: [4. All-in-one Bot]()

### 이걸 만들게 된 이유

Bigquery의 데이터를 Slack에 올리는 bot을 만드는 작업을 했습니다. 

기존에는 

> *Bigquery의 데이터를 Google Spreadsheet로 OWOX를 이용해서 가져오고, 가져온 데이터를 Google Spreadsheet 내에서 또 하나의 시트로 합치고, 데이터가 업데이트 될때마다 Zapier.io /  Automate.io 라는 사이트를 이용해서 slack과 연동하여 slack에 메세지를 업로드*

하는 방법을 사용했습니다.

정말 복잡하고 쓸데없이 third-party 앱을 자주 사용하는 방법입니다. 심지어 Bigquery에서 Google Spreadsheet로 데이터를 가져오기 위해 사용하는 OWOX라는 third-party 앱도 에러가 발생하는 경우가 있습니다. 

그래서 third-party 앱을 사용하지 않도록 slack bot을 python으로 구현했습니다. 구현하면서 **한글 자료의 부재와 자료 자체가 없는 것을 심각하게 느껴** 한글 자료가 있으면 좋을 것 같아 기록으로 남깁니다.

시간이 된다면 기존에 이용한 위의 방법을 하는 방법도 정리할 생각입니다.
