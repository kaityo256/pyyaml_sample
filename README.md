# PyYAMLのサンプル

## 概要

PythonからYAMLファイルを読み込み、値を取得して使うサンプルです。

## YAMLファイルとは

YAML (データをテキストで保存するデータ形式の一つです。様々な情報を表現できますが、ここでは連想配列のみを扱います。

```yaml
Type: Hoge
Radius: 12
Temperature: 0.7
```

このように、「名前」「コロン」「値」を羅列します。これをファイルに保存しておき、Pythonから読み込むのが目的です。なお、名前や値は大文字始まりにする必要はありません。

## PyYAMLのインストール

PythonからYAMLを使うには、PyYAMLモジュールのインストールが必要です。pipでインストールします。

```py
python3 -m pip install pyyaml
```

## PyYAMLの使い方

YAMLファイルの拡張子は`yaml`もしくは`yml`です。このリポジトリには、以下のようなファイル`params.yaml`が用意されています。

```yaml
Type: Hoge
Radius: 12
Temperature: 0.7
```

これを読み込み、値を取得するサンプルが`pyyaml_sample.py`です。順番に説明します

まず`yaml`をインポートします。これで`yaml`モジュールが使えるようになります。

```py
import yaml
```

YAMLファイルをロードします。`yaml.safe_load`を使います。

```py
with open("params.yaml") as f:
    params = yaml.safe_load(f)
```

以後、`params.yaml`ファイルの中身は`params`という変数からアクセスできます。この変数は辞書のように使えます。例えばYAMLファイルの`Type`の値は、`params['Type']`でアクセスできます。他の変数も同様です。

```py
# 値の読み込み
name = params['Type']
radius = params['Radius']
temperature = params['Temperature']
```

読み込んだ値は、自動的に適切な型に変換されます。整数なら`int`、小数点を含むなら`float`、それ以外なら文字列(`str`)になります。

```py
# 型の確認
print(f"name: {name} ({type(name)})")
print(f"radius: {radius} ({type(radius)})")
print(f"name: {temperature} ({type(temperature)})")
```

実行結果。

```txt
name: Hoge (<class 'str'>)
radius: 12 (<class 'int'>)
name: 0.7 (<class 'float'>)
```

得た値をファイルに出力するには、f文字列を使うのが便利です。

```py
# ファイルへの出力
with open("output.txt", "w") as f:
    f.write(f"name = {name}\n")
    f.write(f"radius = {radius}\n")
    f.write(f"temperature = {temperature}\n")
```

`open`でファイルを開き、ファイルオブジェクトを`f`で受け取り、`f.write`で書き込みます。文字列の先頭に`f`をつけることで、中身に`{name}`などとあると、`name`変数の値で展開されます。

実行すると、以下の内容の`output.txt`が作成されます。

```txt
name = Hoge
radius = 12
temperature = 0.7
```

## LICENSE

MIT
