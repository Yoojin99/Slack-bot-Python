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