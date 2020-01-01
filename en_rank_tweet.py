# -*- coding:utf-8 -*-
import codecs
import nltk

def en_rank_tweet(dfile,outfile):
    #読込むファイル名を設定
    fname = r"'"+ dfile + "'"
    fname = fname.replace("'","")

    #削除したい文字
    del_words = [ 'https','*','-','#','@','://','(',')','/',':','.','　#','_','|','+0000']

    with open(fname, 'r',encoding="utf-8") as f:
         text = f.read();

         #UnicodeEncodeErrorを避けるため
         s = text.encode('cp932', "ignore")
         text_after = s.decode('cp932')

         #NLTKで形態素解析
         words = nltk.word_tokenize(text_after) 
         pos_tags = nltk.pos_tag(words)
         length = len(pos_tags) - 1
         a = list()

         for i in range(0, length):
             #pos_tags [i][0]  word
             #pos_tags [i][1]  tag
             log = (pos_tags [i][1][0] == 'N')
             if log == True:
                if pos_tags [i][0] not in del_words:
                   a.append(pos_tags [i][0])

         freqdist = nltk.FreqDist(a)
         #print(freqdist.most_common(50))

    #出力ファイル名
    fname = r"'"+ outfile + "'"
    fname = fname.replace("'","")

    #集計した単語と出現回数をファイルへ出力
    with open(fname, "w",encoding="utf-8") as f:
         for k,v in sorted(freqdist.most_common(50), key=lambda x: x[1], reverse=True):
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

    en_rank_tweet(dfile,outfile)
