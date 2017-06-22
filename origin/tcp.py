'''author inten
   start writing 2017/06/22 0:31

    これはTCPプロトコルによるCoToHA/origin用の通信をサポートするソース群

'''

# -*- coding:utf-8 -*-
import socket

host = "localhost" #お使いのサーバーのホスト名を入れます
port = 5108 #適当なPORTを指定してあげます




if __name__ == '__main__':
    if input('server?') == 'y':
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IP/TCP
        serversocket.bind((socket.gethostname(), 5108))
        serversocket.listen(5)
        print('waitting...')
        clientsock, client_address= serversocket.accept()  # 接続されればデータを格納
        while True:
            rcvmsg = clientsock.recv(1024)
            print('Received -> %s' % (rcvmsg))
            if rcvmsg == '':
                break
            print('Type message...')
            s_msg = input()
            if s_msg == '':
                break
            print('Wait...')
            clientsock.sendall(ord(s_msg) )  # メッセージを返します
        clientsock.close()
    else:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # オブジェクトの作成をします

        client.connect(('localhost', 5108))  # これでサーバーに接続します

        client.send(b'rom nadechin')  # 適当なデータを送信します（届く側にわかるように）

        response = client.recv(4096)  # レシーブは適当な2進数にします（大きすぎるとダメ）

        print(response)