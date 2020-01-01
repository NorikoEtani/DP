# -*- coding:utf-8 -*-  
from requests_oauthlib import OAuth1Session
import json
                                                                                                                                                  
oath_key_dict = {
    "consumer_key": "<Twitter API登録申請して取得した API key>",
    "consumer_secret": "<Twitter API登録申請して取得した Consumer_secret>",
    "access_token": "<Twitter API登録申請 して取得した Access_token>",
    "access_token_secret": "<Twitter API登録申請して取得した Access_secret>"
}

def searchtweet(searchstr,outfile): 
  tweets = tweet_search(searchstr, oath_key_dict)
  #出力ファイル名
  fname = r"'"+ outfile + "'"
  fname = fname.replace("'","")
  #ファイルへ出力
  with open(fname, "w",encoding="utf-8") as f:
    for tweet in tweets["statuses"]:
        tweet_id = tweet[u'id_str']
        text = tweet[u'text']
        created_at = tweet[u'created_at']
        user_id = tweet[u'user'][u'id_str']
        user_description = tweet[u'user'][u'description']
        screen_name = tweet[u'user'][u'screen_name']
        user_name = tweet[u'user'][u'name']

        f.write('\n')
        f.write(tweet_id)
        f.write('\n')

        #UnicodeEncodeErrorを避けるため
        before_text = text.encode('cp932', "ignore")
        after_text = before_text.decode('cp932')
        f.write(after_text)
        f.write('\n')

        f.write(created_at)
        f.write('\n')
        f.write(user_id)
        f.write('\n')

        #UnicodeEncodeErrorを避けるため
        before_user = user_description.encode('cp932', "ignore")
        after_user = before_user.decode('cp932')
        f.write(after_user)
        f.write('\n')

        f.write(screen_name)
        f.write('\n')

        #UnicodeEncodeErrorを避けるため
        before_uname = user_name.encode('cp932', "ignore")
        after_uname = before_uname.decode('cp932')
        f.write(after_uname)
        f.write('\n')
    f.close()
    return

def create_oath_session(oath_key_dict):
    oath = OAuth1Session(
    oath_key_dict["consumer_key"],
    oath_key_dict["consumer_secret"],
    oath_key_dict["access_token"],
    oath_key_dict["access_token_secret"]
    )
    return oath

def tweet_search(search_word, oath_key_dict):
    url = "https://api.twitter.com/1.1/search/tweets.json?"
    params = {
        "q": search_word,
	#"geocode": "37.7749,-122.4194,1mi",
        #"lang": "en",
        "lang": "ja",
        "result_type": "recent",
        "count": "100"
        }
    oath = create_oath_session(oath_key_dict)
    responce = oath.get(url, params = params)
    if responce.status_code != 200:
        print ("Error code: %d" %(responce.status_code))
        return None
    tweets = json.loads(responce.text)
    return tweets

if __name__ == '__main__':
    #検索キーワードを入力
    print ('====== Enter Search String   =====')
    searchstr = input('>  ')
    #出力ファイル名を入力
    print ('====== Enter Tweet Data file =====')
    outfile = input('>  ')

    searchtweet(searchstr,outfile)
                                                                                                                                                       


