def tweet(text):
  path_to_key='./key.json'
  from requests_oauthlib import OAuth1Session
  import time
  from collections import Counter
  import sys
  import json

  key_json=open(path_to_key,'r')
  key=json.load(key_json)

  CK=format(key['Consumer Key (API Key)'])
  CS=format(key['Consumer Secret (API Secret)'])
  AT=format(key['Access Token'])
  AS=format(key['Access Token Secret'])

  #投稿先URL
  url = "https://api.twitter.com/1.1/statuses/update.json"
  #ツイート内容
  params = {"status":text}
  
  #ツイート実行
  twitter = OAuth1Session(CK, CS, AT, AS)
  req = twitter.post(url,params=params)
  
  #ツイート結果表示
  if req.status_code==200:
    print("以下の内容をツイートしました : ",text)
  else:
    print("Error: %d  以下の内容をツイートできませんでした : "%req.status_code,text)

#tweet(tweet_text)
