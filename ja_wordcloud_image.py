# -*- coding:utf-8 -*-
import MeCab
import matplotlib.pyplot as plt
import csv
from wordcloud import WordCloud
from PIL import Image
import numpy as np
from wordcloud import ImageColorGenerator

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

    #マスク画像読み込み
    mask = np.array(Image.open('color_alice_one.png'))

    #解析した単語、ストップワードを設定、マスク画像の設定、背景の色は白にしてます
    wordcloud = WordCloud(max_font_size=15,background_color="white",mask=mask,font_path=font_path, stopwords=set(stop_words),
        width=800,height=600).generate(txt)

    # create coloring from image
    image_colors = ImageColorGenerator(mask)

    # show
    fig, axes = plt.subplots(1, 3)
    axes[0].imshow(wordcloud, interpolation="bilinear")
    # recolor wordcloud and show
    # we could also give color_func=image_colors directly in the constructor
    axes[1].imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
    axes[2].imshow(mask, cmap=plt.cm.gray, interpolation="bilinear")
    for ax in axes:
        ax.set_axis_off()
    plt.show()
    #plt.imshow(wordcloud)
    #plt.axis("off")
    #plt.show()


if __name__ == '__main__':

    print ('====== Enter Tweet Data file =====')
    datafile = input('>  ')

    analyze_tweet_text(datafile)
