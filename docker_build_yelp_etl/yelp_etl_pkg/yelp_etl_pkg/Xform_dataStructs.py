import pandas as pd
import json
import numpy as np
import sqlite3

def transform_q2(df_ljoin_urbc):
    df_q2 = df_ljoin_urbc.groupby(['Business - Id', 'Business - Name']).mean()
    df_q2 = df_q2.reset_index()
    df_q2_w = df_q2[['Business - Id', 'Business - Name', 'Review - Stars']]
    return df_q2_w

def derive_zips(df_ljoin_urbc):
    df_ljoin_urbc['zip code'] = df_ljoin_urbc['Business - Address'].str.extract(r'(\d{5}\-?\d{0,4})')
    #df_part_o = df_ljoin_urbc[df_ljoin_urbc['zip code'].isnotnull()]
    #df_part_t = df_ljoin_urbc[df_ljoin_urbc['zip code'].isnull()]

    # Calculating Zip codes using Latitude and Longitude

    return df_ljoin_urbc

def transform_q3(df_ljoin_urbc):
    df_ljoin_urbc = derive_zips(df_ljoin_urbc)
    df_q3 = df_ljoin_urbc.groupby(['zip code']).size().to_frame('size')
    df_q3_w = df_q3.reset_index().sort_values(['size'], ascending= False).nlargest(5, columns= 'size')

    lst = []
    for i in df_q3_w['zip code']:
        lst.append(i)
    
    df_q3_filter = df_ljoin_urbc[df_ljoin_urbc['zip code'].isin(lst)]
    df_q3_filter.head(5)

    df_q3_filter_w = df_q3_filter.groupby(['zip code']).mean()
    df_q3_filter_w = df_q3_filter_w.reset_index()
    df_q3_filter_w = df_q3_filter_w[['zip code', 'Review - Stars']]
    return df_q3_filter_w    

def transform_q4(df_ljoin_urbc):
    df_q4 = df_ljoin_urbc.groupby(['User - Id']).count()
    df_q4 = df_q4.reset_index()
    df_q4 = df_q4[['Review - Id', 'User - Id']]
    df_q4 = df_q4.sort_values(['Review - Id'], ascending= False)
    df_q4_w = df_q4.head(10)
    return df_q4_w    