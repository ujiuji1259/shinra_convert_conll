# shinra_convert_conll
トークナイズ後の[森羅データセット](https://github.com/k141303/shinra_data_tokenizer)をconllフォーマットに変換

## input
```bash
# データセットのパスを環境変数に格納(処理したいデータセットのみ格納してください)
export SHINRA2020EVENT=[Eventデータセットのパス]
export SHINRA2020FACILITY=[Facilityデータセットのパス]
export SHINRA2020JP5=[JP-5データセットのパス]
export SHINRA2020LOCATION=[Locationデータセットのパス]
export SHINRA2020ORGANIZATION=[Organizationデータセットのパス]

python main.py
```

## output
データセットのディレクトリに、train.iob、test.iobが追加されます
```bash
./outputs/mecab_ipadic/JP-5/Airport/
 ├ train.iob
 ├ test.iob
 ├ Airport_dist.json
 ├ vocab.txt
 └ tokens/
    ├ 1001711.txt
    ├ 175701.txt
    ≈
    └ 999854.txt
```

出力ファイルのフォーマットは以下の通りです。
```
page_id
line_id
token_id  start_text_offset  end_text_offset  IOB2_label
token_id  start_text_offset  end_text_offset  IOB2_label
...
token_id  start_text_offset  end_text_offset  IOB2_label

page_id
line_id
token_id  start_text_offset  end_text_offset  IOB2_label
token_id  start_text_offset  end_text_offset  IOB2_label
...
token_id  start_text_offset  end_text_offset  IOB2_label

....
```

### 注意点
- testファイルではIOB2_labelが空文字となっています
- token_id、start_text_offset、end_text_offsetはデータセットと同一となっています
- testファイルではIOB2_labelが空文字となっています
- 複数のラベルが付与されている場合`|`で結合されています（label1|label2など）
