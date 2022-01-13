# @since: 2021-10-1
# @author: Gabriel Marojevic, Daniel Japs, Waldemar Granson, Lukas Gabriel, Kai Perich

# Import Packages
import matplotlib
import pandas as pd
from matplotlib import pyplot as plt

#Visualisierung Twitch Genre: Action
df_action = pd.read_csv("action.csv")
plt.plot(df_action.Twitch_Year, df_action.Hours_watched)
plt.title("Genre: Action")
plt.xlabel("Year")
plt.ylabel("Hours watched (million)")
plt.savefig("action.png")
plt.show()

#Visualisierung Twitch Genre: Action
df_adventure = pd.read_csv("adventure.csv")
plt.plot(df_adventure.Twitch_Year, df_adventure.Hours_watched)
plt.title("Genre: Adventure")
plt.xlabel("Year")
plt.ylabel("Hours watched (million)")
plt.savefig("adventure.png")
plt.show()

#Visualisierung Twitch Genre: Fighting
df_fighting = pd.read_csv("fighting.csv")
plt.plot(df_fighting.Twitch_Year, df_fighting.Hours_watched)
plt.title("Genre: Fighting")
plt.xlabel("Year")
plt.ylabel("Hours watched (million)")
plt.savefig("fighting.png")
plt.show()

#Visualisierung Twitch Genre: Misc
df_misc = pd.read_csv("misc.csv")
plt.plot(df_misc.Twitch_Year, df_misc.Hours_watched)
plt.title("Genre: Misc")
plt.xlabel("Year")
plt.ylabel("Hours watched (million)")
plt.savefig("misc.png")
plt.show()

#Visualisierung Twitch Genre: Platform
df_platform = pd.read_csv("platform.csv")
plt.plot(df_platform.Twitch_Year, df_platform.Hours_watched)
plt.title("Genre: Platform")
plt.xlabel("Year")
plt.ylabel("Hours watched (million)")
plt.savefig("platform.png")
plt.show()

#Visualisierung Twitch Genre: Puzzle
df_puzzle = pd.read_csv("puzzle.csv")
plt.bar(df_puzzle.Twitch_Year, df_puzzle.Hours_watched)
plt.title("Genre: Puzzle")
plt.xlabel("Year")
plt.ylabel("Hours watched (million)")
plt.savefig("puzzle.png")
plt.show()

#Visualisierung Twitch Genre: Racing
df_racing = pd.read_csv("racing.csv")
plt.plot(df_racing.Twitch_Year, df_racing.Hours_watched)
plt.title("Genre: Racing")
plt.xlabel("Year")
plt.ylabel("Hours watched (million)")
plt.savefig("racing.png")
plt.show()

#Visualisierung Twitch Genre: Role-Playing
df_rp = pd.read_csv("rp.csv")
plt.plot(df_rp.Twitch_Year, df_rp.Hours_watched)
plt.title("Genre: Role-Playing")
plt.xlabel("Year")
plt.ylabel("Hours watched (million)")
plt.savefig("rp.png")
plt.show()

#Visualisierung Twitch Genre: Shooter
df_shooter = pd.read_csv("shooter.csv")
plt.plot(df_shooter.Twitch_Year, df_shooter.Hours_watched)
plt.title("Genre: Shooter")
plt.xlabel("Year")
plt.ylabel("Hours watched (million)")
plt.savefig("shooter.png")
plt.show()

#Visualisierung Twitch Genre: Simulation
df_simulation = pd.read_csv("simulation.csv")
plt.plot(df_simulation.Twitch_Year, df_simulation.Hours_watched)
plt.title("Genre: Simulation")
plt.xlabel("Year")
plt.ylabel("Hours watched (million)")
plt.savefig("simulation.png")
plt.show()

#Visualisierung Twitch Genre: Sports
df_sports = pd.read_csv("sports.csv")
plt.plot(df_sports.Twitch_Year, df_sports.Hours_watched)
plt.title("Genre: Sports")
plt.xlabel("Year")
plt.ylabel("Hours watched (million)")
plt.savefig("sports.png")
plt.show()

#Visualisierung Twitch Genre: Strategy
df_strategy = pd.read_csv("strategy.csv")
plt.plot(df_strategy.Twitch_Year, df_strategy.Hours_watched)
plt.title("Genre: Strategy")
plt.xlabel("Year")
plt.ylabel("Hours watched (million)")
plt.savefig("strategy.png")
plt.show()

#Visualisierung Genre Popularität: 2016
df_hw2016 = pd.read_csv("genre_hw2016.csv")
plt.bar(df_hw2016.Genre, df_hw2016.Hours_watched)
plt.rcParams.update({'font.size': 20})
plt.title("Genre Popularity (2016)")
plt.xlabel("Genre", fontsize=16)
plt.ylabel("Hours watched (million)", fontsize=16)
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(14, 8)
fig.savefig("popularity_2016.png")
plt.show()

#Visualisierung Genre Popularität: 2017
df_hw2017 = pd.read_csv("genre_hw2017.csv")
plt.bar(df_hw2017.Genre, df_hw2017.Hours_watched)
plt.rcParams.update({'font.size': 20})
plt.title("Genre Popularity (2017)")
plt.xlabel("Genre", fontsize=24)
plt.ylabel("Hours watched (million)", fontsize=24)
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(28, 14)
fig.savefig("popularity_2017.png")
plt.show()

#Visualisierung Genre Popularität: 2018
df_hw2018 = pd.read_csv("genre_hw2018.csv")
plt.bar(df_hw2018.Genre, df_hw2018.Hours_watched)
plt.rcParams.update({'font.size': 20})
plt.title("Genre Popularity (2018)")
plt.xlabel("Genre", fontsize=24)
plt.ylabel("Hours watched (million)", fontsize=24)
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(28, 14)
fig.savefig("popularity_2018.png")
plt.show()

#Visualisierung Genre Popularität: 2019
df_hw2019 = pd.read_csv("genre_hw2019.csv")
plt.bar(df_hw2019.Genre, df_hw2019.Hours_watched)
plt.rcParams.update({'font.size': 20})
plt.title("Genre Popularity (2019)")
plt.xlabel("Genre", fontsize=24)
plt.ylabel("Hours watched (million)", fontsize=24)
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(32, 14)
fig.savefig("popularity_2019.png")
plt.show()

#Visualisierung Genre Popularität: 2020
df_hw2020 = pd.read_csv("genre_hw2020.csv")
plt.bar(df_hw2020.Genre, df_hw2020.Hours_watched)
plt.rcParams.update({'font.size': 20})
plt.title("Genre Popularity (2020)")
plt.xlabel("Genre")
plt.ylabel("Hours watched (million)")
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(28, 14)
fig.savefig("popularity_2020.png")
plt.show()

#Visualisierung Genre Popularität: 2021
df_hw2021 = pd.read_csv("genre_hw2021.csv")
plt.bar(df_hw2021.Genre, df_hw2021.Hours_watched)
plt.rcParams.update({'font.size': 20})
plt.title("Genre Popularity (2021)")
plt.xlabel("Genre")
plt.ylabel("Hours watched (million)")
fig2 = matplotlib.pyplot.gcf()
fig2.set_size_inches(30, 14)
fig2.savefig("popularity_2021.png")
plt.show()

#Visualisierung VGS Genre: Action
df_action = pd.read_csv("action_vgs_sum.csv")
plt.plot(df_action.Year, df_action.Global_Sales)
plt.title("Genre: Action")
plt.xlabel("Year")
plt.ylabel("Global Sales (million)")
plt.savefig("action_vgs.png")
plt.show()

#Visualisierung VGS Genre: Adventure
df_adventure = pd.read_csv("adventure_vgs_sum.csv")
plt.plot(df_adventure.Year, df_adventure.Global_Sales)
plt.title("Genre: Adventure")
plt.xlabel("Year")
plt.ylabel("Global Sales (million)")
plt.savefig("adventure_vgs.png")
plt.show()

#Visualisierung VGS Genre: Fighting
df_fighting = pd.read_csv("fighting_vgs_sum.csv")
plt.plot(df_fighting.Year, df_fighting.Global_Sales)
plt.title("Genre: Fighting")
plt.xlabel("Year")
plt.ylabel("Global Sales (million)")
plt.savefig("fighting_vgs.png")
plt.show()

#Visualisierung VGS Genre: Misc
df_misc = pd.read_csv("misc_vgs_sum.csv")
plt.plot(df_misc.Year, df_misc.Global_Sales)
plt.title("Genre: Misc")
plt.xlabel("Year")
plt.ylabel("Global Sales (million)")
plt.savefig("misc_vgs.png")
plt.show()

#Visualisierung VGS Genre: Platform
df_platform = pd.read_csv("platform_vgs_sum.csv")
plt.plot(df_platform.Year, df_platform.Global_Sales)
plt.title("Genre: Platform")
plt.xlabel("Year")
plt.ylabel("Global Sales (million)")
plt.savefig("platform_vgs.png")
plt.show()

#Visualisierung VGS Genre: Puzzle
df_puzzle = pd.read_csv("puzzle_vgs_sum.csv")
plt.plot(df_puzzle.Year, df_puzzle.Global_Sales)
plt.title("Genre: Puzzle")
plt.xlabel("Year")
plt.ylabel("Global Sales (million)")
plt.savefig("puzzle_vgs.png")
plt.show()

#Visualisierung VGS Genre: Racing
df_racing = pd.read_csv("racing_vgs_sum.csv")
plt.plot(df_racing.Year, df_racing.Global_Sales)
plt.title("Genre: Racing")
plt.xlabel("Year")
plt.ylabel("Global Sales (million)")
plt.savefig("racing_vgs.png")
plt.show()

#Visualisierung VGS Genre: Role-Playing
df_rp = pd.read_csv("rp_vgs_sum.csv")
plt.plot(df_rp.Year, df_rp.Global_Sales)
plt.title("Genre: Role-Playing")
plt.xlabel("Year")
plt.ylabel("Global Sales (million)")
plt.savefig("rp_vgs.png")
plt.show()

#Visualisierung VGS Genre: Shooter
df_shooter = pd.read_csv("shooter_vgs_sum.csv")
plt.plot(df_shooter.Year, df_shooter.Global_Sales)
plt.title("Genre: Shooter")
plt.xlabel("Year")
plt.ylabel("Global Sales (million)")
plt.savefig("shooter_vgs.png")
plt.show()

#Visualisierung VGS Genre: Simulation
df_simulation = pd.read_csv("simulation_vgs_sum.csv")
plt.plot(df_simulation.Year, df_simulation.Global_Sales)
plt.title("Genre: Simulation")
plt.xlabel("Year")
plt.ylabel("Global Sales (million)")
plt.savefig("simulation_vgs.png")
plt.show()

#Visualisierung VGS Genre: Sports
df_sports = pd.read_csv("sports_vgs_sum.csv")
plt.plot(df_sports.Year, df_sports.Global_Sales)
plt.title("Genre: Sports")
plt.xlabel("Year")
plt.ylabel("Global Sales (million)")
plt.savefig("sports_vgs.png")
plt.show()

#Visualisierung VGS Genre: Strategy
df_strategy = pd.read_csv("strategy_vgs_sum.csv")
plt.plot(df_strategy.Year, df_strategy.Global_Sales)
plt.title("Genre: Strategy")
plt.xlabel("Year")
plt.ylabel("Global Sales (million)")
plt.savefig("strategy_vgs.png")
plt.show()

#Visualisierung VGS Genre: Overview
df_overview_vgs = pd.read_csv("genre_overview_vgs.csv")
df_overview_vgs.plot(x="Year")
plt.savefig("overview_vgs.png")
plt.show()

#Visualisierung Twitch Genre: Overview
df_overview_tgd = pd.read_csv("genre_overview_tgd.csv")
df_overview_tgd.plot(x="Twitch_Year")
plt.savefig("overview_tgd.png")
plt.show()

#Visualisierung VGS Anzahl Games
df_count = pd.read_csv("genre_count_vgs.csv")
plt.bar(df_count.Genre, df_count.Count)
plt.rcParams.update({'font.size': 20})
plt.title("Genre spread")
plt.xlabel("Genre", fontsize=16)
plt.ylabel("Amount (Games)", fontsize=16)
fig3 = matplotlib.pyplot.gcf()
fig3.set_size_inches(14, 10)
fig3.savefig("count.png")
plt.show()

#Visualisierung Twitch Umsatz
df_totaltgd = pd.read_csv("total_tgd_year2.csv")
plt.bar(df_totaltgd.Year, df_totaltgd.Total)
plt.rcParams.update({'font.size': 20})
plt.title("Twitch revenue")
plt.xlabel("Year", fontsize=16)
plt.ylabel("Total (million)", fontsize=16)
fig3 = matplotlib.pyplot.gcf()
fig3.set_size_inches(14, 10)
fig3.savefig("total_tgd.png")
plt.show()

#Visualisierung Anzahl Verkäufe von Games pro Jahr
df_countyear = pd.read_csv("year_count.csv")
plt.bar(df_countyear.Year, df_countyear.Count)
plt.rcParams.update({'font.size': 20})
plt.title("Game Sales spread")
plt.xlabel("Year", fontsize=16)
plt.ylabel("Amount", fontsize=16)
fig3 = matplotlib.pyplot.gcf()
fig3.set_size_inches(14, 10)
fig3.savefig("count_year_vgs.png")
plt.show()