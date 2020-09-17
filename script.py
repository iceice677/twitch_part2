import codecademylib3_seaborn
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Bar Graph: Featured Games

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

plt.bar(range(len(games)), viewers, color='lightblue')
plt.title('Top 10 games viewers in Twitch')
plt.legend(['Twitch'])
plt.xlabel('Games')
plt.ylabel('Viewers')
ax= plt.subplot()
ax.set_xticklabels(games, rotation=40)
ax.set_xticks(range(len(games)))
plt.show()

plt.clf()
# Pie Chart: League of Legends Viewers' Whereabouts

labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]

countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]

colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']

explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

plt.pie(countries, explode=explode, shadow=True , startangle=340,labels=labels, colors=colors, autopct= "%1.0f%%" ,pctdistance=1.5)
plt.axis('equal')
plt.show()
plt.title('League of Legends Viewers Whereabouts')
plt.clf()
# Line Graph: Time Series Analysis

hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

y_upper= [i + ( i*0.15) for i in viewers_hour]
y_lower= [i - ( i*0.15) for i in viewers_hour]

plt.plot(hour, viewers_hour)
plt.title('The number of US viewers at different hours of the day on Jan 2015')
plt.legend(['2015-01-01'])
plt.xlabel('Hour')
plt.ylabel('Viewers')
plt.fill_between(hour, y_lower, y_upper, alpha=0.2)
ax2= plt.subplot()
ax2.set_xticklabels(hour)
ax2.set_xticks(hour)
ax2.set_yticks([0,20,40,60,80,100,120])
plt.show()




