# diautils

対話システム用のツールを提供するパッケージです。

## インストール

    $ git clone https://github.com/kenkov/diautils
    $ cd diautils
    $ pip install ./

依存ライブラリのインストール

    $ pip install emoji==0.5.0 fire==0.1.3

## 使い方

### 前処理 `diautils.preprocessor.transformer`

    $ echo "今日は 晴れです 🤤" | python -m diautils.preprocessor.transformer zen,remove_emoji,remove_space
    今日は晴れです

### コーパス中の単語頻度を集計する

    $ echo "hoge fuga\nfuga hoge geko" | python -m diautils.stats.wordcount
    geko 1
    hoge 2
    fuga 2
