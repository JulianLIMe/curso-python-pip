import random

def choose_options():
    options = ('piedra', 'papel', 'tijera') # Tupla
    user_option = input('Piedra, papel o tijera => ')
    user_option = user_option.lower() # Lower to input user

    if not user_option in options:
        print("Invalid option")
        return None, None # Erro case: values to user_option and computer_option 
    
    computer_option = random.choice(options) # Choising a random option

    print('User option => ', user_option)
    print('Computer option => ', computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option):
    if user_option == computer_option:
        print('Tie')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('User is the winer')
        else:
            print('Computer is the winer')
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('User is the winer')
        else:
            print('Computer is the winer')
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('User is the winer')
        else:
            print('Computer is the winer')
    return None

def run_game():
    user_option, computer_option = choose_options()
    if not user_option == None and not computer_option == None:
        check_rules(user_option, computer_option)
    else:
        print('Nobody won')
    return None

run_game()
