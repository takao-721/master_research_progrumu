# -*- coding: utf-8 -*-
#ツイートをエクセルファイルに出力する
import tweepy
import csv
import MeCab
import oseti
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, preprocessing
from sklearn.cluster import KMeans

# TweepyAPI KEY
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

#tweepyの設定
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#ここで取得したいツイッターアカウントIDを指定する
q = "mochimochi_2go"
#10個までしかさかのぼれない
count = 10

tweet_list=[]

# アナライザー
analyzer = oseti.Analyzer()

fav_cou=0
ret_cou=0
#ツイート取得
tweets = api.search(q=q, locale="ja", count=count,tweet_mode='extended')
for tweet in tweets:
    tweet.full_text=tweet.full_text.split()
    #print(tweet_list)
    tweet_list.append([tweet.full_text])
    fav_cou=fav_cou+tweet.favorite_count
    ret_cou=ret_cou+tweet.retweet_count

#エクセルファイル作成
#with open("Tweets_data_stack.csv", "w", encoding="utf-8") as f:
#    writer = csv.writer(f,  lineterminator="\n")
#    writer.writerow(tweet_list)
#print(tweet_list)
for tweet in tweet_list:
    for a in tweet:
        if "納豆" in a:
            print("不正なユーザです")


analysis = []
counter=0.0
loop_counter=0
for text in tweet_list :
    text =str(text).lower()
    tagger = MeCab.Tagger("-Owakati")
    parse = tagger.parse(text)
    counter=counter+float(sum(analyzer.analyze(parse))/float(len(list(analyzer.analyze(parse)))))
    analysis.append(analyzer.analyze_detail(parse))
    loop_counter=loop_counter+1

print("いいね：",fav_cou)
print("リツイート：",ret_cou)
print("ポジネガ：",counter/loop_counter)

