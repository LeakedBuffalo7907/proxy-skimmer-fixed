from time import sleep
import requests
import random
import string
from colorama import Fore

scrape = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Proxy Scrape? {Fore.WHITE}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")

if scrape == "no":
  input()

if scrape == "yes":
  scrape()