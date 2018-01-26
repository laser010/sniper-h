import hashlib
import datetime

print("""

            _                        _     
           (_)                      | |    
  ___ _ __  _ _ __   ___ _ __ ______| |__  
 / __| '_ \| | '_ \ / _ \ '__|______| '_ \ 
 \__ \ | | | | |_) |  __/ |         | | | |
 |___/_| |_|_| .__/ \___|_|         |_| |_|
             | |                           
             |_|                           
Coded by instagram @laser01 Version 1.0.0

for test : 644fef65c574baeda79b3988c2353290
""")

hashed = input('\n\nEnter hash : ')

print("\n[*] Raeding file")
file = open("wordlist.txt", "r")

num_lines = sum(1 for line in open("wordlist.txt"))
lines = 0

datetime1 = datetime.datetime.now().replace(microsecond=0)
print("[*] Start {0}".format(datetime1))
for text in file:
        word = text
        text = text.encode("utf-8")
        hash = hashlib.new("md5")
        hash.update(text)
        text=hash.hexdigest()
        if text == hashed :
           print(text," ",word)
           datetime2 = datetime.datetime.now().replace(microsecond=0)
           Time_to_finish = datetime2-datetime1
           print("\nStart in {0}\nFinish in {1}\nTime to finish {2}".format(datetime1, datetime2, Time_to_finish))
           exit()
        elif text != hashed :
           lines += 1
           op = (int((lines/num_lines)*100))
           print(str(op)+"%",text,end="\r")
           pass

datetime2 = datetime.datetime.now().replace(microsecond=0)
Time_to_finish = datetime2-datetime1
print("\nStart in {0}\nFinish in {1}\nTime to finish {2}".format(datetime1, datetime2, Time_to_finish))
