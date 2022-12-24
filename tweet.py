#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session

# Consumer Key
CK = 'zUGK2KtdmEZHQOUXXltivp1x5'
# Consumer Secret
CS = 'q0R53WXLQ3pfoFh0U8P6hT8KXcOm6R38Kh88pgPXjdhrNy98W6'
# Access Token
AT = '744114337-I1ijGMXt9FaODBpBuAvR0qHrwUExdbibLCKcJAWV'
# Accesss Token Secert
AS = '6bEgAjRqxwZmKoK8gLGm17kUsVL3hGejO0iEx3UMBQyoj'

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

# ツイート本文
if __name__ == '__main__':
    tweet_publish = raw_input('Tweet: ')
    params = {"status": tweet_publish}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.post(url, params = params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)
