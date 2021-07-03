import random
# import replit
s1=random.randint(11,40)
s2=random.randint(41,70)
s3=random.randint(71,100)
l1=random.randint(1,30)
l2=random.randint(31,60)
l3=random.randint(61,90)
p1 = 0
p2 = 0
p3 = 0
p4 = 0
playernum=input("How many players do you want? 2, 3 or 4.")
if playernum=="2":
  print("Player 1 position =", p1)
  print("Player 2 position =", p2)
  while p1<100 and p2<100:
    input("Player 1, please press 'Enter' to roll the dice.")
    # replit.clear()
    print("There are snakes at ",s1,s2,s3," and there are ladders at ",l1,l2,l3,".")
    dice = random.randint(1,6)
    print("You rolled a", dice)
    p1 = p1 + dice
    if p1==s1 or p1==s2 or p1==s3:
      print ("Player 1 hit a snake. Player 1 will move back 10 spaces")
      p1=p1-10
    if p1==l1 or p1==l2 or p1==l3:
      p1=p1+10
      print ("Player 1 hit a ladder. Player 1 will move forward 10 spaces")
    print("Player 1 is in position ", p1)
    input("Player 2, please press 'Enter' to roll the dice.")
    dice = random.randint(1,6)
    print("You rolled a", dice)
    p2 = p2 + dice
    if p2==s1 or p2==s2 or p2==s3:
      print ("Player 2 hit a snake. Player 2 will move back 10 spaces")
      p2=p2-10
    if p2==l1 or p2==l2 or p2==l3:
      p2=p2+10
      print ("Player 2 hit a ladder. Player 2 will move forward 10 spaces")
    print("Player 2 is in position ", p2)
  if p1>p2:
    print ("Congratulations Player 1. You won.")
  else:
    print ("Congratulations Player 2. You won.")
elif playernum=="3":
  print("Player 1 position =", p1)
  print("Player 2 position =", p2)
  print("Player 3 position =", p3)
  while p1<100 and p2<100 and p3<100:
    input("Player 1, please press 'Enter' to roll the dice.")
    # replit.clear()
    print("There are snakes at ",s1,s2,s3," and there are ladders at ",l1,l2,l3,".")
    dice = random.randint(1,6)
    print("You rolled a", dice)
    p1 = p1 + dice
    if p1==s1 or p1==s2 or p1==s3:
      print ("Player 1 hit a snake. Player 1 will move back 10 spaces")
      p1=p1-10
    if p1==l1 or p1==l2 or p1==l3:
      p1=p1+10
      print ("Player 1 hit a ladder. Player 1 will move forward 10 spaces")
    print("Player 1 is in position ", p1)
    input("Player 2, please press 'Enter' to roll the dice.")
    dice = random.randint(1,6)
    print("You rolled a", dice)
    p2 = p2 + dice
    if p2==s1 or p2==s2 or p2==s3:
      print ("Player 2 hit a snake. Player 2 will move back 10 spaces")
      p2=p2-10
    if p2==l1 or p2==l2 or p2==l3:
      p2=p2+10
      print ("Player 2 hit a ladder. Player 2 will move forward 10 spaces")
    print("Player 2 is in position ", p2)
    input("Player 3, please press 'Enter' to roll the dice.")
    dice = random.randint(1,6)
    print("You rolled a", dice)
    p3 = p3 + dice
    if p3==s1 or p3==s2 or p3==s3:
      print ("Player 3 hit a snake. Player 3 will move back 10 spaces")
      p3=p3-10
    if p3==l1 or p3==l2 or p3==l3:
      p3=p3+10
      print ("Player 3 hit a ladder. Player 3 will move forward 10 spaces")
    print("Player 3 is in position ", p3)
  if p1>p2 and p1>p3:
    print ("Congratulations Player 1. You won.")
  elif p2>p1 and p2 > p3:
    print ("Congratulations Player 2. You won.")
  else:
    print ("Congratulations Player 3. You won.")
else:
  print("Player 1 position =", p1)
  print("Player 2 position =", p2)
  print("Player 3 position =", p3)
  print("Player 4 position =", p4)
  while p1<100 and p2<100 and p3<100 and p4<100:
    input("Player 1, please press 'Enter' to roll the dice.")
    # replit.clear()
    print("There are snakes at ",s1,s2,s3," and there are ladders at ",l1,l2,l3,".")
    dice = random.randint(1,6)
    print("You rolled a", dice)
    p1 = p1 + dice
    if p1==s1 or p1==s2 or p1==s3:
      print ("Player 1 hit a snake. Player 1 will move back 10 spaces")
      p1=p1-10
    if p1==l1 or p1==l2 or p1==l3:
      p1=p1+10
      print ("Player 1 hit a ladder. Player 1 will move forward 10 spaces")
    print("Player 1 is in position ", p1)
    input("Player 2, please press 'Enter' to roll the dice.")
    dice = random.randint(1,6)
    print("You rolled a", dice)
    p2 = p2 + dice
    if p2==s1 or p2==s2 or p2==s3:
      print ("Player 2 hit a snake. Player 2 will move back 10 spaces")
      p2=p2-10
    if p2==l1 or p2==l2 or p2==l3:
      p2=p2+10
      print ("Player 2 hit a ladder. Player 2 will move forward 10 spaces")
    print("Player 2 is in position ", p2)
    input("Player 3, please press 'Enter' to roll the dice.")
    dice = random.randint(1,6)
    print("You rolled a", dice)
    p3 = p3 + dice
    if p3==s1 or p3==s2 or p3==s3:
      print ("Player 3 hit a snake. Player 3 will move back 10 spaces")
      p3=p3-10
    if p3==l1 or p3==l2 or p3==l3:
      p3=p3+10
      print ("Player 3 hit a ladder. Player 3 will move forward 10 spaces")
    print("Player 3 is in position ", p3)

    input("Player 4, please press 'Enter' to roll the dice.")
    dice = random.randint(1,6)
    print("You rolled a", dice)
    p4 = p4 + dice
    if p4==s1 or p4==s2 or p4==s3:
      print ("Player 4 hit a snake. Player 4 will move back 10 spaces")
      p4=p4-10
    if p4==l1 or p4==l2 or p3==l3:
      p4=p4+10
      print ("Player 4 hit a ladder. Player 4 will move forward 10 spaces")
    print("Player 4 is in position ", p3)
  if p1>p2 and p1>p3 and p1>p4:
    print ("Congratulations Player 1. You won.")
  elif p2>p1 and p2 > p3 and p2 > p4:
    print ("Congratulations Player 2. You won.")
  elif p3>p1 and p3 > p2 and p3 > p4:
    print ("Congratulations Player 3. You won.")
  else:
    print ("Congratulations Player 4. You won.")