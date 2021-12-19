import pandas as pd
import re

df_vgs = pd.read_csv('vgsales.csv')
df_tgd = pd.read_csv('Twitch_game_data.csv')

#print(df_vgs.head())
#print(df_tgd.head())

##print(df_vgs.shape)
##print(df_vgs.Rank.nunique())

df_tgd['Total'] = df_tgd['Hours_watched'] / (10/60) * 0.751 * 3.5

df_tgd.to_csv('empty.csv', index=False)

games_list = []

df_tgd = df_tgd.dropna(subset=['Game'])

for index, row in df_vgs.iterrows():
    games_list.append(row['Name'])

pattern = ' | '.join(games_list)

testlist = ['League', 'hundr']
test = ' | '.join(testlist)

print(df_tgd.loc[df_tgd['Game'].str.contains(test)])




##df_tgd_v2 = df_tgd
##df_tgd_v3 = df_tgd


"""for index, row in df_tgd.iterrows():
    if row['Game'] not in games_list:
        df_tgd_v2 = df_tgd_v2.drop(index)
    else:
        df_tgd_v3 = df_tgd_v3.drop(index)

df_tgd_v2.to_csv('empty.csv')

print(df_tgd['Game'].unique())"""



