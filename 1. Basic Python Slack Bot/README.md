# Python으로 Slack bot 만들기

여기는 slack 채널에 간단한 메세지를 올릴 수 있는 bot이 작동할 수 있도록 파이썬으로 코드를 작성하는 방법, 그리고 그에 필요한 slack app 생성에 대해 설명이 있습니다.

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

