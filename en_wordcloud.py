# -*- coding:utf-8 -*-
import codecs
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def en_wordcloud(dfile):
    #読込むファイル名を設定
    fname = r"'"+ dfile + "'"
    fname = fname.replace("'","")

    with open(fname, 'r',encoding="utf-8") as f:
         text = f.read();

         #UnicodeEncodeErrorを避けるため
         s = text.encode('cp932', "ignore")
         text_after = s.decode('cp932')

         #NLTKで形態素解析を行う
         words = nltk.word_tokenize(text_after) 
         pos_tags = nltk.pos_tag(words)
         length = len(pos_tags) - 1
         a = list()

         for i in range(0, length):
             #pos_tags [i][0]  word
             #pos_tags [i][1]  tag
             log = (pos_tags [i][1][0] == 'N')
             if log == True:
                a.append(pos_tags [i][0])

         txt = " ".join(a)

         # Stop Words  ※これは除外したい単語を設定
         stop_words = ['https','*','-','#','@']

         # Generate a word cloud image
         wordcloud = WordCloud(max_font_size=40,stopwords=set(stop_words)).generate(txt)

         plt.figure()
         plt.imshow(wordcloud, interpolation="bilinear")
         plt.axis("off")
         plt.show()


if __name__ == '__main__':
    #ツィートデータのファイル名（入力）を入力
    print ('====== Enter Tweet Data file =====')
    dfile = input('>  ')

    en_wordcloud(dfile)

