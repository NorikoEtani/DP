# -*- coding:utf-8 -*-
import MeCab
import csv

def ja_place_tweet(dfile,outfile):

    fname = r"'"+ dfile + "'"
    fname = fname.replace("'","")

    #Mecabを使用して、形態素解析
    mecab = MeCab.Tagger("-Ochasen")

    #"名詞"を格納するリスト
    termFreq = {}

    #ファイルを読込み
    with open(fname, 'r',encoding="utf-8") as f:

        reader = f.readline()

        while reader:
            #Mecabで形態素解析を実施
            node = mecab.parseToNode(reader)

            while node:
                word_type = node.feature.split(",")[0]

                #取得する単語は地名
                if word_type in ["名詞"]:
                    if (node.feature.split(",")[1]=="固有名詞") and (node.feature.split(",")[2]=="地域"):
                       plain_word = node.feature.split(",")[6]
                       if plain_word !="*":
                          word = node.surface
                          #地名が重複しないようにするため
                          if word not in termFreq:
                             termFreq[word] = 1

                node = node.next

            reader = f.readline()

    #出力ファイル名
    fname = r"'"+ outfile + "'"
    fname = fname.replace("'","")

    #重複していない地名をファイルへ出力
    with open(fname, "w",encoding="utf-8") as f:
         for term, count in termFreq.items():
             #print(term)
             f.write(term)
             f.write('\n')
    f.close()


if __name__ == '__main__':
    #ツィートデータのファイル名(入力）を入力
    print ('====== Enter Tweet Data file =====')
    dfile = input('>  ')

    #地名ファイル名（出力）を入力
    print ('====== Enter Place Data file =====')
    outfile = input('>  ')

    ja_place_tweet(dfile,outfile)
