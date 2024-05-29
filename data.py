import pandas as pd

def read_country_data():
    return pd.read_csv('data/Country.csv')

def read_leagues_data():
    return pd.read_csv('data/Leagues.csv')

def read_teams_data():
    return pd.read_csv('data/Teams.csv')

def read_managers_data():
    return pd.read_csv('data/Managers.csv')