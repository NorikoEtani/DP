# -*- coding:utf-8 -*-
import folium
import geocoder


def ja_geodata(dfile,outfile):
    # 地図の基準 兵庫県明石市に設定
    japan_location = [35, 135]

    # 基準地点と初期の倍率(日本近郊）を指定し、地図を作成する
    map = folium.Map(location=japan_location, zoom_start=5)

    #読込むファイル名を設定
    fname = r"'"+ dfile + "'"
    fname = fname.replace("'","")

    #ファイルを読込みんで緯度経度出力
    with open(fname, 'r',encoding="utf-8") as f:
         reader = f.readline()

         #UnicodeEncodeErrorを避けるため
         s = reader.encode('cp932', "ignore")
         reader_after = s.decode('cp932')

         #print(reader_after)
         while reader_after:
                ret = geocoder.osm(reader_after, timeout=5.0)
                if ret.ok != False:
                   #UnicodeEncodeErrorを避けるため
                   s_add = ret.address.encode('cp932', "ignore")
                   add_after = s_add.decode('cp932')

                   #京都府内のマーカーのみ表示
                   if add_after.find('京都府') > -1:
                       latitude = ret.latlng[0]
                       longtude = ret.latlng[1]
                       name = reader_after
                       folium.Marker(location=[latitude, longtude], popup=name).add_to(map)

                reader = f.readline()

                #UnicodeEncodeErrorを避けるため
                s = reader.encode('cp932', "ignore")
                reader_after = s.decode('cp932')

# 地図表示
    #出力ファイル名
    fname = r"'"+ outfile + "'"
    fname = fname.replace("'","")
    map.save(fname)

if __name__ == '__main__':
    #地名ファイル名入力
    print ('====== Enter Place Data file =====')
    dfile = input('>  ')

    #地図htmlファイル名（出力）を入力
    print ('====== Enter Map HTML file =====')
    outfile = input('>  ')

    ja_geodata(dfile,outfile)


