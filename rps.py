#rock, paper, scissor
from random import randint

player = False

class computer():
    def __init__(self, n, c, w):
        self.name = n
        self.color = c
        self.weight = w
    def greet (self):
        print ("hello, I am " + self.name)
    def taunt (self):
        print ("Are you ready to lose?")
    def taunt2 (self):
        print("fuck you, let's play!")
c1 = computer("amada", "brown", "100")
print(c1.greet())
while player == False:
    player = input("Say hello or bye")
    if player == "hello":
        print(c1.taunt())
    if player == "bye":
        print(c1.taunt2())

x = ("rock", "paper", "scissor")

c1 = x[randint(0,2)]

player = False

while player == False:
    player = input("rock! paper! scissor!")
    if player == c1:
        print ("It's a tie! Again!")
    elif player == "rock":
        if c1 == "paper":
            print ("Haha! I won!")
        if c1 == "scissor":
            print ("You won this time!")
    elif player == "paper":
        if c1 == "rock":
            print ("You won this time!")
        if c1 == "scissor":
            print ("Haha! I won!")
    elif player == "scissor":
        if c1 == "rock":
            print ("Haha! I won!")
        if c1 == "paper":
            print ("You won this time!")
    else:
        print ("Hurry up, and play something, pussy!")
player = False
computer = x[randint(0,2)]





