import random
import math

lower_num=int(input("Enter lower bound:"))
upper_num=int(input("Enter upper bound:"))

x=random.randint(lower_num,upper_num)
print("\n\tYou've only",
      round(math.log(upper_num-lower_num+ 1,2)),
      "chances to guess the number\n")

count=0

while count < math.log(upper_num-lower_num+ 1,2):
    count+=1

guess=int(input("Guess a number:"))

if x==guess:
    print("Congratulations you did it in",
          count,"try")
elif x>guess:
    print("You guessed too small!!")
elif x<guess:
    print("You guessed too high!!")

if count>=math.log(upper_num-lower_num+ 1,2):
    print("\nThe number is %d"%x)
    print("\tBetter Luck Next time")
