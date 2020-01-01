# -*- coding:utf-8 -*-
import codecs
import nltk

def en_place_tweet(dfile,outfile):
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

         #NLTKで形態素解析を行う
         words = nltk.word_tokenize(text_after) 
         pos_tags = nltk.pos_tag(words)
         #print(pos_tags)
         entities = nltk.chunk.ne_chunk(pos_tags)
         #print(entities)

         named_entities = []
         for tagged_tree in entities:
            print(tagged_tree)
            if hasattr(tagged_tree, 'label'):
               entity_name = ' '.join(c[0] for c in tagged_tree.leaves()) 
               entity_type = tagged_tree.label() # get entities category
               named_entities.append((entity_name, entity_type))

         #print(named_entities) 

         a = list()

         for tag in named_entities:
             #print(tag[1])
             if tag[1]=='GPE':   #Specify any tag which is required
                #print(tag[0])
                a.append(tag[0])
         #地名が重複しないようにするため     
         freqdist = nltk.FreqDist(a)

    #出力ファイル名
    fname = r"'"+ outfile + "'"
    fname = fname.replace("'","")

    #重複していない地名をファイルへ出力
    with open(fname, "w",encoding="utf-8") as f:
         for k,v in sorted(freqdist.most_common(100), key=lambda x: x[1], reverse=True):
             f.write("%s" % k)
             f.write('\n')
    f.close()


'''
         length = len(entities) - 1
         a = list()

         for i in range(0, length):
             print(entities [i])
             #GPE 地名
             if entities [i] in ["GPE"]:




             #pos_tags [i][0]  word
             #pos_tags [i][1]  tag
             #固有名詞を抽出
             #log = (pos_tags [i][1] == 'NNP')
             #if log == True:
                #if pos_tags [i][0] not in del_words:
                   #a.append(pos_tags [i][0])

         #freqdist = nltk.FreqDist(a)
         #print(freqdist.most_common(100))

    #出力ファイル名
    fname = r"'"+ outfile + "'"
    fname = fname.replace("'","")

    #重複していない地名をファイルへ出力
    #with open(fname, "w",encoding="utf-8") as f:
         #for k,v in sorted(freqdist.most_common(100), key=lambda x: x[1], reverse=True):
             #f.write("%s" % k)
             #f.write('\n')
    #f.close()
'''
if __name__ == '__main__':
    #ツィートデータのファイル名（入力）を入力
    print ('====== Enter Tweet Data file =====')
    dfile = input('>  ')

    #地名ファイル名（出力）を入力
    print ('====== Enter Place Data file =====')
    outfile = input('>  ')

    en_place_tweet(dfile,outfile)

