# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 20:26:56 2017

@author: taichiNakamura
"""

'''
CoToHA/originとは
    CoToHAにおいて超初期段階の草案的テストコードであり、一つのソースでIPによるCoToHAデバイスとの通信を可能にすることを目指したものである。
    CoToHAを学ぶことにおけるチュートリアルの役割があることも期待する。
    
CoToHA/originの使い方
    まずCoToHA/origin.pyを起動する。起動すると自動的にLAN内にいるCoToHAデバイスの捜索を開始します。
    見つけたデバイスを名前とともに一覧で表示します。
    デバイスは承認を受けることでCoToHAデバイスとして動かすことができるようになります。
    
    Help機能
        Helpを使うことでCoToHAデバイスの技（操作方法）の詳細を知ることができます。
        例：
        ダイソン扇風機：技　
                    ：【動く、つく、回る】＝＞電源がつき通常の回転動作を開始します。
                    ：【微風、自然】＝＞当社独自の微風運転を開始します。
        動作例：「ダイソン扇風機を微風で動かして」または「ダイソン扇風機をつけて」とCoToHAに話してみてください
        
とりあえずここまで、IF文の実装はCoToHA/masterOriginで実装予定


CoToHAデバイスとは
    マイコンが実装されたネットワーク通信に耐えうる機器を想定。将来的にはUBW通信をデフォルトでサポートさせる。それによって位置測位の可能なデバイスを目指す。
    想定する機体はPIC,AVR,Arduino、MbedまたはRasberryPi
    CoToHAライブラリを導入するだけで、あとは簡単なAPIをたたくだけで動かすことができるようにする。
    基本的な処理機構はCoToHAにやらせることを想定しているためデバイス側で受け取るのは制御に必要なパラメータのみにすることが望ましい。
    CoToHAは事前にアップロードされた技（CoToHAデバイス操作方法）を習得することでデバイスの操作を行えるようにする。（従来のドライバの考え方に同じ）
    
    
CoToHAのビジネスモデル
    IoTデバイスの普及におけるボトルネックは購買者のIoTデバイスを収集することのメリットが集め終わるまで得ずらいことにある。
    そこで、IoTデバイスの値段を値引きして初期コストを下げる。この下げたコストは後のユーザ情報の収集や技（ソフトウェア）の管理費として回収する。
    これによって購買者の購買意欲を底上げして直近の購買メリットを呼ぶ。ゆえにこれは一時的な処理として行い将来的には中止するサービスである。
'''
import MeCab

class CoToHA():
    def __init__(self):
        self.alive = 1
    
    def run(self):
        speak = input("おしゃべりしてくださいね！")
        if speak == "おしまい" or speak == "exit":
            self.alive = 0
            print("バイバイー！(@^^)/~~~")
            return
        import MeCab
        mecab = MeCab.Tagger("-Owakati")
        parsed = mecab.parse(speak)
        object__list = ["LED"]
        for s in parsed:
            print(s)

class CoToHA_object():
    '''
    CoToHA_objectとは
    CoToHAにおける核となるクラスである。CoToHAにおけるすべてのクラスはこのクラスを継承する。
    CoToHA_ID
    parent
    children
    '''
    def __init__(self, parent, CoToHA_ID=None):
        if parent == None:
            raise 
        self.parent = parent

    def command(self):
        pass
    
if __name__ == '__main__':
    mycotoha = CoToHA()
    while mycotoha.alive == 1:
        mycotoha.run()
        