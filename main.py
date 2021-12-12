import pandas as pd

df_vgs = pd.read_csv('vgsales.csv')
df_tgd = pd.read_csv('Twitch_game_data.csv')

print(df_vgs.head())
print(df_tgd.head())

print(df_vgs.shape)
print(df_vgs.Rank.nunique())

games_list = []

df_tgd = df_tgd.dropna(subset=['Game'])

for index, row in df_vgs.iterrows():
    games_list.append(row['Name'])

df_tgd_v2 = df_tgd
df_tgd_v3 = df_tgd


for index, row in df_tgd.iterrows():
    if row['Game'] not in games_list:
        df_tgd_v2 = df_tgd_v2.drop(index)
    else:
        df_tgd_v3 = df_tgd_v3.drop(index)

df_tgd_v2.to_csv('empty.csv')

print(df_tgd['Game'].unique())
