import sys
import csv
from googletrans import Translator
import re
import asyncio

args = sys.argv

in_file=open(args[1], 'r')
out_file = open(f"{args[1]}_out.srt", 'w')
reader = csv.reader(in_file)
translator = Translator()

async def translate_text(text):
    """テキストを翻訳する関数（同期・非同期両対応）"""
    try:
        # 新しいバージョンの googletrans (非同期)
        result = await translator.translate(text, src='ja', dest='en')
        return result.text
    except TypeError:
        # 古いバージョンの googletrans (同期)
        result = translator.translate(text, src='ja', dest='en')
        return result.text

async def main():
    result = ""
    count = 0
    for row in reader:
        if(count == 0):
            count+=1
            continue
        if(row[2] == ""): 
            continue
        result += f"{count}\n"
        start = re.sub(r':(?!.+:)', ',', row[0].replace(";", ":"), flags=re.DOTALL)
        end = re.sub(r':(?!.+:)', ',', row[1].replace(";", ":"), flags=re.DOTALL)
        result += f"{start} --> {end}\n"
        japanese = row[2].replace("\n", "")
        translated = await translate_text(japanese)
        print(row[2])
        print(translated)
        result += f"{translated}\n\n"
        count+=1
        
    print(result)
    
    out_file.write(result)
    out_file.close()
    in_file.close()

# 非同期処理を実行
asyncio.run(main())
