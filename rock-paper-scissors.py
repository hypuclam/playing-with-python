import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player} computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smaches scissors! You win!"
    else:
      return "Paper covers rock! You lost."
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock! You win!"
    else:
      return "Scissors cut paper! You lost."
  elif player == "scissors":
    if computer == "paper":
      return "Paper covers rock! You lost."
    else:
      return "Rock brakes scissors. You lost."
  
  return [player, computer]

choices = get_choices()
p_choice = choices["player"]
c_choice = choices["computer"]
result = check_win(p_choice, c_choice)
print(result)
