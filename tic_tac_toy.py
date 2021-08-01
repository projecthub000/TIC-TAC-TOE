# Demo of tic tac toe board
def board(a):
    print("",a[1]," │",a[2]," │ ",a[3]," ")
    print("────┼────┼────")
    print("",a[4]," │",a[5]," │ ",a[6]," ")
    print("────┼────┼────")
    print("",a[7]," │",a[8]," │ ",a[9]," ")

def instrunction():
    board(pos)
    print("WELCOME TO TIC TAC TOE")
    players[0]=input("Enter your name player 1:")
    players[1]=input("Enter your name player 2:")
    print("->",players[0],"your sign is x")
    print("->",players[1],"your sign is 0")
    print("-> Potisions are like :-")
    print("  1 │  2 │ 3  ")
    print("────┼────┼────")
    print("  4 │ 5  │ 6  ")
    print("────┼────┼────")
    print("  7 │ 8  │ 9  ")
    yes=input("You guys really wants to play this game? say (yes/no):")
    return yes
def start_game():
        turn=0
        for i in range(9):
         try:
            if turn%2==0:
                print("This is Your Turn",players[0])
                p=int(input("Please Enter position:"))
                if p>=10 or p<=0:
                    print("Please enter right position")
                    continue
                if p not in check:
                 check.append(p)
                 value="x"
                 pos[p]=value
                 board(pos)
                 winner=checkwin(value)
                 if winner=="noone":
                    turn=1
                    
                 else:
                    print("HURRAY! YOU WON",players[0])
                    break
                else:
                    print("Please enter valid position,the position yo typed is already used lol!".upper())
                    continue
            else:
                 print("This is Your Turn",players[1])
                 p=int(input("Please Enter Position:"))
                 if p>=10 or p<=0:
                    print("Please enter right position")
                    continue
                 if p not in check:
                  check.append(p)
                  value="0"
                  pos[p]=value
                  board(pos)
                  winner=checkwin(value)
                  if winner=="noone":
                    turn=0
                  else:
                    print("HURRAY! YOU WON",players[1])
                    break
                 else:
                    print("Please enter valid position,the position you typed is already used lol!".upper())
                    continue
         except:
            print("please enter valid position")
        else:
          print("Game is tie","You guys are heavy driver")

def checkwin(value):
    for i in winning_combination:
        if (pos[i[0]],pos[i[1]],pos[i[2]])==(value,value,value):
         winner=players[0]
         break
        elif (pos[i[0]],pos[i[1]],pos[i[2]])==(value,value,value):
         winner=players[1]
         break
        else:
         winner="noone"
    return winner

winning_combination=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,8),(1,5,9),(3,5,7)]
pos=['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
check=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
players=["",""]
ins=instrunction()
flag=True
while flag:
 if ins.lower()=="yes":
    start_game()
    x=input("You guys wants to play again?")
    if x.lower()=="yes":
        start_game()
    else:
        print("OK bye-bye")
        break
 elif ins.lower()!= ("yes" or "YES") or ("no","NO"):
     print("please say clearly it's your typing mistake")
     x=input("You guys wants to play again?")
     if x.lower()=="yes": 
      start_game()
 else:
    print("Ohk Ta-ta By By")
    break
