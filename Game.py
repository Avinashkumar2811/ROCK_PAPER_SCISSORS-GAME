import random

print(".......😀ROCK PAPER SCISSOR😀.......")
print()
print("*****💟WELCOME TO THIS GAME💟*****")

print("----------------------------------------")
option = ["Rock👊", "Paper✋", "Scissor✌️"]

print("----------------------------------------")

#rules for winners
print(""" The Winning Rules of this game are:
Rock👊 vs Paper✋ --> Paper wins✋
Rock👊 vs Scissor✌️ --> Rock wins 👊
Paper✋ vs Scissors✌️ --> Scissor wins✌️""")
print("----------------------------------------")
print("----------------------------------------")

print("*****GET READY TO PLAY*****")
print()
#bta rhe hain options ko
print("""Choose any one option to play:
1-Rock👊
2-Paper✋
3-Scissor✌️
""")

#main code
u_s = 0
c_s = 0
tie=0
playagain = "Yes"
while playagain == "Yes" or playagain == "yes":
  options = {1: "Rock👊", 2: "Paper✋", 3: "Scissor✌️"}

  #USER KA CHOICE LO SHI GALAT DONO KA CODE
  user_ch = int(input("Enter your choice among 1, 2 and 3: "))
  print("----------------------------------------")
  

  wrong_input = True  #means galat choose kiya toh pehle shi krwao then aage jao
  while wrong_input:  #jab galat choose kra
    if user_ch < 0 or user_ch > 3:
      print("Invalid option please choose among 1,2 and 3 only")
      user_ch = int(input("Enter your choice among 1, 2 and 3: "))
    else:  #shi kiya choose toh aage bdh jayenge
      print("Your choice is", options[user_ch])
      wrong_input = False  #jab shi choose kr liya

  print()

  #COMPUTER KA CHOICE LO
  comp_ch = random.randint(1, 3)
  print("The choice of computer is", options[comp_ch])

  print()
  #MAIN LOGIC FOR WINNING
  if user_ch == comp_ch:
    print("IT'S A DRAW/TIE 👔👔")
    u_s=u_s+0
    c_s=c_s+0
    tie=tie+1
    
  elif ((user_ch == 1 and comp_ch == 2) or (user_ch == 2 and comp_ch == 3)
        or (user_ch == 3 and comp_ch == 1)):
    print("Huhh😰😰The WINNER IS YOUR COMPUTER 🖥️👑")
    c_s = c_s + 1
  else:
    print("CONGRATS USER 🕺🕺, YOU WON THIS GAME🫅🫅")
    u_s = u_s + 1
  print()

  print("-----------------------------------------")

  #agar nhi khelna chahta toh use thanks bol do
  print("----😀😀GAME ENDS HAPPY PLAYING😀😀----")

  print("-----------------------------------------")
  #WANT TO PLAY AGAIN AND AGAIN
  playagain = input("""---> IF YOU WANT TO PLAY THIS GAME AGAIN, Type Yes/yes , Else Type No Stop this game.
=> """)

if playagain == "No" or "no":
  if u_s == c_s:
    print("User_score is",u_s)
    print("computer_score is",c_s)
    print("Tie score is",tie)
    print("****OVERALL Its a TIE****")
    
  elif u_s > c_s:
    print("User_score is",u_s)
    print("computer_score is",c_s)
    print("Tie score is",tie)
    print("OVERALL the USER wins 🕺🕺")
    
  elif u_s < c_s:
    print("User_score is",u_s)
    print("computer_score is",c_s)
    print("Tie score is",tie)
    print("Finally COMPUTER wins 🖥️👑")
