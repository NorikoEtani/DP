# -*- coding:utf-8 -*-
import MeCab
import matplotlib.pyplot as plt
import csv
from wordcloud import WordCloud

def analyze_tweet_text(datafile):

    #読込むファイル名を設定
    fname = r"'"+ datafile + "'"
    fname = fname.replace("'","")

    #Mecabを使用して、形態素解析
    mecab = MeCab.Tagger("-Ochasen")

    #"名詞"を格納するリスト
    words=[]

    #ファイルを読込み
    with open(fname, 'r',encoding="utf-8") as f:

        reader = f.readline()

        while reader:
            #Mecabで形態素解析を行う
            node = mecab.parseToNode(reader)

            while node:
                word_type = node.feature.split(",")[0]

                #取得する単語は、"名詞", "動詞", "形容詞", "副詞"
                #if word_type in ["名詞", "動詞", "形容詞", "副詞"]:
                if word_type in ["名詞"]:

                    words.append(node.surface)

                node = node.next

            reader = f.readline()

    #wordcloudで出力するフォントを指定
    font_path = r"<インストール先のドライブとディレクトリ>\IPAfont00303\ipag.ttf"

    txt = " ".join(words)

     stop_words = [ 'https','*','-','#','@']

    #解析した単語、ストップワードを設定、背景の色は黒にしてます
    wordcloud = WordCloud(background_color="black",font_path=font_path, stopwords=set(stop_words),
        width=800,height=600).generate(txt)

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


if __name__ == '__main__':

    print ('====== Enter Tweet Data file =====')
    datafile = input('>  ')

    analyze_tweet_text(datafile)
