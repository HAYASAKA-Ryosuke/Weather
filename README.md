Weather

現在の天気情報のネットから取得します．
作った理由は一目で分かる天気情報をtmux上で表示させたいこととbeautifulsoupの勉強のために作りました．
もともとtmux-powerlineの中にyahooから取得する天気情報があったのでそちらを使おうと思いましたが，
どういうわけか私の環境では動作しなかったために作ってみました．

このコードでは札幌市の現在の天気を取得しています．

URL="http://www.jma.go.jp/jp/yoho/306.html"

306が札幌市のナンバとなっています．使用の際には各地域の番号に書き換えてください．

なお開発はpython2.7で行っています．


