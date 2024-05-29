import time
import random
import team_selection
import main

#player_team , player_stadium = team_selection.player_team_select()
#opposition_team , oppostion_stadium = team_selection.opposition_team_select()
extra_time_status = False

def match():
    
    global player_score
    global opposition_score
    global player_team
    global opposition_team
    global player_team_abbv
    global player_attack
    global player_midfield
    global player_defend
    global opposition_team_abbv
    global opposition_attack
    global opposition_midfield
    global opposition_defend
    
    from team_selection import player_team,player_stadium,player_team_abbv,player_attack,player_midfield,player_defend
    from team_selection import opposition_team,opposition_stadium,opposition_team_abbv,opposition_attack,opposition_midfield,opposition_defend
    
    print(f"\nHello Everyone welcome to {player_stadium} for todays match where {player_team} faces up against {opposition_team}")
    start_time = 0
    possesion = random.choice([player_team,opposition_team])
    player_score = 0
    opposition_score = 0
    
    input("\nPress Enter to start")

    ############################## First Half ##############################
    
    print("\nAnd We are under way\n")
    
    while start_time < 45:
        
        mid_dif = (player_midfield - opposition_midfield)/100 

        weight_a = 0.5 + mid_dif
        weight_b = 0.5 - mid_dif
        weights_pc_pot = [weight_a,weight_b]
        weights_pc_ppt = [weight_b,weight_a]
        
        time.sleep(1)
        
        if possesion == player_team:
            possesion_change = random.choices([True,False],weights_pc_ppt,k=1)[0]
        else:
            possesion_change = random.choices([True,False],weights_pc_pot,k=1)[0]
            
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
        
        mid_dif = (player_midfield - opposition_midfield)/100 

        weight_a = 0.5 + mid_dif
        weight_b = 0.5 - mid_dif
        weights_pc_pot = [weight_a,weight_b]
        weights_pc_ppt = [weight_b,weight_a]
        
        time.sleep(1)
        
        if possesion == player_team:
            possesion_change = random.choices([True,False],weights_pc_ppt,k=1)[0]
        else:
            possesion_change = random.choices([True,False],weights_pc_pot,k=1)[0]
            
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
        
        mid_dif = (player_midfield - opposition_midfield)/100 

        weight_a = 0.5 + mid_dif
        weight_b = 0.5 - mid_dif
        weights_pc_pot = [weight_a,weight_b]
        weights_pc_ppt = [weight_b,weight_a]
        
        time.sleep(1)
        
        if possesion == player_team:
            possesion_change = random.choices([True,False],weights_pc_ppt,k=1)[0]
        else:
            possesion_change = random.choices([True,False],weights_pc_pot,k=1)[0]
            
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
        
        mid_dif = (player_midfield - opposition_midfield)/100 

        weight_a = 0.5 + mid_dif
        weight_b = 0.5 - mid_dif
        weights_pc_pot = [weight_a,weight_b]
        weights_pc_ppt = [weight_b,weight_a]
        
        time.sleep(1)
        
        if possesion == player_team:
            possesion_change = random.choices([True,False],weights_pc_ppt,k=1)[0]
        else:
            possesion_change = random.choices([True,False],weights_pc_pot,k=1)[0]
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

def extra_time():
    
    global player_score
    global opposition_score
    
    print(f"\n90 minutes couldn't seperate the teams. So we will go to extra time")
    start_time = 90
    possesion = random.choice([player_team,opposition_team])
    
    input("\nPress Enter to start")

    ############################## First Half ##############################
    
    print("\nAnd We are under way in the first half of Extra time\n")
    
    while start_time < 105:
        
        mid_dif = (player_midfield - opposition_midfield)/100 

        weight_a = 0.5 + mid_dif
        weight_b = 0.5 - mid_dif
        weights_pc_pot = [weight_a,weight_b]
        weights_pc_ppt = [weight_b,weight_a]
        
        time.sleep(1)
        
        if possesion == player_team:
            possesion_change = random.choices([True,False],weights_pc_ppt,k=1)[0]
        else:
            possesion_change = random.choices([True,False],weights_pc_pot,k=1)[0]
            
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
        
        mid_dif = (player_midfield - opposition_midfield)/100 

        weight_a = 0.5 + mid_dif
        weight_b = 0.5 - mid_dif
        weights_pc_pot = [weight_a,weight_b]
        weights_pc_ppt = [weight_b,weight_a]
        
        time.sleep(1)
        
        if possesion == player_team:
            possesion_change = random.choices([True,False],weights_pc_ppt,k=1)[0]
        else:
            possesion_change = random.choices([True,False],weights_pc_pot,k=1)[0]
            
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
        
        mid_dif = (player_midfield - opposition_midfield)/100 

        weight_a = 0.5 + mid_dif
        weight_b = 0.5 - mid_dif
        weights_pc_pot = [weight_a,weight_b]
        weights_pc_ppt = [weight_b,weight_a]
        
        time.sleep(1)
        
        if possesion == player_team:
            possesion_change = random.choices([True,False],weights_pc_ppt,k=1)[0]
        else:
            possesion_change = random.choices([True,False],weights_pc_pot,k=1)[0]
            
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
        
        mid_dif = (player_midfield - opposition_midfield)/100 

        weight_a = 0.5 + mid_dif
        weight_b = 0.5 - mid_dif
        weights_pc_pot = [weight_a,weight_b]
        weights_pc_ppt = [weight_b,weight_a]
        
        time.sleep(1)
        
        if possesion == player_team:
            possesion_change = random.choices([True,False],weights_pc_ppt,k=1)[0]
        else:
            possesion_change = random.choices([True,False],weights_pc_pot,k=1)[0]
            
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

def post_result_selection():
    prs = input("\nOptions\n[1] Restart Match\n[2] Restart Match with new teams\n[3] Quit to Main Menu\nWhat do you choose: ")
    print("\n")
    
    if prs == '1':
        match()
        result()
        post_result_selection()
    elif prs == '2':
        team_selection.player_country_select()
        team_selection.opposition_country_select()
        match()
        result()
        post_result_selection()
    elif prs == '3':
        main.main_menu()
    else:
        print('Error Please select a number input from above\n')
        post_result_selection()
        
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
            team_selection.player_country_select()
            team_selection.opposition_country_select()
            match()
            result()
        elif pds == '5':
            main.main_menu()
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
            team_selection.player_country_select()
            team_selection.opposition_country_select()
            match()
            result()
        elif pds == '4':
            extra_time_status = False
            main.main_menu()
        else:
            print('Error Please select a number input from above\n')
            post_draw_selection()