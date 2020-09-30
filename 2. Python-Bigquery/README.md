# Python과 Bigquery 연동하기, Bigquery에서 python으로 데이터 가져오기

## 목차

로컬에서 실행시키기 위해서는 Bigquery를 이용하기 위해 사용자 키에 대한 json 파일이 필요합니다.

만약 Google Cloud Functions나 Google Cloud Scheduler와 같이 cloud platfom console에서 실행시키는 거면 키에 대한 json 파일을 따로 저장할 필요가 없습니다.

## 1. 사용자 키 파일 가져오기

여기는 로컬에서(Google cloud platform 이외의 환경) python 코드를 실행시키기 위해 필요한 단계입니다. 

먼저, [Google cloud platform console](https://console.cloud.google.com/)에 접속하여 **API 및 서비스 -> 사용자 인증 정보** 에 들어가줍니다.

![image](https://user-images.githubusercontent.com/41438361/94689282-a59e5a80-0369-11eb-843c-217faae330de.png)

맨 밑으로 내려가면 **서비스 계정**이 있습니다. 여기에서 원하는 서비스 계정을 선택합니다.

![image](https://user-images.githubusercontent.com/41438361/94689749-37a66300-036a-11eb-8286-227c0ef4698d.png)

맨 밑으로 내려보면 **키**를 확인할 수 있습니다. 여기에서 json 파일을 다운받거나, 이전의 서비스 계정들이 나와있는 화면에서 키 json 파일을 다운받습니다.

![image](https://user-images.githubusercontent.com/41438361/94690539-36296a80-036b-11eb-9265-c941b132e86b.png)

다운받은 파일의 경로를 기억해둡시다.

## 2. Python 코드 작성

먼저 파이썬 코드를 작성하기 전에, Google cloud bigquery 라이브러리를 다운받아야 합니다.

cmd 창을 켜서, 아래의 커맨드를 입력해줍니다.

```
pip install --upgrade google-cloud-bigquery
```

예시 파이썬 코드도 `BigqueryBot.py`로 올려놓았으니 필요한 부분만 수정해서 그대로 이용하면 됩니다.

먼저 필요한 라이브러리, 함수를 import 합니다. 추가로 1.에서 받은 json 파일의 경로를 지정해주고, bigquery 프로젝트 아이디를 적습니다.

```python
from google.cloud import bigquery
from google.oauth2 import service_account
import datetime

import requests

# replace here with your json file location.
Path_to_json_file = './your-json-file-name.json'
# your bigquery project id
project_id = 'my-cat'
```

그리고 사용하고 싶은 쿼리문을 작성합니다. 쿼리문은 `"""  """` 안에 작성해주면 됩니다.

```python
# Write you bigquery here
CAT_QUERY = """
  SELECT cat
  FROM `my_heart`
"""
```

마지막으로 작성한 쿼리문을 실행시켜 얻은 결과를 `results` 에 저장하고, 이를 리스트화시켜 `data`로 저장합니다.

참고로 `data`에 있는 데이터들은 몇개를 `SELECT` 하는지에 따라 다른 length를 가집니다.

예를 들어, 만약 제가 `SELECT A, B`를 해서 A와 B를 가져왔다면 `data` 안에 있는 데이터들은 각각 길이가 2일 것입니다. 따라서 `d[0]`, `d[1]`과 같이 접근할 수 있습니다. 이때 `d[0]`은 A가 될 것이고, `d[1]`은 B가 될 것입니다.

아래의 예제에서 저는 `SELECT cat`을 하여 `cat`만 가져왔기 때문에 `d[0]`으로 `cat`을 가져올 수 있고, `d[1]`은 범위에서 벗어나는 값을 가져오게 되는 것이므로 에러가 날 것입니다.

```python
def get_data_from_bigquery(query_string, now):
    credentials = service_account.Credentials.from_service_account_file(Path_to_json_file)
    client = bigquery.Client(credentials= credentials, project=project_id)

    query_job = client.query(query_string)

    results = query_job.result()

    data = list(results)

    # Do whatever with your data. You can just check data by printing data
    for d in data:
        if d[0] == now:
            return d[1]

    return 0
```

전체 파이썬 코드입니다. 

```python
# -*- coding: utf8 -*- 

from google.cloud import bigquery
from google.oauth2 import service_account
import datetime

import requests

# replace here with your json file location.
Path_to_json_file = './your-json-file-name.json'
# your bigquery project id
project_id = 'my-cat'


# Write you bigquery here
CAT_QUERY = """
  SELECT cat
  FROM `my_heart`
"""

def get_data_from_bigquery(query_string, now):
    credentials = service_account.Credentials.from_service_account_file(Path_to_json_file)
    client = bigquery.Client(credentials= credentials, project=project_id)

    query_job = client.query(query_string)

    results = query_job.result()

    data = list(results)

    # Do whatever with your data. You can just check data by printing data
    for d in data:
        if d[0] == now:
            return d[1]

    return 0

def slack_data() :

    # write your webhook url here (for slack)
    url = "SlackWebhookurl"

    # I used datetime to get today's data. (format : 200922)
    now = datetime.datetime.now().strftime("%Y%m%d")

    cats_number = get_data_from_bigquery(CAT_QUERY, now)

    
    text = (
        "제 마음에는 {} 마리의 고양이가 살고 있습니다,, ^^".format(cats_number)
        )

    payload = {
        "text": text
    }
    
    # you can send data from bigquery to slack
    requests.post(url, json=payload)

if __name__ == "__main__":
    slack_data()
```
