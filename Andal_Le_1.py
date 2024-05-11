import sys #final code for lab exam 1

game_library = {#fixed
    "Donkey Kong": {"copies_available": 3, "cost": 2},
    "Super Mario Bros": {"copies_available": 5, "cost": 3},
    "Tetris": {"copies_available": 2, "cost": 1}
}

acc_library = {}

def display_available_games(): #fixed
    print("\n===========================================================")
    print("Games Available For Rent:\n")
    for i, game in enumerate(game_library, start=1):
        copies_available = game_library[game]["copies_available"]
        cost = game_library[game]["cost"]
        print(f"{i}. {game} - Copies available: {copies_available} - Rental cost: ${cost}")
    print("===========================================================")
    
def register_user(): #fixed
    while True:
        try:
            print("\n===========================================================")
            print("Account Registration\n")
            print("Please enter your information below\n")
            username = str(input("Please enter your selected username: "))
            password = str(input("Please enter your password (should be at least 8 characters long): "))

            while len(password) < 8:
                print("\n===========================================================")
                print("       Password must be at least 8 characters long.")
                print("===========================================================\n")
                password = input("Enter your password again (must be 8 characters long): ")

            if username in acc_library:
                print("\n==============================================================")
                print("Username is already taken. Please choose a different username.")
                print("==============================================================")
            else:
                print("\n===========================================================")
                print("      Your account has been registered successfully")
                print("===========================================================")
                
                userbal = 0
                userpoints = 0

                acc_library[username] = {
                    "username": username,
                    "password": password,
                    "Balance": userbal,
                    "Points": userpoints
                }
                main()  
                break

        except ValueError:
            print("\nInvalid Username or Password\n")
            input()
            return

def login_user(): #fixed
    while True:
            print("\n===========================================================")
            print("Sign-in Portal\n")
            username = str(input("Username: "))
            password = str(input("Password: "))
            if username in acc_library and acc_library[username]["password"] == password:
                print("\n===========================================================")
                print("                    Sign-in Successful")
                print("===========================================================")
                user_menu(username)
            else:
                print("\n===========================================================")
                print("         Account not found. Please register first!")
                print("===========================================================")
                break
        
def admin_login():
    while True:
        try:
            print("\n===========================================================")
            print("Admin Log-in Page\n")
            admin_username = str(input("Username: "))
            admin_password = str(input("Password: "))

            if admin_username == "admin" and admin_password == "adminpass":
                print("\n===========================================================")
                print("                    Log-in Successful")
                print("===========================================================")
                admin_menu()
                break 
            else:
                print("\n===========================================================")
                print("              Incorrect username or password")
                print("===========================================================")
                break
        except ValueError:
            print("\nWrong input")
            break
        
def user_menu(username): #fixed
    while True:
        try:
            print(f"\nLogged in as {username} ---- Balance: ${acc_library[username]['Balance']}\n")
            print("1. Rent a game")
            print("2. Return a game")
            print("3. Top-up Account")
            print("4. Display inventory")
            print("5. Redeem free game rental")
            print("6. Check profile")
            print("7. Log out")

            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                rent_selected_game(username)
            elif choice == 2:
                return_rented_game(username)
            elif choice == 3:
                top_up_account(username)
            elif choice == 4:
                display_inventory(username)
            elif choice == 5:
                redeem_free_rental(username)
            elif choice == 6:
                check_credentials(username)
            elif choice == 7:
                print("\n===========================================================")
                print("                     LOGGING OUT!")
                print("===========================================================")
                main()
                
            else:
                print("\n===========================================================")
                print("                Please select a valid option")
                print("===========================================================")
                break
        except ValueError:
            print("\n===========================================================")
            print("                      Wrong input")
            print("===========================================================")
            return

def admin_menu(): #fixed
    while True:
            print("\n===========================================================")
            print("Administrative Menu\n") 
            print("1. Manage Game Details")
            print("2. Log out")
            
            choice = input("\nEnter your choice: ")
            
            if choice == "1":
                admin_game_menu()
            elif choice == "2":
                print("\n===========================================================")
                print("                      Logging out...")
                print("===========================================================")
                main()
                break
            else:
                print("\n===========================================================")
                print("               Please select a valid option")
                print("===========================================================")
                admin_menu()
                return
        
def top_up_account(username): #fixed
    try:
        print("\n===========================================================")
        print("Top-up Account\n")
        amount = input("Enter the amount, or leave blank if you want to cancel: ")

        if amount == "" or amount == " ":
            print("\n===========================================================")
            print("                 Transcation Cancelled")
            print("===========================================================")
        else:
            amount = float(amount)
            if amount > 0:
                acc_library[username]["Balance"] += amount
                print("\n===========================================================")
                print(f"           Top-up successful. New balance: ${acc_library[username]['Balance']}")
                print("===========================================================")
            else:
                print("\n===========================================================")
                print("     Invalid amount. Please enter a positive value.")
                print("===========================================================")
                top_up_account(username)
                return
    except ValueError:
        print("\n===========================================================")
        print("      Invalid input. Please enter a valid amount.")
        print("===========================================================")
        top_up_account(username)
        return

def display_inventory(username): #fixed
    print("\n===========================================================")
    print(f"Inventory for {username}\n")
    if "rented_games" in acc_library[username]:
        for game_name, copies_rented in acc_library[username]["rented_games"].items():
            print(f"{game_name} - Copies rented: {copies_rented}")
    else:
        print("===========================================================")
        print("              No games currently rented!")
        print("===========================================================")

def redeem_free_rental(username): #fixed
    if acc_library[username]["Points"] >= 3:
        display_available_games()
        try:
            game_choice = input("Select the number of the game you want to redeem for free: ")
            if game_choice == "" or game_choice == " ":
                print("\n===========================================================")
                print("                 Transcation Cancelled")
                print("===========================================================")
            else:
                game_choice = int(game_choice)
                for i, game in enumerate(game_library, start=1):
                    if game_choice == i:
                        game_name = game
                        if game_library[game_name]["copies_available"] > 0:
                            acc_library[username]["Points"] -= 3
                            game_library[game_name]["copies_available"] -=1
                            
                            if "rented_games" not in acc_library[username]:
                                acc_library[username]["rented_games"] = {}
                            if game_name in acc_library[username]["rented_games"]:
                                acc_library[username]["rented_games"][game_name] += 1
                            else:
                                acc_library[username]["rented_games"][game_name] = 1
                                print("\n================================================================")
                                print(f"Congratulations for redeeming {game_name} for free. Your remaining points: {acc_library[username]['Points']}")
                                print("================================================================")
                        else:
                            print("\n===========================================================")
                            print("Insufficient copies. Please try redeeming another game.")
                            print("===========================================================")
                            redeem_free_rental(username)
                            return
        except ValueError:
            print("\n===========================================================")
            print("              Please select a valid option")
            print("===========================================================")
            redeem_free_rental(username)
            return
    else:
        print("\n==============================================================")
        print("Insufficient points. You need at least 3 points to rent a game.")
        print("==============================================================")
            
            
def check_credentials(username): #fixed
    user_password = acc_library[username]["password"]
    print("\n===========================================================")
    print(f"Username: {username}")
    print(f"Password: {user_password}")
    print(f"\nPoints for {username}: {acc_library[username]['Points']}")
    print("===========================================================")

def rent_selected_game(username): #fixed
    display_available_games()
    try:
        game_num = input("\nPlease select the number of the game you want to rent: ")
        if game_num == "" or game_num == " ":
                print("\n===========================================================")
                print("                 Transcation Cancelled")
                print("===========================================================")
        else:
            game_num = int(game_num)
            for i, game in enumerate(game_library, start=1):
                if game_num == i:
                    game_name = game     
                    if game_library[game_name]["copies_available"] > 0:
                        cost = game_library[game_name]["cost"]
                        if acc_library[username]["Balance"] >= cost:
                            print("\n===========================================================")
                            print(f"{game_name} rented successfully.")
                            game_library[game_name]["copies_available"] -= 1
                            acc_library[username]["Balance"] -= cost
                            if "rented_games" not in acc_library[username]:
                                acc_library[username]["rented_games"] = {}
                            if game_name in acc_library[username]["rented_games"]:
                                acc_library[username]["rented_games"][game_name] += 1
                            else:
                                acc_library[username]["rented_games"][game_name] = 1
                            print(f"\nYour balance after renting {game_name}: ${acc_library[username]['Balance']}")
                            print("===========================================================")
                            return
                        else:
                            print("\n===========================================================")
                            print("      You don't have enough balance to rent the game.")
                            print("===========================================================")
                            return
                    else:
                        print("\n===========================================================")
                        print("    Insufficient copies. Please try renting another game.")
                        print("===========================================================")
                        rent_selected_game(username)
                        return   
                else:
                    print("\n===========================================================")
                    print("  Please enter a valid option from the game library.")
                    print("===========================================================")
                    rent_selected_game(username)
                    return
    except ValueError:
        print("\n===========================================================")
        print("          Invalid input. Canceling transaction.")
        print("===========================================================")
        user_menu(username)
        return
def return_rented_game(username):
    display_available_games()
    while True:
        if "rented_games" in acc_library[username]: 
            try:
                game_num = input("\nPlease select the number of the game that you want to return: ")
                if game_num == "" or game_num == " ":
                    print("\n===========================================================")
                    print("                 Transcation Cancelled")
                    print("===========================================================")
                else:
                    game_num = int(game_num)
                    for i, game in enumerate(game_library, start=1):
                        if game_num == i:
                            game_name = game
                            if game_name in acc_library[username]["rented_games"]:
                                game_library[game_name]["copies_available"] += 1
                                acc_library[username]["rented_games"][game_name] -= 1
                                
                                print("\n===========================================================")
                                print(f"{game_name} returned successfully. You earned 1 point.")
                                print("===========================================================")
                                    
                                if acc_library[username]["rented_games"][game_name] == 0:
                                    del acc_library[username]["rented_games"]
                                acc_library[username]["Points"] += 1
                                return
                            else:
                                print("\n===========================================================")
                                print("      Invalid game choice. You didn't rent this game.")
                                print("===========================================================")
                                return_rented_game(username)
                                 
                    else:
                        print("\n===========================================================")
                        print("  Please enter a valid game option from the game library.")
                        print("===========================================================")
                        return_rented_game(username)
                        return
            except ValueError:
                print("\n===========================================================")
                print("     Invalid input. Canceling transaction.")
                print("===========================================================")
                user_menu(username)
                return
        else:
            print("\n===========================================================")
            print("               No games currently rented!")
            print("===========================================================")
        break
                
def admin_game_menu(): #fixed    
    print("\n===========================================================")
    print("Update Game\n")
    print("1. Update Game Copies")
    print("2. Update Game Price")
    print("3. Exit")
            
    try:   
        choice = int(input("\nEnter your choice: "))
                
        if choice == 1:
            display_available_games()
            game_choice = int(input("\nSelect the number of the game to be updated: "))
            for i, game in enumerate(game_library, start=1):
                if game_choice == i:
                    game_name = game
                    if game_name in game_library:
                        updated_copies = int(input(f"Enter the updated copies for {game_name}: "))
                        game_library[game_name]["copies_available"] = updated_copies           
                        print("\n===========================================================")
                        print(f"Updated {game_name}'s copies to {updated_copies}")
                        print("===========================================================")
                        break
                    else:
                        print("\n===========================================================")
                        print("               Invalid input. Exiting....")
                        print("===========================================================")
                        admin_game_menu()
                        return
                            
        elif choice == 2:
            display_available_games()
            game_choice = int(input("\nSelect the number of the game to be updated: "))
            for i, game in enumerate(game_library, start=1):
                if game_choice == i:
                    game_name = game
                    if game_name in game_library:
                        updated_price = int(input(f"Enter the updated price for {game_name}: "))
                        game_library[game_name]["cost"] = updated_price
                        print("\n===========================================================")
                        print(f"Updated {game_name}'s price to {updated_price}")
                        print("===========================================================")
                        break
                    else:
                        print("\n===========================================================")
                        print("               Invalid input. Exiting....")
                        print("===========================================================")
                        admin_game_menu()
                        return
        elif choice == 3:
            print("\n===========================================================")
            print("                      Exiting....")
            print("===========================================================")
            admin_menu()
            return 
        else:
            print("\n===========================================================")
            print("              Please select a valid option.")
            print("===========================================================") 
            admin_game_menu()
            return    
    except ValueError:
        print("\nWrong input")
        admin_game_menu()
        return
            
        
def main(): #fixed
        print("\nWELCOME TO THE GAME RENTAL SYSTEM!\n") 
        print("1. Display Available Games")
        print("2. Register User")
        print("3. Sign-in")
        print("4. Admin Log-in")
        print("5. Exit Program")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_available_games()
        elif choice == "2":
            register_user()
        elif choice == "3":
            login_user()
        elif choice == "4":
            admin_login()
        elif choice == "5":
            print("\n===========================================================")
            print("         Thank you for using our Game Rental System!")
            print("===========================================================\n")
            sys.exit()
        else:
            print("\n===========================================================")
            print("               Please select a valid option")
            print("===========================================================")
main()