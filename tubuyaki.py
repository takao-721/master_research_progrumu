import tweepy

# TweepyAPI KEY
CONSUMER_KEY = "45DxU9Zvx4XOitcRBYuJSofhf"
CONSUMER_SECRET = "RTjQ9dzconLULJYfg42htwfeYYYwUXNM4fFotjPPTJ0xXOnRDR"
ACCESS_TOKEN = "1257175778145366016-3UScJMtGeo3xIjBXEOGDrODPT2i0oI"
ACCESS_TOKEN_SECRET = "c3YMfn2KZBaw6N90PEcWWewH4GREhCWPcpy29jWtnif2D"

#tweepyの設定
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

api.update_status("研究は意味のあることはだいたいやられてる。実装が大変すぎて。Pythonより投稿")