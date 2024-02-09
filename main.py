from player import  Player
from patterns_positions import patterns
#import a dictionary which have speicific postions that can help us determine a winner
def fetch_position(player):
    positions_list=[]
    for i, row in enumerate(game_array):
        for j, element in enumerate(row):
            if element == player.choice:
                positions_list.append([i,j]) #Todo : check if it is returning a tuple or not?
    layout()
    posi_tuples = to_three_element(positions_list)
    if posi_tuples :
        return check_pattern(posi_tuples)
    #if pattern found then  it is true else go for another player


#issue is that i der can be many elements
#after getting positions i must shuffle them in three different components so that i can use it with "if in "



def check_pattern(tuples):
    if len(tuples) != 3:
        return None
    for _ in tuples:
        if tuples in  patterns:
            return True


# if pattern in tuple
#return true



def to_three_element(list_of_positions):


    if len(list_of_positions)==3:
        new_tuple=(element for element in list_of_positions)
        #((1,2),(2,3),(4,5)) c
    elif len(list_of_positions)>3:
        #give me all combination

    return None


    #this algo should be able to shuffle if der are more then 3 elements and give all combinations


#return a multidimentional tuple



def layout():
    for row in game_array:
        print(row)


def ask_position(player):
    print(f"{player.name} your turn. ")
    layout()
    if "X" not in game_array and 0 not in game_array:

        print("given the above gamelayout, give me the positions in row and column,")
        print("starting from one each.")


#add a functionality that can check if a element is alreADY present at given positon

    row=int(input("Give me row number"))-1
    column= int(input("Give me column number"))-1
    game_array[row][column]=player.choice
    return fetch_position(player)







# def turn_list_to_diagram:
#     pass






#Main
game_array=[["","",""],
            ["","",""],
            ["","",""]]

player_1=Player("player 1")
player_2=Player("player 2")


player_1.choice=input("Player 1,choose between 0 or X\n")
if player_1.choice =="X":
    player_2.choice=0

else:

    player_2.choice="X"
    print(f"Player 2 your weapon is {player_2.choice}" )

gameover=False
player2_result=""
while not gameover:
    if "" not in game_array:
        gameover=True
        print("Draw")
    player1_result=ask_position(player_1)

    if player1_result:
        gameover=True
        print("Winner is ")
    else:
        player2_result=ask_position(player_2)
        if player2_result:
            gameover=True
            print("Winner is player 2")



