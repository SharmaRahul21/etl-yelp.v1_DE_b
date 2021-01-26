import pandas as pd
import json
import numpy as np
import sqlite3

def extract_data(data_path):

    # Loading data from SQLITE Db
    cnx = sqlite3.connect(data_path + "/user.sqlite")
    df_users = pd.read_sql_query("SELECT * FROM Users2", cnx)
    print("Loaded Users data")
    df_ba = pd.read_sql_query("SELECT * FROM business_attributes", cnx)
    print("Loaded Business attrributes data")

    # Loading data from CSV Files
    df_1_rev = pd.read_csv(data_path + "/reviews1.csv")
    df_2_rev = pd.read_csv(data_path + "/reviews2.csv")
    df_3_rev = pd.read_csv(data_path + "/reviews3.csv")
    df_4_rev = pd.read_csv(data_path + "/reviews4.csv")
    df_5_rev = pd.read_csv(data_path + "/reviews5.csv")
    
    df_r = pd.concat([df_1_rev, df_2_rev, df_3_rev, df_4_rev, df_5_rev])
    print("Concatenated and Loaded Reviews data")

    # Loading data from JSON Files
    def json_prepro(df):
        df_tr = df.transpose()
        df_tr = df_tr.reset_index()
        df_tr = df_tr.rename(columns={"index": "Id"})
        return df_tr
    
    df_1_bc = pd.read_json(data_path + "/business_composition_final1.json")
    df_1_bctr = json_prepro(df_1_bc)
    df_2_bc = pd.read_json(data_path + "/business_composition_final2.json")
    df_2_bctr = json_prepro(df_2_bc)
    df_3_bc = pd.read_json(data_path + "/business_composition_final3.json")
    df_3_bctr = json_prepro(df_3_bc)
    df_4_bc = pd.read_json(data_path + "/business_composition_final4.json")
    df_4_bctr = json_prepro(df_4_bc)
    df_5_bc = pd.read_json(data_path + "/business_composition_final5.json")
    df_5_bctr = json_prepro(df_5_bc)

    df_business_ctr = pd.concat([df_1_bctr, df_2_bctr, df_3_bctr, df_4_bctr, df_5_bctr])
    print("Concatenated and Loaded Business CTR data")
    print(df_business_ctr.columns)

    return df_users, df_r, df_business_ctr, df_ba

def create_base_ds(df_users, df_r, df_business_ctr, df_ba):
    df_ljoin_user_rev = df_users.merge(df_r, on = ['User - Id', 'Business - Id', 'Review - Id'], how = 'left')
    print("Join computed for Users and Reviews")

    df_ljoin_urbc = df_ljoin_user_rev.merge(df_business_ctr, left_on = ['Business - Id'], right_on = ['Id'], how = 'left')
    print("Join computed for Users, Reviews and Business Composition")

    #df_ljoin_urbc = df_ljoin_urbc.set_index(['Business - Id'])
    #df_ba = df_ba.set_index(['Business - Id'])
    #df_final = df_ljoin_urbc.merge(df_ba, on = ['Business - Id'], how = 'left')
    #print("Join computed for Final DF")

    return df_ljoin_urbc

def write_as_csv(df, path_to_write):
    print("Writing the DF to path: ", path_to_write)
    df.to_csv(path_to_write)