#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd

class GetTopPlayer:
    
    def __init__(self, team_html):
        
        self.team_html = team_html

    def final_top_players(self):

        df = pd.read_csv(f'data/{self.team_html}_season_stats.csv')

        df.rename(columns = {'Unnamed: 1': 'Name'}, inplace = True)

        df['Name'] = df['Name'].str.split('\\').str[0]

        top_players = []

        team = f'{self.team_html.title()}'

        df['Team'] = team

        df = df[['Name', 'Team', 'G', 'TRB', 'AST', 'PTS/G']]

        df = df.loc[df['G'] >= 45]

        df_trb = df.sort_values(['TRB', 'G'], ascending=False)

        df_pts = df.sort_values(['PTS/G', 'G'], ascending=False)

        df_ast = df.sort_values(['AST', 'G'], ascending=False)
        
        df_final = pd.DataFrame()
        df_final = df_final.append([df_pts[:3], df_ast[:3], df_trb[:3]])
        df_final = df_final.drop_duplicates()
        
        print(df_final)

        with open(f'nba_compiled_data.csv', 'a') as f:
            df_final.to_csv(f, header = False, index = False)








