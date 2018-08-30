# diautils

diautils は対話テキストデータの変換、解析ツールです。

## インストール

    $ git clone https://github.com/kenkov/diautils
    $ cd diautils
    $ pip install ./

依存ライブラリのインストール

    $ pip install emoji==0.5.0 fire==0.1.3 mojimoji==0.0.8

## フォーマット

diautils では、3 つの対話テキストデータフォーマットを取り扱います。

| フォーマット名 | 説明 | 例 |
| --- | --- | --- |
| jsond | 対話を、`{"text": "発話"}` という形式の発話のリストを保持する JSON で表す | [{"text": "おはよう"}, {"text": "おはようございます"}, {"text": "元気気？"} |
| tabd | 対話を、タブ区切りの発話のリストで表す | "おはよう\tおはようございます\t元気？" |
| paird | 入力発話と応答発話のペアの tabd 形式の対話データ | "おはよう\tおはようございます\nおはようございます\n元気？ |

## 使い方

### フォーマット変換

- `diautils.formatter.jsond2tabd` で jsond 形式から tabd 形式へ変換します。
- `diautils.formatter.tabd2paird` で tabd 形式から paird 形式へ変換します。

### 前処理 `diautils.preprocessor.transformer`

`diautils.preprocessor.transformer` は前処理を提供します。

    $ echo "今日は 晴れです 🤤" | python -m diautils.preprocessor.transformer zen,remove_emoji,remove_space
    今日は晴れです

引数として処理を指定します。

入力文字列が複数カラムの場合は `column` および `separator` で前処理を行うカラムを指定します。

### コーパス中の単語頻度を集計する

    $ echo "hoge fuga\nfuga hoge geko" | python -m diautils.stats.wordcount
    geko 1
    hoge 2
    fuga 2
