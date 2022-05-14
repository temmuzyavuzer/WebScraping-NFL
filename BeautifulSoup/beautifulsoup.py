#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as BS
import requests
import re
import pandas as pd


html_tect = requests.get('https://stathead.com/tiny/tTuxM').text
soup = BS(html_tect, 'lxml')

links = []
i = 0
players_text = soup.find_all('td', {'data-stat': "name_display"})
regex = re.compile('href="(.*)" rel="noopener"\s')


for player in players_text:
    player_link = re.findall(regex, str(player))
    links.append(player_link)

list_names = pd.DataFrame(
    {'Name': [], 'G': [], 'AV': [], 'QBrec': [], 'Cmp%': [], 'Yds': [], 'Y/A': [], 'TD': [], 'Int': [], 'FantPt': []}
)
for j in range(100):
    html_text = requests.get(links[j][0]).text
    soup = BS(html_text, 'lxml')
    specific_place = soup.find("div", {"class": "stats_pullout"})
    first_table = [i.text for i in specific_place.find_all("div", {"class": "p1"})[0].find_all("p")]
    second_table = [i.text for i in specific_place.find_all("div", {"class": "p1"})[3].find_all("p")]
    name = soup.find("h1").text.strip('\n')
    if len(first_table) == 2:
        games_played = first_table[0]
        av = first_table[1]
        qbeck = second_table[0]
        cmp = second_table[1]
        yds = second_table[2]
        y_a = second_table[3]
        td = second_table[4]
        intt = second_table[5]
        fantpt = second_table[6]
    if len(first_table) == 4:
        games_played = first_table[1]
        av = first_table[3]
        qbeck = second_table[1]
        cmp = second_table[3]
        yds = second_table[5]
        y_a = second_table[7]
        td = second_table[9]
        intt = second_table[11]
        fantpt = second_table[13]
    football_player = {
        'Name': name, 'G': games_played, 'AV': av, 'QBrec': qbeck, 'Cmp%': cmp, 'Yds': yds, 'Y/A': y_a, 'TD': td,
        'Int': intt, 'FantPt': fantpt
    }
    list_names = list_names.append(football_player, ignore_index=True)

print(list_names)
################################################################################
# This part saves data to csv.
################################################################################
list_names.to_csv('players.csv', index=False)
