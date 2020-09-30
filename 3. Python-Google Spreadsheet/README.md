# Python과 Bigquery 연동하기, Bigquery에서 python으로 데이터 가져오기

## 목차

1. [사용자 키 파일 가져오기](#1-사용자-키-파일-가져오기)
2. [파이썬 코드 작성](#2-python-코드-작성)


## 1. `credentials.json` 파일 다운받기

Python 코드를 통해 Google 스프레드 시트에 접근하려면, 새로운 Google cloud platform 프로젝트를 만들고, Google Sheets API를 활성화시켜야 합니다.

이미 Cloud platform 프로젝트가 있다는 가정하에, google sheets API를 활성화 시켜줘야 합니다.

[여기](https://developers.google.com/sheets/api/quickstart/python)로 가서 아래의 버튼을 클릭해줍니다.

![image](https://user-images.githubusercontent.com/41438361/94396222-7090dd00-019c-11eb-8d96-85ed64a25ca4.png)

버튼을 클릭하면, 이 화면이 나옵니다. 'Back' 버튼을 눌러줍시다.

![image](https://user-images.githubusercontent.com/41438361/94396373-bcdc1d00-019c-11eb-82a9-2f97566e5a98.png)

그리고 cloud platform 프로젝트를 선택한 후 '다음' 버튼을 눌러줍시다.

![image](https://user-images.githubusercontent.com/41438361/94396471-f3199c80-019c-11eb-868d-2248d45480d1.png)

'생성' 버튼을 눌러 credentials 파일을 만들어줍니다.

![image](https://user-images.githubusercontent.com/41438361/94396656-599eba80-019d-11eb-8894-0ae09afcf504.png)

그러면 이제 client configuration 파일을 다운받을 수 있습니다.

![image](https://user-images.githubusercontent.com/41438361/94396781-a2ef0a00-019d-11eb-9ca7-95d023ec9d16.png)

다운받고, 코드가 있는 폴더에 위치시켜줍시다.

### + 구글 클라이언트 라이브러리 설치

만약 로컬 환경(google cloud functions 이외의 환경) 에서 파이썬 코드를 실행시킨다면, 필요한 라이브러리를 설치해야 합니다.

아래의 코드를 cmd 창에 입력해줍시다.

```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

## 2. Python code 작성

먼저 필요한 라이브러리들을 import 해줍니다.

```python
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
```

그리고 Google spreadsheet api를 이용하기 위해 필요한 정보들을 적어줍니다.

`SPREADSHEET_ID` 는 스프레드 시트 링크 주소가 만약 아래와 같이 되어있다면 d 이후부터 / 전까지입니다.

`https://docs.google.com/spreadsheets/d/[여기 이 부분이 ID입니다]/어쩌구 저쩌구`

`RANGE_NAME` 에서 볼 수 있듯이 `cat!A2:E` 는 `cat`이라는 스프레드 시트(working sheet)의 A2부터 E열 까지를 의미합니다.

따라서 `cat` 부분에는 현재 작업하는 working sheet의 이름을 적어주면 되겠습니다. 범위도 원하는대로 수정하면 됩니다.

```python
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '어쩌구저쩌구'
# if your spread sheet name is 'cat' and range you want to print is 'A2:E'
RANGE_NAME = 'cat!A2:E'
```

먼저 데이터 읽기 부분입니다. 여기에서는 바로 위에서 정한 `RANGE_NAME`에 해당하는 부분의 데이터를 읽어옵니다.

읽어오는 데이터를 처리하는 부분은 `# print your data` 주석 이후에 나와 있습니다.

참고로 이 코드에서는 읽기를 A2부터 E열까지 읽어왔기 때문에 row[0]는 A열에 있는 값, row[1]는 B열에 있는 값,
row[2]는 C열, row[3]는 D열, row[4]는 E열의 값이 됩니다.

```python
def read_data():
  # prints values from spreadsheet

  creds = None
  # The file token.pickle stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists('token.pickle'):
      with open('token.pickle', 'rb') as token:
          creds = pickle.load(token)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
          creds.refresh(Request())
      else:
          flow = InstalledAppFlow.from_client_secrets_file(
              'credentials.json', SCOPES)
          creds = flow.run_local_server(port=0)
      # Save the credentials for the next run
      with open('token.pickle', 'wb') as token:
          pickle.dump(creds, token)

  service = build('sheets', 'v4', credentials=creds)

  # Call the Sheets API
  sheet = service.spreadsheets()
  result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                              range=RANGE_NAME).execute()
  values = result.get('values', [])

  # print your data
  if not values:
      print('No data found.')
  else:
      print('Lets print:')
      for row in values:
          # Print columns A and E, which correspond to indices 0 and 4.
          print('%s, %s' % (row[0], row[4]))
```

그리고 아래는 스프레드 시트에 데이터를 쓰는 부분입니다.

마찬가지로 `worksheet_name`에는 working sheet의 이름, `cell_range_insert`에는 값을 쓰기 시작하는 위치를 적습니다.

`values` 에는 쓰고 싶은 값들을 적습니다. 즉 아래와 같이 코드를 작성하면 스프레드 시트에는 아래와 같이 값이 써지게 됩니다.

![image](https://user-images.githubusercontent.com/41438361/94702074-53b10100-0378-11eb-8808-d05c77d42c1e.png)

이미지에서 확인할 수 있듯이 ''는 ''값으로 해당 셀을 덮어씌웁니다.

참고로 스프레드 시트에 값을 쓰게 되면 원래 해당 셀에 있는 함수도 없어지게 됩니다. 그러므로 셀에 값을 덮어씌울 때는 함수가 적용되지 않은 셀에 덮어씌우는 것을 추천합니다.

```python
def write_data():

    creds = None

    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # your sheet name
    worksheet_name = 'cat!'
    # start point you want to write data
    cell_range_insert = 'B2'

    # values you want to write
    values = [
        ['Col A', '' ,'Col B', 'Col C', 'Col D'],
        ['Apple', 'Orange', 'Watermelon', 'Banana']
    ]

    value_range_body = {
        'majorDimension': 'ROWS',
        'values': values
    }

    service.spreadsheets().values().update(
        spreadsheetId=SAMPLE_SPREADSHEET_ID,
        valueInputOption='USER_ENTERED',
        range=worksheet_name + cell_range_insert,
        body=value_range_body
    ).execute()
```
