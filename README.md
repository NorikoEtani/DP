# DP
作成日：2020年1月1日
作成者：江谷典子
電子メール：kerotan@kcn.ne.jp

社団法人情報処理学会のデジタルプラクティス報告「オープンソースによるTwitter検索およびデータ可視化の方法」を読んで必要なライブラリやモジュールをインストールし，プログラムを御利用ください．
【目的】
基本となるTwitterの検索，単語の出現頻度リスト作成，出現頻度のWord Cloudによる可視化，地名の地図マーカー表示，に関するPythonのプログラムを提供する．
【開発環境】
　筆者の開発環境は下記の通りである．
・Windowsのエディション：Windows 10 Home
・システムの種類：64ビットオペレーティングシステム
・Java version 9
・Python 3.5.2 /Anaconda 4.1.1 (64-bit)
・日本語形態素解析MeCab 0.996
【提供するプログラム】
・search_tweet.py	
TwitterのデータをTwitter APIを利用して取得（絞り込み検索が可能）
・ja_rank_tweet.py
　日本語形態素解析から名詞の単語を抽出し単語の出現頻度リストを作成
・ja_wordcloud.py
　日本語形態素解析から名詞の単語を抽出しWord Cloudで単語の出現頻度を可視化
・ja_place_tweet.py
日本語形態素解析から地名の単語を抽出
・ja_geodata.py
日本語の地名から緯度経度を取得し地図マーカーを表示
・en_rank_tweet.py
　英語形態素解析から名詞の単語を抽出し単語の出現頻度リストを作成
・en_wordcloud.py
　英語形態素解析から名詞の単語を抽出しWord Cloudで単語の出現頻度を可視化
・en_place_tweet.py
英語形態素解析から地名の単語を抽出
・en_geodata.py
英語の地名から緯度経度を取得し地図マーカーを表示
・IPAfont00303\ipag.ttf
　Word Cloudで表示するフォント
***おまけ***
お試しください．
・ja_wordcloud_image.py
　Word Cloudの出力形状を指定したプログラムサンプル．マスクファイルはcolor_alice_one.pngを利用．
・color_alice_one.png
　Word Cloudの形状となるマスクファイル
