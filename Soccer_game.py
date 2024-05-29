import time
import random
import pandas as pd

country_data = pd.read_csv('data/Country.csv')
leagues_data = pd.read_csv('data/Leagues.csv')
teams_data = pd.read_csv('data/Teams.csv')
managers_data = pd.read_csv('data/Managers.csv')

country_dict = country_data.set_index('country_id')['country_name'].to_dict()
extra_time_status = False

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
    
    print("\nAnd We are under way\n")
    
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
        
        print(f"{player_team_abbv} : {player_score}")
        print(f"{opposition_team_abbv} : {opposition_score}")
        
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
    
    first_half_added_time = random.randrange(1,11)
    print(f"{first_half_added_time}' of added time\n")
    
    while start_time < 45 + first_half_added_time:
        
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
        
        print(f"{player_team_abbv} : {player_score}")
        print(f"{opposition_team_abbv} : {opposition_score}")
        
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
        
    start_time = 45        

    print("\nEnd of first Half")
    input("\nPress enter to start the second half")

    ######################################## Second Half ########################################

    print("\nAnd We are under way in the second half\n")
    
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
        
        print(f"{player_team_abbv} : {player_score}")
        print(f"{opposition_team_abbv} : {opposition_score}")
        
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
        
    second_half_added_time = random.randrange(1,11)
    print(f"{second_half_added_time}' of added time\n")
    
    while start_time < 90 + second_half_added_time:
        
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
        
        print(f"{player_team_abbv} : {player_score}")
        print(f"{opposition_team_abbv} : {opposition_score}")
        
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
    
    start_time = 90    
    print ("\nThats the final Whistle")
 
    
def result():
    
    if player_score == opposition_score:
        print("The Match is a Draw")
        post_draw_selection()
    elif player_score > opposition_score:
        print(f"{player_team} won the match")
        post_result_selection()
    else:
        print(f"{opposition_team} won the match")
        post_result_selection()
    

def extra_time():
    
    global player_score
    global opposition_score
    
    #player_team = "Chelsea"
    #opposition_team = "Arsenal"
    
    print(f"\n90 minutes couldn't seperate the teams. So we will go to extra time")
    start_time = 90
    possesion = random.choice([player_team,opposition_team])
    
    input("\nPress Enter to start")

    ############################## First Half ##############################
    
    print("\nAnd We are under way in the first half of Extra time\n")
    
    while start_time < 105:
        
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
        
        print(f"{player_team_abbv} : {player_score}")
        print(f"{opposition_team_abbv} : {opposition_score}")
        
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
    
    first_half_extra_time = random.randrange(1,6)
    print(f"{first_half_extra_time}' of added time\n")
    
    while start_time < 105 + first_half_extra_time:
        
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
        
        print(f"{player_team_abbv} : {player_score}")
        print(f"{opposition_team_abbv} : {opposition_score}")
        
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
        
    start_time = 105        

    print("\nEnd of first half of extra time")
    input("\nPress enter to start the second half")

    ######################################## Second Half ########################################

    print("\nAnd We are under way in the second half of extra time\n")
    
    while start_time < 120:
        
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
        
        print(f"{player_team_abbv} : {player_score}")
        print(f"{opposition_team_abbv} : {opposition_score}")
        
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
        
    second_half_extra_time = random.randrange(1,11)
    print(f"{second_half_extra_time}' of added time\n")
    
    while start_time < 120 + second_half_extra_time:
        
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
        
        print(f"{player_team_abbv} : {player_score}")
        print(f"{opposition_team_abbv} : {opposition_score}")
        
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
    
    start_time = 120    
    print ("\nThats the final Whistle")
    

def take_penalty():
    # Simulate a penalty shot with a 70% chance of scoring
    return random.random() < 0.7


def penalties(team1,team2):
    
    global palyer_score
    global opposition_score
    
    player_score = 0
    opposition_score = 0
    rounds = 5
    results = {"team1": [], "team2": []}

    for round in range(1, rounds + 1):
        # Team 1 takes a penalty
        if take_penalty():
            player_score += 1
            results["team1"].append("Goal")
        else:
            results["team1"].append("Miss")
        
        # Team 2 takes a penalty
        if take_penalty():
            opposition_score += 1
            results["team2"].append("Goal")
        else:
            results["team2"].append("Miss")
        
        print(f"Round {round} - {team1}: {results['team1'][-1]}, {team2}: {results['team2'][-1]}")
        print(f"Score after round {round}: {team1} {player_score} - {opposition_score} {team2}")
        time.sleep(2)
        
        # Check if one team has already won after 5 rounds
        if round == rounds:
            if player_score > opposition_score:
                result()
            elif opposition_score > player_score:
                result()

    # If tied after 5 rounds, go into sudden death
    print("Tied after 5 rounds. Sudden death!")
    while player_score == opposition_score:
        # Team 1 takes a sudden death penalty
        if take_penalty():
            player_score += 1
            results["team1"].append("Goal")
        else:
            results["team1"].append("Miss")
        
        # Team 2 takes a sudden death penalty
        if take_penalty():
            opposition_score += 1
            results["team2"].append("Goal")
        else:
            results["team2"].append("Miss")

        print(f"Sudden Death - {team1}: {results['team1'][-1]}, {team2}: {results['team2'][-1]}")
        print(f"Score: {team1} {player_score} - {opposition_score} {team2}")


def post_draw_selection():
    
    global extra_time_status
    
    if extra_time_status == False:
    
        pds = input("\nOptions\n[1] Extra Time\n[2] Penalties\n[3] Restart Match\n[4] Restart Match with new teams\n[5] Quit to Main Menu\nWhat do you choose: ")
        print("\n")
        
        if pds == '1':
            extra_time_status = True
            extra_time()
            result()
        elif pds == '2':
            penalties(player_team,opposition_team)
            result()
        elif pds == '3':
            match()
            result()
        elif pds == '4':
            player_country_select()
            opposition_country_select()
            match()
            result()
        elif pds == '5':
            main_menu()
        else:
            print('Error Please select a number input from above\n')
            post_draw_selection()
            
    else:
        
        pds = input("\nOptions\n[1] Penalties\n[2] Restart Match\n[3] Restart Match with new teams\n[4] Quit to Main Menu\nWhat do you choose: ")
        print("\n")
        
        if pds == '1':
            extra_time_status = False
            penalties(player_team,opposition_team)
            result()
        elif pds == '2':
            extra_time_status = False
            match()
            result()
        elif pds == '3':
            extra_time_status = False
            player_country_select()
            opposition_country_select()
            match()
            result()
        elif pds == '4':
            extra_time_status = False
            main_menu()
        else:
            print('Error Please select a number input from above\n')
            post_draw_selection()


def post_result_selection():
    prs = input("\nOptions\n[1] Restart Match\n[2] Restart Match with new teams\n[3] Quit to Main Menu\nWhat do you choose: ")
    print("\n")
    
    if prs == '1':
        match()
        result()
        post_result_selection()
    elif prs == '2':
        player_country_select()
        opposition_country_select()
        match()
        result()
        post_result_selection()
    elif prs == '3':
        main_menu()
    else:
        print('Error Please select a number input from above\n')
        post_result_selection()
          

def player_team_select():
    
    global player_team
    global player_stadium
    global player_team_abbv
    global player_attack
    global player_midfield
    global player_defend
    global number_pt
    
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


def opposition_team_select():
    
    global opposition_team
    global opposition_stadium
    global opposition_team_abbv
    global opposition_attack
    global opposition_midfield
    global opposition_defend
    global number_ot
    
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
    
    
def player_league_select():
    
    global number_pl
    
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


def player_country_select():
    
    global number_pc
    
    print("\n#### Country Options ####")
    
    for k,v in country_dict.items():
        print(f"[{k}] {v}")
    
    number_pc = int(input("Choose your League or Press 0 to go back: "))
    
    if number_pc in country_dict:
        player_league_select()
    
    elif number_pc == 0:
        main_menu()    
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
        player_team_select()    
    else:
        print("\nError please input a valid league id ")
        opposition_country_select() 


def main():
    player_country_select()
    opposition_country_select()
    match()  
    result()
  
    
def main_menu():
    
    print("\nWelcome to Soccer World\n\n[1] Start Game\n[2] Quit Game")

    input_mm = input()
    if input_mm == '1':
        main()
    elif input_mm == '2':
        quit()
    else:
        print("Error Please input number of your option\n")
    
        
if __name__ == "__main__":
    main_menu()
