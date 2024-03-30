# flask_fcgi_test

## GitPod
https://gitpod.io/?autostart=true#https://github.com/cti1650/flask_fcgi_test

## コマンド

### Git Clone

```
git clone {url}
cd flask_fcgi_test
```

### ライブラリインストール

```
python3.9 -m pip install -r requirements_prod.txt
```

### 権限付与

```
chmod 644 .htaccess
chmod 755 index.fcgi
chmod 600 hello.py
```

### 更新
```
git reset --hard
git pull
```

or

```
sh script/setup.sh
```

## 参考サイト
- [PythonのWebアプリをXserverで動かす(Flask編) – CodeAid-Lab（コードエイド・ラボ）](https://codeaid.jp/webapp-xserver/)  
- [Xserver内での移転作業でトラブル！原因はパーミッションだった。 | LIVETHERE](https://livethere.net/web_design/xserver_move)  
- [git pull を強制し、リモートでローカルを上書きする方法 | WWWクリエイターズ](https://www-creators.com/archives/1097#git_reset_w_hyphenhard)
- [Flask2でURLルーティングを別ファイルにまとめたい #Python - Qiita](https://qiita.com/miyakiyo/items/34617adaf77acf8b4511)  
