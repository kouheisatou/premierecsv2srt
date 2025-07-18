import sys
import csv
from googletrans import Translator
import re

args = sys.argv

in_file=open(args[1], 'r')
out_file = open(f"{args[1]}_out.srt", 'w')
reader = csv.reader(in_file)
translator = Translator()

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
    translated = translator.translate(row[2], src='ja', dest='en').text
    print(row[2])
    print(translated)
    result += f"{translated}\n\n"
    count+=1
    
print(result)

out_file.write(result)
out_file.close()
in_file.close()
