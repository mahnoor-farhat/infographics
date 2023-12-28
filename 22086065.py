# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:26:01 2023

@author: Mahnoor Farhat
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.pyplot import pie, axis, show
import seaborn as sns

df = pd.read_csv(r"co2_emission.csv")
df.head()


def plot1():

    line_df = df[df.Entity == 'World']

    fig, axs = plt.subplots(2, 2, figsize=(8, 2 * 2),
                            constrained_layout=True, 
                            facecolor='#57BBF7')

    axs[0, 0].plot(line_df['Year'], line_df['Emission'],
                   label='World', color='r')
    axs[0, 0].set_xlim([1850, 1900])
    axs[0, 0].set(xlabel='Year', ylabel='CO2 Emissions\n' +
                  '(Tonnes)', title='World CO2 Emissions for\n' + '1850 - 1900')
    axs[0, 0].legend(loc='upper right')
    axs[0, 0].grid(True)
    axs[0, 0].set_facecolor('#151B8D')

    axs[0, 1].plot(line_df['Year'], line_df['Emission'],
                   label='World', color='r')
    axs[0, 1].set_xlim([1900, 1950])
    axs[0, 1].set(xlabel='Year', ylabel='CO2 Emissions\n' +
                  '(Tonnes)', title='World CO2 Emissions for\n' + '1900 - 1950')
    axs[0, 1].legend(loc='upper right')
    axs[0, 1].grid(True)
    axs[0, 1].set_facecolor('#151B8D')

    axs[1, 0].plot(line_df['Year'], line_df['Emission'],
                   label='World', color='r')
    axs[1, 0].set_xlim([1950, 2000])
    axs[1, 0].set(xlabel='Year', ylabel='CO2 Emissions\n' +
                  '(Tonnes)', title='World CO2 Emissions for\n' + '1950 - 2000')
    axs[1, 0].legend(loc='lower right')
    axs[1, 0].grid(True)
    axs[1, 0].set_facecolor('#151B8D')

    axs[1, 1].plot(line_df['Year'], line_df['Emission'],
                   label='World', color='r')
    axs[1, 1].set_xlim([2000, 2020])
    axs[1, 1].set(xlabel='Year', ylabel='CO2 Emissions\n' +
                  '(Tonnes)', title='World CO2 Emissions for\n' + '2000 - 2020')
    axs[1, 1].legend(loc='lower right')
    axs[1, 1].grid(True)
    axs[1, 1].set_facecolor('#151B8D')
    plt.show()
    return


def plot2():

    year00_df = df[df.Year == 2000]
    year00_df = year00_df.sort_values(by='Emission', ascending=False)
    year00_df.notna()

    year00_df = year00_df[year00_df.Entity != 'World']
    year00_df = year00_df[~pd.isna(year00_df.Code)]
    year00_df.head(20)

    plt.figure(figsize=(10, 5))
    plt.bar(year00_df.Entity.head(20), year00_df.Emission.head(
        20), color=sns.color_palette('Set3'), edgecolor='white')
    plt.xlabel('Countries', fontsize=10)
    plt.ylabel('CO2 Emission (Tonnes)')
    plt.title('CO2 Emission for 2000: Top 20 Countries',
              fontdict={'fontsize': 12})
    plt.grid(True)
    plt.xticks(rotation=90)

    plt.show()

    return


def plot3():

    year00_df = df[df.Year == 2000]
    year00_df = year00_df.sort_values(by='Emission', ascending=False)
    year00_df.notna()

    year00_df = year00_df[year00_df.Entity != 'World']
    year00_df = year00_df[~pd.isna(year00_df.Code)]
    year00_df.head(20)

    year00_sum = year00_df['Emission'].sum()
    np.round(year00_sum/1e6, 2)

    year00_df['Emission %'] = (year00_df['Emission']/year00_sum) * 100
    year00_df.tail(10)

    sums = year00_df.groupby(year00_df["Entity"].tail(10))["Emission %"].sum()

    fig = plt.figure()
    fig.patch.set_facecolor('#57BBF7')
    axis('equal')
    pie(sums, labels=sums.index, autopct='%1.2f%%',
        textprops={'fontsize': 8},
        colors=sns.color_palette('Set3'),
        shadow=True,
        explode=[0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05])
    plt.title("Lowest Emissions (%) by 10 Countries\n" +
              "for the Year 2000", fontsize=10)
    show()

    return


def plot4():

    year2017_df = df[df.Year == 2017]
    year2017_df = year2017_df.sort_values(by='Emission', ascending=False)
    year2017_df.notna()

    year2017_df = year2017_df[year2017_df.Entity != 'World']
    year2017_df = year2017_df[~pd.isna(year2017_df.Code)]
    top_2017 = year2017_df.head(10)
    top_2017

    top_n = list(top_2017.Entity[0:10])
    top_10 = df[(df.Entity.isin(top_n))]
    top_10

    fig = plt.figure(figsize=(12, 5))

    sns.lineplot(x='Year', y='Emission', hue='Entity', data=top_10)
    plt.title('Trend for the Year 2017: Top 10 Countries')
    plt.grid()
    plt.show()
    return


plot1()
plot2()
plot3()
plot4()
