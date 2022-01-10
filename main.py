import pandas as pd
import re

df_vgs = pd.read_csv('vgsales.csv')
df_tgd = pd.read_csv('Twitch_game_data.csv')

#print(df_vgs.head())
#print(df_tgd.head())

##print(df_vgs.shape)
##print(df_vgs.Rank.nunique())

#Berechnung des Umsatzes von Twitch
df_tgd['Total'] = df_tgd['Hours_watched'] / (10/60) * 0.751 * 3.5 * (df_tgd["Avg_viewers"] / 1000)
df_tgd.to_csv("Twitch_game_data_total.csv")

#unnötige Überprüfung
df_cod = df_vgs[df_vgs["Name"] == "Call of Duty 3"]
df_cod.to_csv("cod.csv")

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

#unnötige Überprüfung
df_cod2 = df_final[df_final["Name"] == "Call of Duty 3"]
df_cod2.to_csv("cod2.csv")

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
all_tgd = [df_sum2016, df_sum2017, df_sum2018, df_sum2019, df_sum2020, df_sum2021]
df_finaltgd = pd.concat(all_tgd)
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

#Filter nach einzelnen Genre
df_action = df_join[df_join["Genre"] == "Action"]
df_action.to_csv("action_genre.csv", index=False)

"""
games_list = []

df_tgd = df_tgd.dropna(subset=['Game'])

for index, row in df_vgs.iterrows():
    games_list.append(row['Name'])

pattern = ' | '.join(games_list)

testlist = ['League', 'hundr']
test = ' | '.join(testlist)

print(df_tgd.loc[df_tgd['Game'].str.contains(test)])
"""



##df_tgd_v2 = df_tgd
##df_tgd_v3 = df_tgd


"""for index, row in df_tgd.iterrows():
    if row['Game'] not in games_list:
        df_tgd_v2 = df_tgd_v2.drop(index)
    else:
        df_tgd_v3 = df_tgd_v3.drop(index)

df_tgd_v2.to_csv('empty.csv')

print(df_tgd['Game'].unique())"""



