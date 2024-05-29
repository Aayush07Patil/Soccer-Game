import team_selection
import match

def main_menu():
    
    print("\nWelcome to Soccer World\n\n[1] Start Game\n[2] Quit Game")

    input_mm = input()
    if input_mm == '1':
        main()
    elif input_mm == '2':
        quit()
    else:
        print("Error Please input number of your option\n")

def main():
    team_selection.player_country_select()
    team_selection.opposition_country_select()
    match.match()  
    match.result()

if __name__ == "__main__":
    main_menu()