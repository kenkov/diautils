# diautils

対話システム用のツールを提供するパッケージです。

## インストール

    $ git clone https://github.com/kenkov/diautils
    $ cd diautils
    $ pip install ./

## 使い方

### コーパス中の単語頻度を集計する

    $ echo "hoge fuga\nfuga hoge geko" | python -m diautils.stats.wordcount
    geko 1
    hoge 2
    fuga 2
