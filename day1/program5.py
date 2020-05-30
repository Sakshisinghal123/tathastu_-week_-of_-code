run_player1=int(input("enter the run scored by player 1 in 60 ball:"))
run_player2=int(input("enter the run scored by player 2 in 60 ball:"))
run_player3=int(input("enter the run scored by player 3 in 60 ball:"))
strike rate1 = run_player1*100/60
strike rate2 = run_player2*100/60
strike rate3 = run_player3*100/60
print("strike rate of player 1 is ", strike rate1)
print("strike rate of player 2 is ", strike rate2)
print("strike rate of palyer 3 is ", strike rate3)
print("runs scored by player 1 if they played 60 more ball is ", run_player1*2)
print("runs scored by player 2 if they played 60 more ball is ", run_player2*2)
print("runs scored by player 3 if they played 60 more ball is ", run_player3*2)
print("maximum number of sixes player 1 could hit=",run_player1//6)
print("maximum number of sixes player 2 could hit=",run_player2//6)
print("maximum number of sixes player 3 could hit=",run_player3//6)
