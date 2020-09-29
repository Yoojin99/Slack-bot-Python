# Python으로 Slack bot 만들기

여기는 slack 채널에 간단한 메세지를 올릴 수 있는 bot이 작동할 수 있도록 파이썬으로 코드를 작성하는 방법, 그리고 그에 필요한 slack app 생성에 대해 설명이 있습니다.

## 목차

* [Slack app 만들기](#slack-appbot-만들기)
* [Python code 작성하기](#python-코드-작성)

## Slack app(bot) 만들기

Slack app(bot)을 만들기 전에 두 가지 유형으로 나뉠 거 같습니다.

1. 저처럼 이것저것 시도하다가 이미 slack app을 slack api 사이트에서 만들어버림
2. 아직 slack api에서 app을 만들지 않음

### 1. 아직 slack app을 만들지 않은 경우

Slack의 왼쪽에 보면 현재 속해 있는 곳이 있고, 그 오른쪽에 작은 화살표가 있습니다. 이것을 눌러 **Administration->Manage apps**를 눌러줍니다.

![image](https://user-images.githubusercontent.com/41438361/94521353-dea2d600-0268-11eb-8520-bf762712a35e.png)

잠시 기다리면 새로운 웹 창이 뜨면서 아래와 같은 화면이 나타납니다.

![image](https://user-images.githubusercontent.com/41438361/94521922-c3849600-0269-11eb-8531-1b895d15f61f.png)

초록색으로 바운딩한 창에 `webhook`을 검색해주고, **Incoming WebHooks**를 선택해줍니다.

![image](https://user-images.githubusercontent.com/41438361/94522075-021a5080-026a-11eb-8b66-59173cbb9625.png)

그리고 **Add to Slack** 버튼을 눌러줍시다.

![image](https://user-images.githubusercontent.com/41438361/94522219-4148a180-026a-11eb-829a-e90e6d69c1bd.png)

Slack 봇이 메세지를 올릴 **채널을 선택**하고, 밑에 **Add Incoming WebHooks integration** 버튼을 클릭해줍니다.

![image](https://user-images.githubusercontent.com/41438361/94522364-7f45c580-026a-11eb-9507-f70d894fbb0e.png)

그러면 이제 **Webhook URL**이 생성된 것을 확인할 수 있습니다.

![image](https://user-images.githubusercontent.com/41438361/94522594-d9468b00-026a-11eb-8791-c92a37eb3226.png)

밑으로 쭉쭉 내리면 봇을 커스터마이징 할 수 있는 곳이 나옵니다. 이름, 이미지 등등을 설정하고 **Save Settings**를 눌러줍니다.

![image](https://user-images.githubusercontent.com/41438361/94522719-0b57ed00-026b-11eb-8392-786a041023e6.png)

이제 만들어진 slack bot이 정상적으로 작동하는지 확인하겠습니다.

cmd 창을 열어서 

```
curl -X POST -d "payload={\"text\": \"Hello\"}" [webhookurl]
```

을 입력합시다. 저 webhookurl 자리에는 아까 생성한 webhook url을 넣으면 되겠습니다.

그러면 아래와 같이 설정한 채널에 bot이 메세지를 올리는 것을 확인할 수 있습니다. Hello가 정상적으로 출력된 것이고, 그 위에 BAD 뭐뭐뭐는 한글을 입력했을 때 발생한 문제입니다. 물론 python 코드에서 slack bot이 한글 메세지를 보내게 했을 때는 정상적으로 잘 출력됩니다.

![image](https://user-images.githubusercontent.com/41438361/94523408-1bbc9780-026c-11eb-9a88-75f90ff5ff4d.png)

그럼 이제 python 코드를 작성할 준비가 다 된 것입니다.

### 2. 이미 slack app을 만든 경우

[slack api 사이트](https://api.slack.com/)에 접속해서 오른쪽 상단의 **Your apps** 를 클릭해줍니다.

![image](https://user-images.githubusercontent.com/41438361/94524118-23307080-026d-11eb-9f9d-aceb33c6e881.png)

그러면 이미 만들어진 봇이 있을 것입니다. 원하는 봇을 클릭해줍시다. 물론 새로운 봇을 만들어서 진행해도 괜찮습니다.

![image](https://user-images.githubusercontent.com/41438361/94524546-b669a600-026d-11eb-9f1c-1d56c02065d9.png)

왼쪽의 Feature 탭의 **Incoming Webhooks**에 들어가 줍니다. 만약 Incoming Webhook을 활성화를 해주지 않았다면 해주면 됩니다. 그러면 아래에 Webhook URLs for Your Workspace라고 똑같이 cmd 창에서 테스트 해 볼 수 있는 커맨드가 나옵니다.

![image](https://user-images.githubusercontent.com/41438361/94524737-f761ba80-026d-11eb-9302-c99476dbe317.png)

아래로 내려보면 Webhook URL만 따로 확인할 수 있습니다. 위의 커맨드에 포함되어 있는 webhook url을 따로 복사해도 됩니다.

![image](https://user-images.githubusercontent.com/41438361/94524910-3a239280-026e-11eb-94d2-0a311460e5f7.png)

만약 webhook url이 없다면 아래에 Add new webhook to workspace 버튼을 클릭해서 추가해도 됩니다.

파이썬 코드에서는 이 webhook url을 이용하니 복사해두고 저장합시다.

---

## Python 코드 작성

코드는 정말 간단합니다. 위에서 생성한 webhook url을 복사하여 붙여넣고, payload(전달할 텍스트를 담은 것)을 작성한 후에 request를 이용하여 보내면 됩니다.

전체적인 코드는 이미 `BasicSlackbot.py` 로 업로드 해놓았으니 그대로 복사해서 양식만 고쳐서 이용하셔도 됩니다.

python3가 아닌 2버전을 이용하고 있는 분들은 맨 위에 `# -*- coding: utf8 -*- ` 를 추가해주세요.

```python
# -*- coding: utf8 -*- 

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
```

위의 `Webhookurl`에 아까 복사한 webhook url로 덮어씌우 주고, `text` 부분에 원하는 포맷으로 텍스트를 작성합니다. 그리고 이 python 코드를 실행시키면 해당 텍스트를 처음에 설정한 slack 채널에 봇이 메세지로 보낸 것을 확인할 수 있을 것입니다.

