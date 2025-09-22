import random
y=random.randint(0,4)
x=random.randint(0,4)
grid=[]
for a in range(5):
    row=[]
    for i in range(5):
        row.append("_")
    grid.append(row)
print(grid)
def display():
    for o in range(5):#
        for a in range(5):
            print(grid[o][a],end=" ")
        print()
while True:
    print("Look at the grid above it has is hidden point one of them will let you win the game the others will not.\n guess the co ordinates of the secret point \n(Guess colum first and then row )" )
    c=int(input("What do you think the colum is of the hiden points-"))
    r=int(input("what do you think the row of the hidden point is-"))
    grid
    grid[r][c]="*"
    display()
    if c==y and r==x:
        print("you win")
        break
    else:
        print("try again")
        if y<c:
            print("Move Left")
        else:
            print("Move right")
        if r<x:
            print("Move down")
        else:
            print("Move up")