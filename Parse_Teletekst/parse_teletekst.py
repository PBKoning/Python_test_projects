import requests
from bs4 import BeautifulSoup

voetbalclubs = ("FC Groningen", "RKC Waalwijk", "FC Volendam", "Ajax", "Sparta R'dam", "FC Emmen",
                 "NEC", "Excelsior", "Go Ahead Eagles", "SC Cambuur", "FC Utrecht", "AZ", "Feyenoord",
                 "FC Twente", "PSV", "sc Heerenveen", "Vitesse", "Fortuna Sit.")


r = requests.get("https://teletekst-data.nos.nl/webplus?p=841")
soup = BeautifulSoup(r.content, "html.parser")
#print(soup.prettify)

data = soup.prettify().split("</head>")
#print(data[1])
all_text = ""

print_text = True
for c in data[1]:
    if c == "<":
        print_text = False
    elif c == ">":
        print_text = True
    elif print_text == True:
        all_text += c
all_lines = all_text.splitlines(False)

for l in all_lines:
    # print(l)
    for v in voetbalclubs:
        if v in l: 
            print(l[:-3].strip())
            break

lines_with_clubs = []


good_characters = "abcdefghijklmnopqrstuvwxyz01234567890.- &;"

for l in all_lines:    
    clubs_in_line = True
    if len(l) < 5: continue # line too short
    if l[0] != " ": continue # has to start with space 
    if not l[1].isalpha(): continue # second character has to be a letter
    
    has_good_characters = True
    has_score = False
    print(l)
    for c in l:
        if c.isdigit() == True or c == "-":
            has_score = True
        if c.lower() not in good_characters:
            print("!", c)
            has_good_characters = False
    if has_score == False: continue # no number or '-' in line, so no score
    if has_good_characters == False: continue # contains unwanted character, so not a line with clubs



    print("*", l.split())
    lines_with_clubs.append(l)

print(lines_with_clubs)
    