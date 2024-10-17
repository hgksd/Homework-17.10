import random
k = 0
l = 0
o = 3
p = ("paper","rock","scissors")
while True:
     q1 = input("hello ,do you wanna play?Yes,No: ").lower()
     if q1 == 'yes':
          print("okay")
          break
     elif q1 == 'no':
          print("Bye")
          quit()
     else:
          print("Write right option")

q2 = input("Your challenge will be to beat me at rock-paper-scissors.Just press enter: ")
for i in range(o):
     
      q2 = input("Choose rock, paper, or scissors: ").lower()
      q3 = random.choice(p)
      print(f"I chose: {q3}")

      if  q2 == q3:
          o = o + 1
          print("It's a tie!")
          


      elif (q2 =="scissors" and q3 =="rock") or (q2 =="rock" and q3 =="paper") or (q2 =="paper" and q3 =="scissors") :
          k = k + 1

          print(f"You lost! ({k} losses, {l} wins)")
      elif (q2 =="scissors" and q3 =="paper") or (q2 =="rock" and q3 =="scissors") or (q2 =="paper" and q3 =="rock") :
          l = l + 1

          print(f"You win! ({k} losses, {l} wins)")
      else:
          o = o + 1
          print("Invalid choice, please try again.")

for t in range(3) :
     if l > k :
          print(" You win!!!!!")
     else:
          print(" You lose!!!!!")
          


     
          
          


