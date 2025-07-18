# premierecsv2srt
Premiereのグラフィックテロップcsvから英語字幕srtを生成するスクリプト

# How to use

1. AdobePremiereProでテロップテキストをcsv書き出し
https://ameblo.jp/herogarage/entry-12860880562.html

3. 
```sh
pip install googletrans==4.0.0-rc1
```

3. 
```sh
python3 premiere_graphics_caption_csv_to_srt.py YOUR_CSV_FILE.csv
```
