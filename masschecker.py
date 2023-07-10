#!/usr/bin/python2.7
#Author By Cx99
#CodeName: Cx99
#10 Juli 2023

import os,re,time,sys
import requests
import urllib2
import ssl
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool


red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[36m'
purple = '\033[35m'
reset = '\033[0m'
#initialize OS for display clear
if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')
pass
#runningText

#Banner
print(green+"   ______       ____  _______           __          ")
print("  / __/ /  ___ / / / / ___/ /  ___ ____/ /_____ ___ ")
print(" _\ \/ _ \/ -_) / / / /__/ _ \/ -_) __/  '_/ -_) __/")
print("/___/_//_/\__/_/_/  \___/_//_/\__/\__/_/\_\\__/_/   ")
print(blue+"Author By Cx99 : https://tools.cx99.my.id "+yellow)
print(red+'( For List Shell use http:// or https:// )')

def error():
	try:
		requests.post('http://www.google.com')
		open(sys.argv[1], 'rb')
	except requests.exceptions.ConnectionError:
		print(red+"[ - ]"+reset+" Internet Down !! ")
		exit()
	except IOError:
		print(red+"[ - ]"+reset+" File NOt WORK !")
		exit()
	except IndexError:
		print(red+"[ - ]"+reset+" Usage : python2 file.py list.txt")
		exit()
error()

def main(url):
		try:
			header = {'Content-Type' : 'text/html; charset=UTF-8','User-Agent':''}
			r = urllib2.urlopen(url, context=ssl._create_unverified_context())
			if r.code == 200:
				print(green+"[ LIVE ] "+reset+url)
				with open('live.txt','a') as live:
					live.write(url+'\n')
					live.close()
			pass
		except:
			print(red+"[ DIE  ] "+reset+url)
			with open('die.txt', 'a') as die:
				die.write(url+'\n')
				die.close()
			pass


#Input

target	= [i for i in open(sys.argv[1]).read().split("\n") if i != ""]
t = ThreadPool(10)
t.map(main, target)



if __name__ == "__main__":
	print(yellow+"LIVE Shell : %s live.txt" % green)
	print(yellow+"DIE Shell  : %s die.txt" % red+reset)