# Requirements
# 1. The program must have a comment with assignment and author names.
# 2. The program must have at least one if/then block.
# 3. The program must have at least one while loop.
# 4. The program must have more than one function.
# 5. The program must have a function called main.

'''
Tic-Tac-Toe Assignment
Author: Diego Feresin
'''

def main():
    player = change_player("")
    dashboard = make_dashboard()
    while not (has_winner(dashboard) or is_a_draw(dashboard)):
        show_dashboard(dashboard)
        make_move(player, dashboard)
        player = change_player(player)
    show_dashboard(dashboard)
    print("We have a winner! Thank you all for playing!") 

def make_dashboard():
    dashboard = []
    for square in range(9):
        dashboard.append(square + 1)
    return dashboard

def show_dashboard(dashboard):
    print()
    print(f"{dashboard[0]}|{dashboard[1]}|{dashboard[2]}")
    print('-+-+-')
    print(f"{dashboard[3]}|{dashboard[4]}|{dashboard[5]}")
    print('-+-+-')
    print(f"{dashboard[6]}|{dashboard[7]}|{dashboard[8]}")
    print()
    
def is_a_draw(dashboard):
    for square in range(9):
        if (dashboard[square]) != "X" and dashboard[square] != "O":
            return False
    return True 
    
def has_winner(dashboard):
    return (dashboard[0] == dashboard[1] == dashboard[2] or
            dashboard[3] == dashboard[4] == dashboard[5] or
            dashboard[6] == dashboard[7] == dashboard[8] or
            dashboard[0] == dashboard[3] == dashboard[6] or
            dashboard[1] == dashboard[4] == dashboard[7] or
            dashboard[2] == dashboard[5] == dashboard[8] or
            dashboard[2] == dashboard[4] == dashboard[6])

def make_move(player, dashboard):
    square = int(input(f"{player}'s turn to choose a square (from 1 to 9): "))
    dashboard[square - 1] = player

def change_player(current):
    if current == "" or current == "O":
        return "X"
    elif current == "X":
        return "O"

if __name__ == "__main__":
    main()