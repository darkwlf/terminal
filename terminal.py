#!/usr/local/bin/python3.8
import pathlib
import shutil
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
   a = input("[root@localhost "+os.getcwd()+"]#:")
   if a.startswith("echo "):
      print(a[5:])
   elif a.startswith("cd "):
      os.chdir(a[3:])
      print(os.getcwd())
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
   elif a.startswith("webview"):
      webview.create_window('Hello world', 'https://pywebview.flowrl.com/hello')
      webview.start()
   elif a.startswith("remove "):
      shutil.rmtree(a[7:])
      print("file deleted succesfully!")
