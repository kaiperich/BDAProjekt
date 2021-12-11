import pandas as pd

df_vgs = pd.read_csv('vgsales.csv')
df_tgd = pd.read_csv('Twitch_game_data.csv')

print(df_vgs.head())
print(df_tgd.head())