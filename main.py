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

for index, row in df_tgd.iterrows():
    if row['Game'] not in games_list:
        df_tgd = df_tgd.drop(index)

print(df_tgd['Game'].unique())
