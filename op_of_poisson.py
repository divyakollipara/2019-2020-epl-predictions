import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
from scipy.stats import poisson
x = 'Burnley'
y = 'Swansea'
def poisson_output(x,y):
    pred161718 = pd.read_csv("/home/divya/Desktop/poissonop/new3sets.csv")
    avg_goals_scored_home = pred161718['FTHG'].mean()
    avg_goals_scored_away = pred161718['FTAG'].mean()
    avg_goals_conceded_home = avg_goals_scored_away
    avg_goals_conceded_away = avg_goals_scored_home
    avg_goals_scored_home_team = pred161718[pred161718['HomeTeam'] == x]['FTHG'].mean()
    attack_strength_home_team = avg_goals_scored_home_team/avg_goals_scored_home
    avg_goals_conceded_away_team = pred161718[pred161718['AwayTeam'] == y]['FTHG'].mean()
    defense_strength_away_team = avg_goals_conceded_away_team/avg_goals_conceded_away
    avg_goals_scored_away_team = pred161718[pred161718['AwayTeam'] == x]['FTAG'].mean()
    attack_strength_away_team = avg_goals_scored_away_team/avg_goals_scored_away
    avg_goals_conceded_home_team = pred161718[pred161718['HomeTeam'] == y]['FTAG'].mean()
    defense_strength_home_team = avg_goals_conceded_home_team/avg_goals_conceded_home
    exp_goals_home_team = attack_strength_home_team * defense_strength_away_team * avg_goals_scored_home
    exp_goals_away_team = attack_strength_away_team*defense_strength_home_team*avg_goals_scored_away
    prob_goals_home_team = [poisson.pmf(i,exp_goals_home_team) for i in range(6)]
    prob_goals_away_team = [poisson.pmf(i,exp_goals_away_team) for i in range(6)]
    print(prob_goals_home_team,prob_goals_away_team)
    return(prob_goals_home_team,prob_goals_away_team)
poisson_output(x,y)
