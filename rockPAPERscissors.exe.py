import random



bets = [0, 1, 2]
words = ["Rock", "Paper", "Scissors"]

player_score = 0
computer_score = 0

print("Welcome to RPS!")
name = input("Please enter your name: ")
while True:
    try:
        player_bet = input("Type: Rock(0), Paper(1), Scissors(2) or Q to quit: ").lower()
        if player_bet == "q":
            break
        if player_bet not in ["0", "1", "2"]:
            print("please enter the number related to your choice".capitalize())
            continue
    except:
        print("Only single digits please!")
        continue
    # generating random number with range 0 to 2 (computer bet)
    rand_num = random.randint(0,2)
    comp_bet = bets[rand_num]
    if comp_bet == 0:
        computer_bet = words[0]
    elif comp_bet == 1:
        computer_bet = words[1] 
    elif comp_bet == 2:
        computer_bet = words[2]
    if player_bet == "0":
        player_betw = words[0]
    elif player_bet == "1":
        player_betw = words[1] 
    elif player_bet == "2":
        player_betw = words[2]
        
    print(f"Player: {player_betw}")
    print(f"Computer: {computer_bet}")
    comp_bet = str(comp_bet)
    if player_bet == "0" and  comp_bet == "2":
        print("You won!") 
        player_score += 1  
        
    elif player_bet == "1" and comp_bet == "0":
        print("You won!") 
        player_score += 1         
        
    elif player_bet == "2" and comp_bet == "1":
        print("You won!") 
        player_score += 1
    elif player_bet == comp_bet:
        print("It's a tie!")
        
    else:
        computer_score +=1
        print("You lost")
if player_score < computer_score:
    winner = "Machine"
elif player_score == computer_score:
    winner = "None of you"
else:
    winner = name
print(f"Player score: {player_score}, Computer score: {computer_score}. the winner is obviousely {winner}!")
print("See you soon!")
    