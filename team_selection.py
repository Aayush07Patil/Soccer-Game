import time
from data import read_country_data, read_leagues_data, read_teams_data
import main

country_dict = read_country_data().set_index('country_id')['country_name'].to_dict()

def player_country_select():
    
    global number_pc
    
    print("\n#### Country Options ####")
    
    for k,v in country_dict.items():
        print(f"[{k}] {v}")
    
    number_pc = int(input("Choose your League or Press 0 to go back: "))
    
    if number_pc in country_dict:
        player_league_select()
    
    elif number_pc == 0:
        main.main_menu()    
    else:
        print("\nError please input a valid league id ")
        player_country_select() 

def opposition_country_select():
   
    global number_oc
    
    print("\n#### Country Options ####")
    
    for k,v in country_dict.items():
        print(f"[{k}] {v}")
    
    number_oc = int(input("Choose oppositions League or Press 0 to go back: "))
    
    if number_pc in country_dict:
        opposition_league_select()
    
    elif number_pc == 0:
        player_country_select()    
    else:
        print("\nError please input a valid league id ")
        opposition_country_select() 

def player_league_select():
    
    global number_pl
    
    leagues_data = read_leagues_data()
    
    while True:
        print('\n#### League Options ####')
        league_df = leagues_data[leagues_data['country_id'] == number_pc]
        
         
        league_name_dict = {i+1:team for i, team in enumerate(league_df['league_name'])}
              
        for k,v in league_name_dict.items():
            print(f"[{k}] {v}")
                    
        input_number_pl = int(input("\nSelect your team or Press 0 to go back: "))
        
        if input_number_pl in league_name_dict:
            league_name = league_name_dict[input_number_pl]
            number_pl= league_df.loc[league_df['league_name']== league_name,'league_id'].values[0]
            player_team_select()
            break
        
        elif input_number_pl == 0:
            player_country_select()
            break    
        else:
            print("\nError please input a valid league id ")
            time.sleep(2)    

def opposition_league_select():
    
    global number_ol
    
    leagues_data = read_leagues_data() 
    
    while True:
        print('\n#### League Options ####')
        league_df = leagues_data[leagues_data['country_id'] == number_oc]
        
         
        league_name_dict = {i+1:team for i, team in enumerate(league_df['league_name'])}
              
        for k,v in league_name_dict.items():
            print(f"[{k}] {v}")
                    
        input_number_ol = int(input("\nSelect your team or Press 0 to go back: "))
        
        if input_number_ol in league_name_dict:
            league_name = league_name_dict[input_number_ol]
            number_ol= league_df.loc[league_df['league_name']== league_name,'league_id'].values[0]
            opposition_team_select()
            break
        
        elif input_number_ol == 0:
            opposition_country_select()
            break    
        else:
            print("\nError please input a valid league id ")
            time.sleep(2)  

def player_team_select():
    
    global player_team
    global player_stadium
    global player_team_abbv
    global player_attack
    global player_midfield
    global player_defend
    global number_pt
    
    teams_data = read_teams_data()
    
    while True:
        print('\n#### Team Options ####')
        team_df = teams_data[teams_data['league_id'] == number_pl]
             
        teams_dict = {i+1:team for i, team in enumerate(team_df['team_name'])}
        stadium_dict = {i+1:team for i, team in enumerate(team_df['team_stadium'])}
        abbv_dict = {i+1:team for i, team in enumerate(team_df['team_abbv'])}
        attack_dict = {i+1:team for i, team in enumerate(team_df['attack'])}
        midfield_dict = {i+1:team for i, team in enumerate(team_df['midfield'])}
        defend_dict = {i+1:team for i, team in enumerate(team_df['defense'])}
                
        for k,v in teams_dict.items():
            print(f"[{k}] {v}")
                    
        input_number_pt = int(input("\nSelect your team or Press 0 to go back: "))
        
        if input_number_pt in teams_dict.keys():
            player_team = teams_dict[input_number_pt]
            player_stadium = stadium_dict[input_number_pt]
            player_team_abbv = abbv_dict[input_number_pt]
            player_attack = attack_dict[input_number_pt]
            player_midfield = midfield_dict[input_number_pt]
            player_defend = defend_dict[input_number_pt]
            number_pt = team_df.loc[team_df['team_name']== player_team,'team_id'].values[0]
            print(f"\nYou selected {player_team}")
            time.sleep(2)
            break
        
        elif input_number_pt == 0:
            player_league_select()
            break
        
        else:
            print("\nError Please input number mentioned on the left of the team you want to choice")
            time.sleep(2)
            
    return None

def opposition_team_select():
    
    global opposition_team
    global opposition_stadium
    global opposition_team_abbv
    global opposition_attack
    global opposition_midfield
    global opposition_defend
    global number_ot
    
    teams_data = read_teams_data()
    
    while True:
        print('\n#### Team Options ####')
        team_df = teams_data[teams_data['league_id'] == number_ol]
                
        teams_dict = {i+1:team for i, team in enumerate(team_df['team_name'])}
        stadium_dict = {i+1:team for i, team in enumerate(team_df['team_stadium'])}
        abbv_dict = {i+1:team for i, team in enumerate(team_df['team_abbv'])}
        attack_dict = {i+1:team for i, team in enumerate(team_df['attack'])}
        midfield_dict = {i+1:team for i, team in enumerate(team_df['midfield'])}
        defend_dict = {i+1:team for i, team in enumerate(team_df['defense'])}
                
        for k,v in teams_dict.items():
            print(f"[{k}] {v}")
                    
        input_number_ot = int(input("\nSelect oppositions team or Press 0 to go back: "))
        
        if input_number_ot in teams_dict.keys():
            opposition_team = teams_dict[input_number_ot]
            opposition_stadium = stadium_dict[input_number_ot]
            opposition_team_abbv = abbv_dict[input_number_ot]
            opposition_attack = attack_dict[input_number_ot]
            opposition_midfield = midfield_dict[input_number_ot]
            opposition_defend = defend_dict[input_number_ot]
            number_ot = team_df.loc[team_df['team_name']== opposition_team,'team_id'].values[0]
            print(f"\nYou selected {opposition_team}")
            time.sleep(2)
            break
        
        elif input_number_ot == 0:
            opposition_league_select()
            break
        
        else:
            print("\nError Please input number mentioned on the left of the team you want to choice")
            time.sleep(2)
            
    return None

    
