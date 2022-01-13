# @since: 2021-10-1
# @author: Gabriel Marojevic, Daniel Japs, Waldemar Granson, Lukas Gabriel, Kai Perich

# Import Packages
import pandas as pd

# @source https://www.kaggle.com/gregorut/videogamesales
df_vgs = pd.read_csv('vgsales.csv')

# @source https://www.kaggle.com/rankirsh/evolution-of-top-games-on-twitch
df_tgd = pd.read_csv('Twitch_game_data.csv')


#Berechnung des Umsatzes von Twitch
SPartnered = df_tgd['Streamers'] * 0.01
SAffiliate = df_tgd['Streamers'] * 0.1
df_tgd['Total'] = (SPartnered * 3000 + SAffiliate * 100) / 1000000
df_tgd.to_csv("Twitch_game_data_total.csv")


#alle Sales der gleichen Spiele werden addiert und in neuem Dataframe gespeichert
df_test = df_vgs.groupby("Name")["Global_Sales"].sum()
df_test.to_csv("test.csv")

#Dataframe VGS säubern
df_vgs.drop(["Rank", "Publisher", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales", "Platform"], axis=1, inplace=True)
df_vgs = df_vgs.drop_duplicates(subset="Name", keep="first")
df_vgs.to_csv("new_vgs.csv", index=False)

#gesäuberter Dataframe VGS und addierte Global Sales werden merged um Kombination aus Global Sales und Genre,Year zu haben
df_final = pd.merge(df_vgs, df_test, on="Name")
df_final.to_csv("final.csv")


#Twitch Dataset säubern
df_newtgd = pd.read_csv("Twitch_game_data_total.csv")
df_newtgd.drop(["Month", "Hours_Streamed", "Peak_viewers", "Peak_channels", "Streamers", "Avg_channels", "Avg_viewer_ratio"], axis=1, inplace=True)
df_newtgd.to_csv("new_tgd.csv", index=False)

#split auf Jahre, damit ich später nicht alle Total über alle Jahre addiere sondern Totals pro Jahr
df_tgd2016 = df_newtgd[df_newtgd["Year"] == 2016]
df_tgd2016.to_csv("tgd2016.csv")
df_tgd2017 = df_newtgd[df_newtgd["Year"] == 2017]
df_tgd2017.to_csv("tgd2017.csv")
df_tgd2018 = df_newtgd[df_newtgd["Year"] == 2018]
df_tgd2018.to_csv("tgd2018.csv")
df_tgd2019 = df_newtgd[df_newtgd["Year"] == 2019]
df_tgd2019.to_csv("tgd2019.csv")
df_tgd2020 = df_newtgd[df_newtgd["Year"] == 2020]
df_tgd2020.to_csv("tgd2020.csv")
df_tgd2021 = df_newtgd[df_newtgd["Year"] == 2021]
df_tgd2021.to_csv("tgd2021.csv")

#addiere alle Totals aus jedem Monat im jeweiligen Jahr, füge Colum Jahr hinzu
df_sum2016 = df_tgd2016.groupby("Game")["Total"].sum()
df_sum2016.to_csv("sum_2016.csv")
df_sum2017 = df_tgd2017.groupby("Game")["Total"].sum()
df_sum2017.to_csv("sum_2017.csv")
df_sum2018 = df_tgd2018.groupby("Game")["Total"].sum()
df_sum2018.to_csv("sum_2018.csv")
df_sum2019 = df_tgd2019.groupby("Game")["Total"].sum()
df_sum2019.to_csv("sum_2019.csv")
df_sum2020 = df_tgd2020.groupby("Game")["Total"].sum()
df_sum2020.to_csv("sum_2020.csv")
df_sum2021 = df_tgd2021.groupby("Game")["Total"].sum()
df_sum2021.to_csv("sum_2021.csv")

#Genre hinzufügen, Hours watched nach Genre im jeweiligen Jahr berechnen
df_filter = pd.read_csv("final.csv")
df_filter.rename(columns={"Name": "Game"}, inplace=True)
df_join1 = pd.merge(df_tgd2016, df_filter, on="Game")
df_join1.to_csv('hw2016.csv', index=False)
df_genre2016 = df_join1.groupby("Genre")["Hours_watched"].sum()
df_genre2016.to_csv("genre_hw2016.csv")
df_join2 = pd.merge(df_tgd2017, df_filter, on="Game")
df_join2.to_csv('hw2017.csv', index=False)
df_genre2017 = df_join2.groupby("Genre")["Hours_watched"].sum()
df_genre2017.to_csv("genre_hw2017.csv")
df_join3 = pd.merge(df_tgd2018, df_filter, on="Game")
df_join3.to_csv('hw2018.csv', index=False)
df_genre2018 = df_join3.groupby("Genre")["Hours_watched"].sum()
df_genre2018.to_csv("genre_hw2018.csv")
df_join4 = pd.merge(df_tgd2019, df_filter, on="Game")
df_join4.to_csv('hw2019.csv', index=False)
df_genre2019 = df_join4.groupby("Genre")["Hours_watched"].sum()
df_genre2019.to_csv("genre_hw2019.csv")
df_join5 = pd.merge(df_tgd2020, df_filter, on="Game")
df_join5.to_csv('hw2020.csv', index=False)
df_genre2020 = df_join5.groupby("Genre")["Hours_watched"].sum()
df_genre2020.to_csv("genre_hw2020.csv")
df_join6 = pd.merge(df_tgd2021, df_filter, on="Game")
df_join6.to_csv('hw2021.csv', index=False)
df_genre2021 = df_join6.groupby("Genre")["Hours_watched"].sum()
df_genre2021.to_csv("genre_hw2021.csv")

#Füge jedem Datensatz wieder sein jeweiliges Jahr hinzu
df_genre2016 = pd.read_csv("genre_hw2016.csv")
df_genre2016["Twitch_Year"] = "2016"
df_genre2016.to_csv("genre_hw2016.csv", index=False)
df_genre2017 = pd.read_csv("genre_hw2017.csv")
df_genre2017["Twitch_Year"] = "2017"
df_genre2017.to_csv("genre_hw2017.csv", index=False)
df_genre2018 = pd.read_csv("genre_hw2018.csv")
df_genre2018["Twitch_Year"] = "2018"
df_genre2018.to_csv("genre_hw2018.csv", index=False)
df_genre2019 = pd.read_csv("genre_hw2019.csv")
df_genre2019["Twitch_Year"] = "2019"
df_genre2019.to_csv("genre_hw2019.csv", index=False)
df_genre2020 = pd.read_csv("genre_hw2020.csv")
df_genre2020["Twitch_Year"] = "2020"
df_genre2020.to_csv("genre_hw2020.csv", index=False)
df_genre2021 = pd.read_csv("genre_hw2021.csv")
df_genre2021["Twitch_Year"] = "2021"
df_genre2021.to_csv("genre_hw2021.csv", index=False)

#Genre Puzzle hinzufügen
DAddPuzzle = {"Genre":"Puzzle", "Hours_watched":0, "Twitch_Year":"2017"}
df_genre2017 = df_genre2017.append(DAddPuzzle, ignore_index=True)
df_genre2017.to_csv("genre_hw2017.csv", index=False)
DAddPuzzle = {"Genre":"Puzzle", "Hours_watched":0, "Twitch_Year":"2020"}
df_genre2020 = df_genre2020.append(DAddPuzzle, ignore_index=True)
df_genre2020.to_csv("genre_hw2020.csv", index=False)
DAddPuzzle = {"Genre":"Puzzle", "Hours_watched":0, "Twitch_Year":"2021"}
df_genre2021 = df_genre2021.append(DAddPuzzle, ignore_index=True)
df_genre2021.to_csv("genre_hw2021.csv", index=False)


#alle Datensätze wieder zusammenfügen
LAllTgd = [df_genre2016, df_genre2017, df_genre2018, df_genre2019, df_genre2020, df_genre2021]
df_finaltgd = pd.concat(LAllTgd)
df_finaltgd.to_csv("final_hw.csv", index=False)

#Export Genre mit Jahr Twitch
df_action = df_finaltgd[df_finaltgd["Genre"] == "Action"]
df_action.to_csv("action.csv", index=False)
df_adventure = df_finaltgd[df_finaltgd["Genre"] == "Adventure"]
df_adventure.to_csv("adventure.csv", index=False)
df_fighting = df_finaltgd[df_finaltgd["Genre"] == "Fighting"]
df_fighting.to_csv("fighting.csv", index=False)
df_misc = df_finaltgd[df_finaltgd["Genre"] == "Misc"]
df_misc.to_csv("misc.csv", index=False)
df_platform = df_finaltgd[df_finaltgd["Genre"] == "Platform"]
df_platform.to_csv("platform.csv", index=False)
df_puzzle = df_finaltgd[df_finaltgd["Genre"] == "Puzzle"]
df_puzzle.to_csv("puzzle.csv", index=False)
df_racing = df_finaltgd[df_finaltgd["Genre"] == "Racing"]
df_racing.to_csv("racing.csv", index=False)
df_rp = df_finaltgd[df_finaltgd["Genre"] == "Role-Playing"]
df_rp.to_csv("rp.csv", index=False)
df_shooter = df_finaltgd[df_finaltgd["Genre"] == "Shooter"]
df_shooter.to_csv("shooter.csv", index=False)
df_simulation = df_finaltgd[df_finaltgd["Genre"] == "Simulation"]
df_simulation.to_csv("simulation.csv", index=False)
df_sports = df_finaltgd[df_finaltgd["Genre"] == "Sports"]
df_sports.to_csv("sports.csv", index=False)
df_strategy = df_finaltgd[df_finaltgd["Genre"] == "Strategy"]
df_strategy.to_csv("strategy.csv", index=False)

#Rearrange um Gerne als Spalten zu bekommen
df_tgd1 = pd.read_csv("action.csv")
df_tgd1.drop("Genre", axis=1, inplace=True)
df_tgd1.rename(columns={"Hours_watched":"Action"}, inplace=True)
df_tgd2 = pd.read_csv("adventure.csv")
df_tgd2.drop("Genre", axis=1, inplace=True)
df_tgd2.rename(columns={"Hours_watched":"Adventure"}, inplace=True)
df_result1 = pd.merge(df_tgd1, df_tgd2, on="Twitch_Year")
df_tgd3 = pd.read_csv("fighting.csv")
df_tgd3.drop("Genre", axis=1, inplace=True)
df_tgd3.rename(columns={"Hours_watched":"Fighting"}, inplace=True)
df_result1 = pd.merge(df_result1, df_tgd3, on="Twitch_Year")
df_tgd4 = pd.read_csv("misc.csv")
df_tgd4.drop("Genre", axis=1, inplace=True)
df_tgd4.rename(columns={"Hours_watched":"Misc"}, inplace=True)
df_result1 = pd.merge(df_result1, df_tgd4, on="Twitch_Year")
df_tgd5 = pd.read_csv("platform.csv")
df_tgd5.drop("Genre", axis=1, inplace=True)
df_tgd5.rename(columns={"Hours_watched":"Platform"}, inplace=True)
df_result1 = pd.merge(df_result1, df_tgd5, on="Twitch_Year")
df_tgd6 = pd.read_csv("puzzle.csv")
df_tgd6.drop("Genre", axis=1, inplace=True)
df_tgd6.rename(columns={"Hours_watched":"Puzzle"}, inplace=True)
df_result1 = pd.merge(df_result1, df_tgd6, on="Twitch_Year")
df_tgd7 = pd.read_csv("racing.csv")
df_tgd7.drop("Genre", axis=1, inplace=True)
df_tgd7.rename(columns={"Global_Sales":"Racing"}, inplace=True)
df_result1 = pd.merge(df_result1, df_tgd7, on="Twitch_Year")
df_tgd8 = pd.read_csv("rp.csv")
df_tgd8.drop("Genre", axis=1, inplace=True)
df_tgd8.rename(columns={"Hours_watched":"Role-Playing"}, inplace=True)
df_result1 = pd.merge(df_result1, df_tgd8, on="Twitch_Year")
df_tgd9 = pd.read_csv("shooter.csv")
df_tgd9.drop("Genre", axis=1, inplace=True)
df_tgd9.rename(columns={"Hours_watched":"Shooter"}, inplace=True)
df_result1 = pd.merge(df_result1, df_tgd9, on="Twitch_Year")
df_tgd10 = pd.read_csv("simulation.csv")
df_tgd10.drop("Genre", axis=1, inplace=True)
df_tgd10.rename(columns={"Hours_watched":"Simulation"}, inplace=True)
df_result1 = pd.merge(df_result1, df_tgd10, on="Twitch_Year")
df_tgd11 = pd.read_csv("sports.csv")
df_tgd11.drop("Genre", axis=1, inplace=True)
df_tgd11.rename(columns={"Hours_watched":"Sports"}, inplace=True)
df_result1 = pd.merge(df_result1, df_tgd11, on="Twitch_Year")
df_tgd12 = pd.read_csv("strategy.csv")
df_tgd12.drop("Genre", axis=1, inplace=True)
df_tgd12.rename(columns={"Hours_watched":"Strategy"}, inplace=True)
df_result1 = pd.merge(df_result1, df_tgd12, on="Twitch_Year")
df_result1.to_csv("genre_overview_tgd.csv", index=False)

#Export Genre mit Jahr VGS
df_action = df_final[df_final["Genre"] == "Action"]
df_action.to_csv("action_VGS.csv", index=False)
df_adventure = df_final[df_final["Genre"] == "Adventure"]
df_adventure.to_csv("adventure_VGS.csv", index=False)
df_fighting = df_final[df_final["Genre"] == "Fighting"]
df_fighting.to_csv("fighting_VGS.csv", index=False)
df_misc = df_final[df_final["Genre"] == "Misc"]
df_misc.to_csv("misc_VGS.csv", index=False)
df_platform = df_final[df_final["Genre"] == "Platform"]
df_platform.to_csv("platform_VGS.csv", index=False)
df_puzzle = df_final[df_final["Genre"] == "Puzzle"]
df_puzzle.to_csv("puzzle_VGS.csv", index=False)
df_racing = df_final[df_final["Genre"] == "Racing"]
df_racing.to_csv("racing_VGS.csv", index=False)
df_rp = df_final[df_final["Genre"] == "Role-Playing"]
df_rp.to_csv("rp_VGS.csv", index=False)
df_shooter = df_final[df_final["Genre"] == "Shooter"]
df_shooter.to_csv("shooter_VGS.csv", index=False)
df_simulation = df_final[df_final["Genre"] == "Simulation"]
df_simulation.to_csv("simulation_VGS.csv", index=False)
df_sports = df_final[df_final["Genre"] == "Sports"]
df_sports.to_csv("sports_VGS.csv", index=False)
df_strategy = df_final[df_final["Genre"] == "Strategy"]
df_strategy.to_csv("strategy_VGS.csv", index=False)

#Sales pro Jahr ausrechnen im jeweiligen Genre
df_vgs = df_action.groupby("Year")["Global_Sales"].sum()
df_vgs.to_csv("action_vgs_sum.csv")
df_vgs = df_adventure.groupby("Year")["Global_Sales"].sum()
df_vgs.to_csv("adventure_vgs_sum.csv")
df_vgs = df_fighting.groupby("Year")["Global_Sales"].sum()
df_vgs.to_csv("fighting_vgs_sum.csv")
df_vgs = df_misc.groupby("Year")["Global_Sales"].sum()
df_vgs.to_csv("misc_vgs_sum.csv")
df_vgs = df_platform.groupby("Year")["Global_Sales"].sum()
df_vgs.to_csv("platform_vgs_sum.csv")
df_vgs = df_puzzle.groupby("Year")["Global_Sales"].sum()
df_vgs.to_csv("puzzle_vgs_sum.csv")
df_vgs = df_racing.groupby("Year")["Global_Sales"].sum()
df_vgs.to_csv("racing_vgs_sum.csv")
df_vgs = df_rp.groupby("Year")["Global_Sales"].sum()
df_vgs.to_csv("rp_vgs_sum.csv")
df_vgs = df_shooter.groupby("Year")["Global_Sales"].sum()
df_vgs.to_csv("shooter_vgs_sum.csv")
df_vgs = df_simulation.groupby("Year")["Global_Sales"].sum()
df_vgs.to_csv("simulation_vgs_sum.csv")
df_vgs = df_sports.groupby("Year")["Global_Sales"].sum()
df_vgs.to_csv("sports_vgs_sum.csv")
df_vgs = df_strategy.groupby("Year")["Global_Sales"].sum()
df_vgs.to_csv("strategy_vgs_sum.csv")

#Fehlerhafte Daten entfernen
df_vgs = pd.read_csv("simulation_vgs_sum.csv")
df_drop = df_vgs.drop(df_vgs[df_vgs.Year > 2015].index)
df_drop.to_csv("simulation_vgs_sum.csv", index=False)

#Overall genre sales
df_vgs1 = pd.read_csv("action_vgs_sum.csv")
df_vgs1.rename(columns={"Global_Sales":"Action"}, inplace=True)
df_vgs2 = pd.read_csv("adventure_vgs_sum.csv")
df_vgs2.rename(columns={"Global_Sales":"Adventure"}, inplace=True)
df_result = pd.merge(df_vgs1, df_vgs2, on="Year", how="outer")
df_vgs3 = pd.read_csv("fighting_vgs_sum.csv")
df_vgs3.rename(columns={"Global_Sales":"Fighting"}, inplace=True)
df_result = pd.merge(df_result, df_vgs3, on="Year", how="outer")
df_vgs4 = pd.read_csv("misc_vgs_sum.csv")
df_vgs4.rename(columns={"Global_Sales":"Misc"}, inplace=True)
df_result = pd.merge(df_result, df_vgs4, on="Year", how="outer")
df_vgs5 = pd.read_csv("platform_vgs_sum.csv")
df_vgs5.rename(columns={"Global_Sales":"Platform"}, inplace=True)
df_result = pd.merge(df_result, df_vgs5, on="Year", how="outer")
df_vgs6 = pd.read_csv("puzzle_vgs_sum.csv")
df_vgs6.rename(columns={"Global_Sales":"Puzzle"}, inplace=True)
df_result = pd.merge(df_result, df_vgs6, on="Year", how="outer")
df_vgs7 = pd.read_csv("racing_vgs_sum.csv")
df_vgs7.rename(columns={"Global_Sales":"Racing"}, inplace=True)
df_result = pd.merge(df_result, df_vgs7, on="Year", how="outer")
df_vgs8 = pd.read_csv("rp_vgs_sum.csv")
df_vgs8.rename(columns={"Global_Sales":"Role-Playing"}, inplace=True)
df_result = pd.merge(df_result, df_vgs8, on="Year", how="outer")
df_vgs9 = pd.read_csv("shooter_vgs_sum.csv")
df_vgs9.rename(columns={"Global_Sales":"Shooter"}, inplace=True)
df_result = pd.merge(df_result, df_vgs9, on="Year", how="outer")
df_vgs10 = pd.read_csv("simulation_vgs_sum.csv")
df_vgs10.rename(columns={"Global_Sales":"Simulation"}, inplace=True)
df_result = pd.merge(df_result, df_vgs10, on="Year", how="outer")
df_vgs11 = pd.read_csv("sports_vgs_sum.csv")
df_vgs11.rename(columns={"Global_Sales":"Sports"}, inplace=True)
df_result = pd.merge(df_result, df_vgs11, on="Year", how="outer")
df_vgs12 = pd.read_csv("strategy_vgs_sum.csv")
df_vgs12.rename(columns={"Global_Sales":"Strategy"}, inplace=True)
df_result = pd.merge(df_result, df_vgs12, on="Year", how="outer")
df_result.to_csv("genre_overview_vgs.csv", index=False)


#Anzahl Genre
df_genrestats = df_final["Genre"].value_counts()
df_genrestats.to_csv("genre_count_vgs.csv")
df_genrestats = pd.read_csv("genre_count_vgs.csv")
df_genrestats.rename(columns={"Genre":"Count", "Unnamed: 0":"Genre"}, inplace=True)
df_genrestats.to_csv("genre_count_vgs.csv", index=False)

#Anzahl Jahre
df_vgsread = pd.read_csv("vgsales.csv")
df_yearstats = df_vgsread["Year"].value_counts()
df_yearstats.to_csv("year_count.csv")
df_vgsread = pd.read_csv("year_count.csv")
df_vgsread.rename(columns={"Year":"Count", "Unnamed: 0":"Year"}, inplace=True)
df_vgsread.sort_values("Year", axis = 0, ascending = True, inplace = True)
df_vgsread.to_csv("year_count.csv", index=False)

#Füge jedem Datensatz wieder sein jeweiliges Jahr hinzu
df_sum2016 = pd.read_csv("sum_2016.csv")
df_sum2016["Twitch_Year"] = "2016"
df_sum2016.to_csv("sum_2016.csv", index=False)
df_sum2017 = pd.read_csv("sum_2017.csv")
df_sum2017["Twitch_Year"] = "2017"
df_sum2017.to_csv("sum_2017.csv", index=False)
df_sum2018 = pd.read_csv("sum_2018.csv")
df_sum2018["Twitch_Year"] = "2018"
df_sum2018.to_csv("sum_2018.csv", index=False)
df_sum2019 = pd.read_csv("sum_2019.csv")
df_sum2019["Twitch_Year"] = "2019"
df_sum2019.to_csv("sum_2019.csv", index=False)
df_sum2020 = pd.read_csv("sum_2020.csv")
df_sum2020["Twitch_Year"] = "2020"
df_sum2020.to_csv("sum_2020.csv", index=False)
df_sum2021 = pd.read_csv("sum_2021.csv")
df_sum2021["Twitch_Year"] = "2021"
df_sum2021.to_csv("sum_2021.csv", index=False)

#alle Datensätze wieder zusammenfügen
LAllTgd = [df_sum2016, df_sum2017, df_sum2018, df_sum2019, df_sum2020, df_sum2021]
df_finaltgd = pd.concat(LAllTgd)
df_finaltgd.to_csv("final_tgd.csv")

#Columns identisch benennen, merge über Name um Genre zu Twitch hinzuzufügen
df_filter = pd.read_csv("final.csv")
df_filter.rename(columns={"Name":"Game"},inplace=True)
df_join = pd.merge(df_finaltgd, df_filter, on="Game")
df_join.to_csv('empty.csv', index=False)

#Twitch Data endgültig säubern
df_join.drop(["Year", "Global_Sales", "Unnamed: 0"], axis=1, inplace=True)
df_join.to_csv("tgd_data.csv")

#Berechnung Total für VGS, mit 60€ als Mittelwert
df_final["Total"] = df_final["Global_Sales"] * 60
df_final.to_csv("vgs_total.csv", index=False)

#Total
df_total2016 = df_join1.groupby("Genre")["Total"].sum()
df_total2016.to_csv("total_hw2016.csv")
df_total2017 = df_join2.groupby("Genre")["Total"].sum()
df_total2017.to_csv("total_hw2017.csv")
df_total2018 = df_join3.groupby("Genre")["Total"].sum()
df_total2018.to_csv("total_hw2018.csv")
df_total2019 = df_join4.groupby("Genre")["Total"].sum()
df_total2019.to_csv("total_hw2019.csv")
df_total2020 = df_join5.groupby("Genre")["Total"].sum()
df_total2020.to_csv("total_hw2020.csv")
df_total2021 = df_join6.groupby("Genre")["Total"].sum()
df_total2021.to_csv("total_hw2021.csv")


#Datensatz Jahr hinzufügen
df_total2016 = pd.read_csv("total_hw2016.csv")
df_total2016["Year"] = "2016"
df_total2016.to_csv("total_hw2016.csv", index=False)
df_total2017 = pd.read_csv("total_hw2017.csv")
df_total2017["Year"] = "2017"
df_total2017.to_csv("total_hw2017.csv", index=False)
df_total2018 = pd.read_csv("total_hw2018.csv")
df_total2018["Year"] = "2018"
df_total2018.to_csv("total_hw2018.csv", index=False)
df_total2019 = pd.read_csv("total_hw2019.csv")
df_total2019["Year"] = "2019"
df_total2019.to_csv("total_hw2019.csv", index=False)
df_total2020 = pd.read_csv("total_hw2020.csv")
df_total2020["Year"] = "2020"
df_total2020.to_csv("total_hw2020.csv", index=False)
df_total2021 = pd.read_csv("total_hw2021.csv")
df_total2021["Year"] = "2021"
df_total2021.to_csv("total_hw2021.csv", index=False)

#Zusammenfügen
LAllTgd = [df_total2016, df_total2017, df_total2018, df_total2019, df_total2020, df_total2021]
df_finaltgd = pd.concat(LAllTgd)
df_finaltgd.to_csv("total_tgd.csv", index=False)

#Umsatz nach Jahr addieren
df_totaltgd = df_finaltgd.groupby("Year")["Total"].sum()
df_totaltgd.to_csv("total_tgd_year.csv")

#Umsatz nach Jahr addieren ohne Genre Filter
df_totaltgd2 = pd.read_csv("Twitch_game_data_total.csv")
df_totaltgd3 = df_totaltgd2.groupby("Year")["Total"].sum()
df_totaltgd3.to_csv("total_tgd_year2.csv")



