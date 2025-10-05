import os

categories = {
    "1": 'Information Gathering',
    "2": 'Vulnerability Analysis',
    "3": 'Web App Analysis',
    "4": 'Password Attacks',
    "5": 'Social Media Attacks',
    "6": 'Wireless Attacks',
    "7": 'Exploitation Tools',
    "8": 'Sniffing and Spoofing',
    "9": 'Post Exploitation',
    "10": 'Forensics',
    "11": 'Useful Tools for Everything'
}

tools = {
    "1": ['inphone', 'sherlock', 'RED_HAWK', 'nmap *', 'netdiscover *', 'theharvester *', 'Nessus Essentials', 'Shodan', 'OSINT Framework'],
    "2": ['nmap *', 'Nessus Essentials'],
    "3": ['Burp Suite *', 'sqlmap *', 'dirbuster *', 'gobuster', 'ffuf *'],
    "4": ['hydra *', 'john *', 'hashcat *', 'rockyou.txt *', 'SecLists', 'Wordlists', 'DarkWeb Lists', 'hashcrack'],
    "5": ['Any brute-forcer for social nets', 'SecLists', 'Wordlists', 'DarkWeb Lists', 'zphisher'],
    "6": ['aircrack-ng *', 'fern wifi cracker *', 'kismet *', 'wifite *', 'BullDDoSer'],
    "7": ['msfconsole *', 'msfvenom *', 'social engineering toolkit (SET) *', 'sqlmap *', 'PayloadsAllTheThings', 'ghost framework', 'netcat (nc) *', 'Exploit Database', 'Google Hacking Database'],
    "8": ['wireshark *', 'ettercap *', 'mitmproxy *', 'macchanger *', 'airmon-ng *'],
    "9": ['powersploit *', 'mimikatz *'],
    "10": ['hashdeep *', 'autopsy *'],
    "11": ['lazy script', 'fsociety']
}

print('\n [*] Categories:')
print('\n [1] Information Gathering')
print(' [2] Vulnerability Analysis')
print(' [3] Web App Analysis')
print(' [4] Password Attacks')
print(' [5] Social Media Attacks')
print(' [6] Wireless Attacks')
print(' [7] Exploitation Tools')
print(' [8] Sniffing and Spoofing')
print(' [9] Post Exploitation')
print('[10] Forensics')
print('[11] Useful Tools for Everything')

category = input('\n[*] Enter Category Choice by Number: ')

os.system("clear")

os.system(f"figlet \"{categories[category]}\"")

print('\n[*] Tools:')
print()

for k, v in tools.items():
    if k == category:
        for elem in v:
            print(elem)

links = {
    "sherlock": 'https://github.com/sherlock-project/sherlock',
    "RED_HAWK": 'https://github.com/Tuhinshubhra/RED_HAWK',
    "Nessus Essentials": 'https://www.tenable.com/products/nessus/nessus-essentials',
    "Shodan": 'https://www.shodan.io',
    "Exploit Database": 'https://www.exploit-db.com',
    "Google Hacking Database": 'https://www.exploit-db.com/google-hacking-database',
    "OSINT Framework": 'https://osintframework.com',
    "gobuster": 'sudo apt install gobuster',
    "SecLists": 'sudo apt install seclists',
    "Wordlists": 'https://github.com/kkrypt0nn/Wordlists',
    "DarkWeb Lists": '',
    "zphisher": 'https://github.com/htr-tech/zphisher/releases/tag/2.3.0',
    "PayloadsAllTheThings": 'https://github.com/swisskyrepo/PayloadsAllTheThings',
    "ghost framework": 'https://github.com/EntySec/ghost',
    "lazy script": 'https://github.com/arismelachroinos/lscript',
    "fsociety": 'https://github.com/Manisso/fsociety'
}

print('\n\n[*] Useful Links:')
print()

for k, v in tools.items():
    if k == category:
        for k2, v2 in links.items():
            if k2 in v:
                print(f'{k2}: {v2}')
