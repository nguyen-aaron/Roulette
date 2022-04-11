import random, time

def game():
  print("Let's play roluette. You start with $100. Try to see how much money you can make!")
  red_numbers = [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]
  black_numbers = [15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26]
  green_numbers = [0]
  account_funds = 100
  is_running = True
  while (is_running):
    if (account_funds > 0):
      roll = random.randint(0, 36)
      print("You have", account_funds,"dollars in your account.")
      bet = input("What would you like to bet on? (Numbers: 0-36, Colors: Black, Red, Green)")
      wager = int(input("How much would you like to wager?"))
      number_payout = int(wager)*37
      green_payout = int(wager)*37
      redblack_payout = int(wager)*2
      
      if (bet.isdigit() and int(wager) <= int(account_funds) and int(wager) > 0):
        if (int(bet) <= 36):
          print("You are betting on", bet+". Good Luck!")
          time.sleep(2)
          if (int(bet) == int(roll)):
            print("Congrats! You just hit the jackpot! Paying out", number_payout, "dollars.")
            account_funds = account_funds + number_payout - int(wager)
          else:
            account_funds = int(account_funds) - int(wager)
            print("Sorry. You just lost", wager, "dollars. You have", account_funds, "dollars remaining.")
            print("The number was",str(roll)+".")
        else:
          print("Invalid number. Choose a number between 0-36")

      elif (bet.isalpha() and int(wager) <= int(account_funds)):
        if (bet.upper() == "BLACK"):
          print("You are betting on black. Good Luck!")
          time.sleep(2)
          if (int(roll) in black_numbers):
            print("Congrats! You just hit! Paying out", redblack_payout, "dollars.")
            account_funds = account_funds + redblack_payout - int(wager)
          else:
            account_funds = int(account_funds) - int(wager)      
            print("Sorry. You just lost", wager, "dollars. You have", account_funds, "dollars remaining.")
            if (int(roll) in red_numbers):
              print("The color was red.")
            else:
              print("The color was green")
        elif (bet.upper() == "RED"):
          print("You are betting on red. Good Luck!")
          time.sleep(2)
          if (int(roll) in red_numbers):
            print("Congrats! You just hit! Paying out", redblack_payout, "dollars.")
            account_funds = account_funds + redblack_payout - int(wager)
          else:
            account_funds = int(account_funds) - int(wager)
            print("Sorry. You just lost", wager, "dollars. You have", account_funds, "dollars remaining.")
            if (int(roll) in black_numbers):
              print("The color was black.")
            else:
              print("The color was green")
        elif (bet.upper() == "GREEN"):
          print("You are betting on green. Good Luck!")
          time.sleep(2)
          if (int(roll) in green_numbers):
            print("Congrats! You just hit the jackpot! Paying out", green_payout, "dollars.")
            account_funds = account_funds + green_payout - int(wager)
          else:
            account_funds = int(account_funds) - int(wager)
            print("Sorry. You just lost", wager, "dollars. You have", account_funds, "dollars remaining.")
          if (int(roll) in black_numbers):
            print("The color was black.")
          else:
            print("The color was red.")
        else:
          print("Invalid color.") 
  
      elif (int(wager) > int(account_funds)):
        print("Insufficient funds.")
    else:
      print("Game Over. No more funds.")
      is_running = False

def main():
  game()
  while input("Would you like to play again? (Y/N)").upper() == "Y":
    game()

if (__name__ == "__main__"):
  main()
  
      
    

