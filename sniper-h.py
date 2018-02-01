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

	 Coded by @laser010 Version 1.1.1

""")

def main():
	try:
		parser = argparse.ArgumentParser(prog="sniper-h.py", add_help=True, usage=(
		"python sniper-h.py [-H HASH] [-W PATH WORDLIST] [-T TYPYE OF HASH]"))
		parser.add_argument("-H", dest="hash", required=True, help=": [-H] hash value")
		parser.add_argument("-W", dest="word_list", required=True, help=": [-W] path word list")
		parser.add_argument("-T", dest="types_of_hash", required=True, help=": [-T] Types of hash",
		choices=["md5","md4",
		"sha1","sha224","sha256","sha512","sha384",
		"sha3_224","sha3_256","sha3_384","sha3_512",
		"blake2b","blake2s"])
		args = parser.parse_args()
		print("\nRaeding file...")
		wordlist = open(args.word_list, "r")
		num_lines = sum(1 for line in open(args.word_list))
		lines = 0
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
			print("\n[ERROR] {} Is not {} hash".format(args.hash, args.types_of_hash))
			exit(0)
		datetime1 = datetime.datetime.now().replace(microsecond=0)
		print("Start in {0}".format(datetime1))
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
	except FileNotFoundError:
		print("\n[ERROR] File not found.!")
	except ValueError:
		print("\n[ERROR] Hash type not found.!")
	except KeyboardInterrupt:
		pass
if __name__ == "__main__" :
	main()