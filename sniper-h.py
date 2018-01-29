import hashlib
import datetime
import argparse

print("""

            _                        _     
           (_)                      | |    
  ___ _ __  _ _ __   ___ _ __ ______| |__  
 / __| '_ \| | '_ \ / _ \ '__|______| '_ \ 
 \__ \ | | | | |_) |  __/ |         | | | |
 |___/_| |_|_| .__/ \___|_|         |_| |_|
             | |                           
             |_|                           
Coded by @laser010 Version 1.1.0

example: python sniper-h.py --Hash 644fef65c574baeda79b3988c2353290 --wordlist wordlist.txt --type md5 

""")

def main():
	try:
		parser = argparse.ArgumentParser()
		parser.add_argument("--Hash", "-H", required=True, help="hash value .")
		parser.add_argument("--wordlist", "-w", required=True, help="path wordlist .")
		parser.add_argument("--type", "-t", required=True, help="type hash md5/md4/sha1/sha224/sha256/sha384/sha512 .")
		args = parser.parse_args()

		print("\n[*] Raeding file...")
		file = open(args.wordlist, "r")

		num_lines = sum(1 for line in open(args.wordlist))
		lines = 0

		datetime1 = datetime.datetime.now().replace(microsecond=0)
		print("[*] Start {0}".format(datetime1))
		for text in file:
			word = text
			text = text.encode("utf-8")
			hash = hashlib.new(args.type)
			hash.update(text)
			text=hash.hexdigest()
			if text == args.Hash :
				datetime2 = datetime.datetime.now().replace(microsecond=0)
				Time_to_finish = datetime2-datetime1
				print("\nStart in {0}\nFinish in {1}\nTime to finish {2}".format(datetime1, datetime2, Time_to_finish))
				print("\n\n"+text,word)
				exit()
			elif text != args.Hash :
				lines += 1
				op = (int((lines/num_lines)*100))
				print(str(op)+"%",str(num_lines)+"/"+str(lines),text,end="\r")
				pass
			else :
				print("[ERROR] using [-h] to help.!")
		datetime2 = datetime.datetime.now().replace(microsecond=0)
		Time_to_finish = datetime2-datetime1
		print("\nStart in {0}\nFinish in {1}\nTime to finish {2}".format(datetime1, datetime2, Time_to_finish))
	except FileNotFoundError:
		print("\n[ERROR] File not found.!")
	except ValueError:
		print("\n[ERROR] Hash type not found.!")
	except KeyboardInterrupt:
		pass
if __name__ == "__main__" :
	main()