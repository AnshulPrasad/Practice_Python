"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""


def command(player_no):
    text = input(f"Enter player{player_no}: ").strip().lower()
    while text not in ["rock", "scissors", "paper"]:
        print("Enter a valid input!")
        text = input(f"Enter player{player_no}: ").strip().lower()
    return text


points = [0, 0]
rules = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
for i in range(5):
    print(f"Round {i+1}")
    text1 = command("1")
    text2 = command("2")

    if rules[text1] == text2:
        points[0] += 1
        print("player1 gets 1 point!\n")
    elif rules[text2] == text1:
        points[1] += 1
        print("player2 gets 1 point!\n")
    else:
        print("Tie!\n")

print(f"points of player1: {points[0]}\npoints of player2: {points[1]}")
if points[0] == points[1]:
    print("Tie game!")
elif points[0] > points[1]:
    print("player1 winns!")
else:
    print("player1 winns!")
