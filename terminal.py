#!/usr/local/bin/python3.8
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
