import time
import random
import pandas as pd

leagues_data = pd.read_csv('Leagues.csv')
teams_data = pd.read_csv('Teams.csv')

leagues_dict = leagues_data.set_index('league_id')['league_name'].to_dict()

def match():
    
    global player_score
    global opposition_score
    
    #player_team = "Chelsea"
    #opposition_team = "Arsenal"
    
    print(f"\nHello Everyone welcome to {player_stadium} for todays match where {player_team} faces up against {opposition_team}")
    start_time = 0
    possesion = random.choice([player_team,opposition_team])
    player_score = 0
    opposition_score = 0
    
    input("\nPress Enter to start")

    ############################## First Half ##############################
    
    print("\nAnd We are under way")
    
    while start_time < 45:
        
        time.sleep(1)
        possesion_change = random.choice([True,False])
        goal_status = random.choices([True,False],weights=(5,95))
            
            
        start_time = start_time + 1
        print(f"{start_time}'")
        
        if possesion_change == True:
            if possesion == player_team:
                possesion = opposition_team
                
            else:
                possesion = player_team
                
        else:
            pass
            
        if goal_status[0] == True:
            if possesion == player_team:
                player_score = player_score + 1
                
            else:
                opposition_score = opposition_score +1
                
        else:
            pass
        
        print(f"{player_team} : {player_score}")
        print(f"{opposition_team} : {opposition_score}")
        
        if possesion_change == True:
            print(f"{possesion} wins the ball")
            
        else:
            pass
        
        if goal_status[0] == True:
            print(f"{possesion} scores !!!!!!!!!!!!")
            time.sleep(4)
            
        else:
            pass
        
        print('\n')

    print("\nEnd of first Half")
    input("\nPress enter to start the second half")

    ######################################## Second Half ########################################

    print("\nAnd We are under way")
    
    while start_time < 90:
        
        time.sleep(1)
        possesion_change = random.choice([True,False])
        goal_status = random.choices([True,False],weights=(5,95))
            
            
        start_time = start_time + 1
        print(f"{start_time}'")
        
        if possesion_change == True:
            if possesion == player_team:
                possesion = opposition_team
            else:
                possesion = player_team
        else:
            pass
            
        if goal_status[0] == True:
            if possesion == player_team:
                player_score = player_score + 1
            else:
                opposition_score = opposition_score +1
        else:
            pass
        
        print(f"{player_team} : {player_score}")
        print(f"{opposition_team} : {opposition_score}")
        
        if possesion_change == True:
            print(f"{possesion} wins the ball")
        else:
            pass
        if goal_status[0] == True:
            print(f"{possesion} scores !!!!!!!!!!!!")
            time.sleep(4)
        else:
            pass
        print('\n')
        
    print ("\nThats the final Whistle")
 
    
def result():
    
    if player_score == opposition_score:
        print("The Match is a Draw")
    elif player_score > opposition_score:
        print(f"{player_team} won the match")
    else:
        print(f"{opposition_team} won the match")
    

def opposition_team_select():
    
    global opposition_team
    global opposition_stadium
    
    print('\n') 
    
    for k,v in leagues_dict.items():
        print(f"[{k}] {v}")
    
    number_ol = int(input("Choose your League: "))
    
    if number_ol in leagues_dict:
         
        try:
            team_df = teams_data[teams_data['league_id'] == number_ol]
            
            teams_dict = {i+1:team for i, team in enumerate(team_df['team_name'])}
            stadium_dict = {i+1:team for i, team in enumerate(team_df['team_stadium'])}
            for k,v in teams_dict.items():
                print(f"[{k}] {v}")
                
            number_ot = int(input("\nSelect your team: "))
        
            if number_ot in teams_dict.keys():
                opposition_team = teams_dict[number_ot]
                opposition_stadium = stadium_dict[number_ot]
                print(f"\nYou selected {opposition_team}")
                time.sleep(2)
            else:
                print("\nError Please input number mentioned on the left of the team you want to choice")
                time.sleep(2)
                opposition_team_select()   
                
        except ValueError:
            print("\nPlease enter a valid number for the league")
            opposition_team_select()
    
    else:
        print("\nError please input a valid league id ")
        opposition_team_select()   
    

def player_team_select():
    
    global player_team
    global player_stadium
    
    print("\n")
    
    for k,v in leagues_dict.items():
        print(f"[{k}] {v}")
    
    number_pl = int(input("Choose your League: "))
    
    if number_pl in leagues_dict:
         
        try:
            team_df = teams_data[teams_data['league_id'] == number_pl]
            
            teams_dict = {i+1:team for i, team in enumerate(team_df['team_name'])}
            stadium_dict = {i+1:team for i, team in enumerate(team_df['team_stadium'])}
            
            for k,v in teams_dict.items():
                print(f"[{k}] {v}")
                
            number_pt = int(input("\nSelect your team: "))
        
            if number_pt in teams_dict.keys():
                player_team = teams_dict[number_pt]
                player_stadium = stadium_dict[number_pt]
                print(f"\nYou selected {player_team}")
                time.sleep(2)
            else:
                print("\nError Please input number mentioned on the left of the team you want to choice")
                time.sleep(2)
                player_team_select()   
                
        except ValueError:
            print("\nPlease enter a valid number for the league")
            player_team_select()
    
    else:
        print("\nError please input a valid league id ")
        player_team_select()    
        
        
def post_result_selection():
    prs = input("\nOptions\n[1] Restart Match\n[2] Restart Match with new teams\n[3] Quit to Main Menu\nWhat do you choose: ")
    print("\n")
    
    if prs == '1':
        match()
        result()
        post_result_selection()
    elif prs == '2':
        player_team_select()
        opposition_team_select()
        match()
        result()
        post_result_selection()
    elif prs == '3':
        main_menu()
    else:
        print('Error Please select a number input from above\n')
        post_result_selection()
    
    
def main():
    player_team_select()
    opposition_team_select()
    match()  
    result()
    post_result_selection()
  
    
def main_menu():
    
    print("Welcome to Soccer World\n[1] Start Game\n[2] Quit Game")

    input_mm = input()
    if input_mm == '1':
        main()
    elif input_mm == '2':
        quit()
    else:
        print("Error Please input number of your option\n")
    
        
if __name__ == "__main__":
    main_menu()
