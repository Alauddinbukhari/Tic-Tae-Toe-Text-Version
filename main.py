from player import Player
from patterns_positions import winning_positions
from itertools import combinations


# Initialize game array
game_array = [["", "", ""], ["", "", ""], ["", "", ""]]

# Function to display the game layout
def layout():
    for row in game_array:
        print(row)

# Function to fetch positions of a player's choice
def fetch_position(player):
    positions_list = []

    for i, row in enumerate(game_array):
        for j, element in enumerate(row):
            if element == player.choice:
                positions_list.append((i, j))

    layout()
    posi_tuples = to_three_element(positions_list)

    if posi_tuples:
        return check_pattern(posi_tuples)

# Function to check if a pattern exists in a tuple of positions
def check_pattern(tuples):
    if len(tuples) != 3:
        return None

    for tpl in tuples:
        if tpl in patterns:
            return True

# Function to convert a list of positions into three-element tuples
def to_three_element(list_of_positions):
    if len(list_of_positions) == 3:
        return tuple(list_of_positions)
    elif len(list_of_positions) > 3:
        # return all combinations of three elements
        return tuple(combinations(list_of_positions, 3))
def combination():




# Function to take player input for position
def ask_position(player):
    if all(cell != "" for row in game_array for cell in row):
        print("It's a draw!")
        return None

    print(f"{player.name}, it's your turn.")
    layout()



    row = int(input("Enter row number: ")) - 1
    column = int(input("Enter column number: ")) - 1

    if game_array[row][column] == "":
        game_array[row][column] = player.choice
        return fetch_position(player)
    else:
        print("Cell already taken. Try again.")
        return ask_position(player)




# Main game loop
player_1 = Player("Player 1")
player_2 = Player("Player 2")

player_1.choice = input("Player 1, choose between 0 or X: ")

if player_1.choice == "X":
    player_2.choice = "0"
else:
    player_2.choice = "X"
    print(f"Player 2, your weapon is {player_2.choice}")

game_over = False

while not game_over:
    player_1_result = ask_position(player_1)

    if player_1_result:
        game_over = True
        print(f"{player_1.name} is the winner!")
    else:
        player_2_result = ask_position(player_2)

        if player_2_result:
            game_over = True
            print(f"{player_2.name} is the winner!")
