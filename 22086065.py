#!/usr/bin/env python
# coding: utf-8

# In[161]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

#Read file
df = pd.read_csv(r"co2_emission.csv")

#Description of dataframe
df.describe()

fig, axs = plt.subplots(2, 2, figsize = (15, 15), layout='constrained', facecolor='#F4A2A2')
fig.suptitle('\nWorld CO2 Emissions: 1750 - 2017\n' + '\n Name: Mahnoor Farhat   ID: 22086065\n', fontsize=15, fontweight="bold", color='#810808')

#Selecting the World parameter
line_df = df[df.Entity=='World']

#Plot 1
axs[0, 0].plot(line_df['Year'], line_df['Emission'], label='World', color='r')
axs[0, 0].set_xlim([1900, 2017])
axs[0, 0].set(xlabel='Year', ylabel='CO2 Emissions (Tonnes)', title='World CO2 Emissions for 1900 - 2017')
axs[0, 0].legend(loc='upper right')
axs[0, 0].grid(True)
axs[0, 0].set_facecolor('black')
axs[0, 0].text(0.5,-0.4, "Visualization 1:  There has been a drastic increase\n" + 
               "after the 1900s for further 100 years to the 2000s\n" +
               "and more as the world advanced gradually.", 
               size=12, ha="center", transform=axs[0, 0].transAxes)

#Calculate sum of the data for the Year 2000
year00_sum = year00_df['Emission'].sum()

#Calculate percentage from the sum
np.round(year00_sum/1e6,2)
year00_df['Emission %'] = (year00_df['Emission']/year00_sum) * 100

#Plot 2
sums = year00_df.groupby(year00_df["Entity"].tail(10))["Emission %"].sum()

axs[0, 1].pie(sums, labels=sums.index, autopct='%1.2f%%',
    textprops={'fontsize':8},
    colors=sns.color_palette('Set3'),
    shadow=True, 
    explode=[0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05])
axs[0, 1].set(title='Lowest Emissions (%) by 10 Countries for the Year 2000')
axs[0, 1].text(0.5, -0.4, "Visualization 2:  The countries that show the division (%)\n" + 
               "for emitting less carbon-dioxide in the Year 2000 are the\n" + 
               "smallest and less known countries of the world.",
               size=12, ha="center", transform=axs[0, 1].transAxes)

#Sort values for the Year 2000
year00_df = df[df.Year == 2000]
year00_df = year00_df.sort_values(by='Emission', ascending=False)
year00_df.notna()

#Remove the unwanted data
year00_df = year00_df[year00_df.Entity != 'World']
year00_df = year00_df[~pd.isna(year00_df.Code)]
year00_df.head(10)

#Plot 3
axs[1, 0].bar(year00_df.Entity.head(10), year00_df.Emission.head(10), color=sns.color_palette('Set3'), edgecolor='white')
axs[1, 0].set(xlabel='Countries', ylabel='CO2 Emission (Tonnes)', title='CO2 Emission for 2000: Top 10 Countries')
axs[1, 0].grid(True)
axs[1, 0].set_xticklabels(year00_df.Entity.head(10), rotation=90)
axs[1, 0].set_facecolor('black')
axs[1, 0].text(0.5, -0.6, "Visualization 3:  US, China & Russia are the top most developed\n" + 
               "countries of the world that have the largest CO2 emissions for\n" +
               "the year 2000.", 
               size=12, ha="center", transform=axs[1, 0].transAxes)

#Sort the values of data for the Year 2017
year2017_df = df[df.Year == 2017]
year2017_df = year2017_df.sort_values(by='Emission', ascending=False)
year2017_df.notna()

#Remove unwanted data
year2017_df = year2017_df[year2017_df.Entity != 'World']
year2017_df = year2017_df[~pd.isna(year2017_df.Code)]
top_2017 = year2017_df.head(10)
top_2017

#Filter top 10 countries
top_n = list(top_2017.Entity[0:10])
top_10 = df[(df.Entity.isin(top_n))]
top_10

#Plot 4
sns.lineplot(x='Year', y='Emission', hue='Entity', data=top_10)
axs[1, 1].set(xlabel='Year', ylabel='CO2 Emissions (Tonnes)', title='World CO2 Emissions for 2017: Top 10 Countries')
axs[1, 1].legend(loc='upper left')
axs[1, 1].grid(True)
axs[1, 1].set_facecolor('black')
axs[1, 1].text(0.5, -0.55, "Visualization 4:  US & China (out of top 10 countries) have the\n" + 
               "most unstable trends throughout the whole period of 1750-2017.", 
               size=12, ha="center", transform=axs[1, 1].transAxes)

plt.tight_layout()

plt.show()

