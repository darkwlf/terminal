#!/usr/local/bin/python3.8
import zipfile
import pathlib
import shutil
import keyboard
import webview
import bs4
import time
import requests
import netifaces
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
   a = input("[root@localhost "+os.getcwd()+"]#")
   if a.startswith("echo "):
      print(a[5:])
   elif a.startswith("cd "):
      os.chdir(a[3:])
   elif a.startswith("ls"):
      dir()
   elif a.startswith("cat "):
      file = open(a[4:],"r")
      print(file.read())
      file.close()
   elif a.startswith("wget "):
      url = a[5:]
      filename = wget.download(url)
      print("file is downloading")
   elif a.startswith("rm "):
      s = a[3:]
      os.remove(s)
      print("file removed")
   elif a.startswith("rmdir "):
      os.rmdir(a[6:])
      print("directory removed!")
   elif a.startswith("pwd"):
      print(os.getcwd())
   elif a.startswith("whoami"):
      print(getpass.getuser())
   elif a.startswith("python"):
      os.system("python3.8")
   elif a.startswith("myip"):
      ip()
   elif a.startswith("ping "):
      ping(a[5:],verbose=True)
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
      print("querying target=>",inp)
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
   elif a.startswith("cp"):
      src = input("enter a file path to copy:")
      des = input("enter a destination path to copy:")
      cp = shutil.copyfile(src,des)
      print(colored("file "+src+" has copied to "+des +" successfully!","green"))
      shutil.copytree(src, des)
   elif a.startswith("mv"):
      src = input("enter a file path to move:")
      des = input("enter a destination path to move:")
      dest = shutil.move(source, destination)  
      print(colored("file "+src+ "moved successfully to "+des,"green"))
   elif a.startswith("rename"):
      inp = input("enter file path:")
      inp2 = input("enter a file new name :")
      os.rename(inp,inp2)
      print(colored("file "+inp+" successfully renamed to "+inp2,"green"))
   elif a.startswith("su"):
      password = "admin"
      a = input("your root password:")
      print("logged in as "+a)
      print("tip:default root password is admin.\n for change root password open terminal.py file and com to 58 line and change your password.")
   elif a.startswith("exit"):
      print("exited successfully!")
      break
   elif a.startswith("help"):
      print(colored("\necho command:\nthe echo is for printing something on your terminal like:echo a / output:a\n\n\ncd command:\n\nis siwtch between directorys\nlike :cd /home\n\n","red"))
