# -*- coding:utf-8 -*-
import MeCab
import numpy
import csv
import codecs

def rank_tweet(dfile,outfile):

    #読込むファイル名を設定
    fname = r"'"+ dfile + "'"
    fname = fname.replace("'","")

    #Mecabを使用して、形態素解析
    mecab = MeCab.Tagger("-Ochasen")

    #単語（"名詞", "動詞", "形容詞", "副詞"）と出現回数を格納
    termFreq = {}
    
    #削除したい文字
    del_words = [ 'https','*','-','#','@','://','(',')','/',':','.','　#','_','t','co','RT']

    #ファイルを読込み
    with open(fname, 'r',encoding="utf-8") as f:

        reader = f.readline()

        #UnicodeEncodeErrorを避けるため
        before_reader = reader.encode('cp932', "ignore")
        reader_after = before_reader.decode('cp932')

        while reader:
            #Mecabで形態素解析を行う
            node = mecab.parseToNode(reader_after)

            while node:
                word_type = node.feature.split(",")[0]
                #取得する単語は、"名詞", "動詞", "形容詞", "副詞"
                #if word_type in ["名詞", "動詞", "形容詞", "副詞"]:
                if word_type in ["名詞"]:
                    word = node.surface
                    if word not in del_words:
                       if word in termFreq:
                          termFreq[word] += 1
                       else:
                          termFreq[word] = 1
                node = node.next
            reader = f.readline()

            #UnicodeEncodeErrorを避けるため
            before_reader = reader.encode('cp932', "ignore")
            reader_after = before_reader.decode('cp932')

    #出力ファイル名
    fname = r"'"+ outfile + "'"
    fname = fname.replace("'","")

    #集計した単語と出現回数をファイルへ出力
    with open(fname, "w",encoding="utf-8") as f:
         for k,v in sorted(termFreq.items(), key=lambda x: x[1], reverse=True):
             print("%d: %s" % (v, k))
             f.write("%d: %s" % (v, k))
             f.write('\n')
    f.close()


if __name__ == '__main__':
    #ツィートデータのファイル名（入力）を入力
    print ('====== Enter Tweet Data file =====')
    dfile = input('>  ')

    #出現頻度ファイル名(出力）を入力
    print ('====== Enter termFreq file =====')
    outfile = input('>  ')

    rank_tweet(dfile,outfile)
