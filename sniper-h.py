#!/usr/bin/env/python

import hashlib
import datetime
import argparse
import itertools
from array import array
import string

print("""

            _                        _     
           (_)                      | |    
  ___ _ __  _ _ __   ___ _ __ ______| |__  
 / __| '_ \| | '_ \ / _ \ '__|______| '_ \ 
 \__ \ | | | | |_) |  __/ |         | | | |
 |___/_| |_|_| .__/ \___|_|         |_| |_|
             | |                           
             |_|                           

	 Coded by @laser010 Version 1.2.0

""")

def main():
	try:
		parser = argparse.ArgumentParser(prog="sniper-h.py", add_help=True , usage=(
		"sniper-h.py [-h] -H HASH [-w WORDLIST] [-m MATTRESSES] [-cns CHARACTERS,NUMBERS,SYMBOLS] -t TYPE"))
		parser.add_argument("-H", dest="hash", required=True, help=": [-H] hash value")
		parser.add_argument("-w", dest="word_list", help=": [-w] path word list")
		parser.add_argument("-m", dest="mattresses", help=": [-m] 	Number of mattresses")
		parser.add_argument("-cns", dest="characters_numbers_symbols", help=": [-cns] characters/numbers/symbols values")
		parser.add_argument("-t", dest="types_of_hash", required=True, help=": [-t] Types of hash",
		choices=["md5","md4",
		"sha1","sha224","sha256","sha512","sha384",
		"sha3_224","sha3_256","sha3_384","sha3_512",
		"blake2b","blake2s"])
		args = parser.parse_args()
		number = args.hash.count("")
		number -= 1
		if (number == 32) and args.types_of_hash == "md5" :
			pass
		elif (number == 32) and args.types_of_hash == "md4" :
			pass
		elif (number == 40) and args.types_of_hash == "sha1" :
			pass
		elif (number == 56) and args.types_of_hash == "sha224" :
			pass
		elif (number == 64) and args.types_of_hash == "sha256" :
			pass
		elif (number == 128) and args.types_of_hash == "sha512" :
			pass
		elif (number == 96) and args.types_of_hash == "sha384" :
			pass
		elif (number == 56) and args.types_of_hash == "sha3_224" :
			pass
		elif (number == 64) and args.types_of_hash == "sha3_256" :
			pass
		elif (number == 96) and args.types_of_hash == "sha3_384" :
			pass
		elif (number == 512) and args.types_of_hash == "sha3_512" :
			pass
		elif (number == 128) and args.types_of_hash == "blake2b" :
			pass
		elif (number == 64) and args.types_of_hash == "blake2s" :
			pass
		else:
			print(
				"\n[ERROR] {} Is not {} hash".format(
					args.hash, args.types_of_hash
				)	
			)
			exit(0)
		datetime1 = datetime.datetime.now().replace(microsecond=0)
		print("Start in {0}".format(datetime1))
		if args.word_list != None :
			print("\nRaeding file...")
			wordlist = open(args.word_list, "r")
			num_lines = sum(1 for line in open(args.word_list))
			lines = 0
			for text in wordlist :
				word = text
				text = text.encode("utf-8")
				hash = hashlib.new(args.types_of_hash)
				hash.update(text)
				text = hash.hexdigest()	
				if text == args.hash :
					datetime2 = datetime.datetime.now().replace(microsecond=0)
					time_to_finish = datetime2-datetime1
					print(
						"\nStart in {0}\nFinish in {1}\nTime to finish {2}".format(
							datetime1, datetime2, time_to_finish
						)
					)
					print("\n\n"+text,word)
					exit()
				elif text != args.hash or hashs:
					lines += 1
					op = (int((lines/num_lines)*100))
					print(str(op)+"%",str(num_lines)+"/"+str(lines),end="\r")
					pass
				else :
					print("[ERROR] using [-h] to help.!")
					datetime2 = datetime.datetime.now().replace(microsecond=0)
					time_to_finish = datetime2-datetime1
					print(
						"\nStart in {0}\nFinish in {1}\nTime to finish {2}".format(
							datetime1, datetime2, time_to_finish
						)
					)
		elif args.characters_numbers_symbols != None and args.mattresses != None :
			for wl in itertools.product(args.characters_numbers_symbols, repeat=int(args.mattresses)):
					try:
						text = ''.join(wl)
					except AttributeError:
						text = string.join(wl, '')
					word = text
					text = text.encode("utf-8")
					hash = hashlib.new(args.types_of_hash)
					hash.update(text)
					text = hash.hexdigest()	
					if text == args.hash :
						datetime2 = datetime.datetime.now().replace(microsecond=0)
						time_to_finish = datetime2-datetime1
						print(
							"\nStart in {0}\nFinish in {1}\nTime to finish {2}".format(
								datetime1, datetime2, time_to_finish
							)
						)
						print("\n\n"+text,word)
						exit()
					else :
						print(word,text,end="\r")
						
			datetime2 = datetime.datetime.now().replace(microsecond=0)
			time_to_finish = datetime2-datetime1
			print(
				"\nStart in {0}\nFinish in {1}\nTime to finish {2}".format(
					datetime1, datetime2, time_to_finish
				)
			)
		else :
			print("[ERROR] Using : python sniper-h.py -h")
	except FileNotFoundError:
		print("\n[ERROR] File not found.!")
	except ValueError:
		print("\n[ERROR] Enter just numbers -m [mattresses] !")
	except KeyboardInterrupt:
		pass
if __name__ == "__main__" :
	main()