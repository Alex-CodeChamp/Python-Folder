import random
def scramble(word):
    a=list(word)
    random.shuffle(a)
    return "".join(a)
score= 0
words=["python","dancing","tomato","television","watch","pneumonoultramicroscopicsilicovolcanoconiosis"]#alex and more words for hw....
while True:
    bg=random.choice(words)
    scrambled_word= scramble(bg)
    print(scrambled_word)
    for i in range(3):
        a=input("What do you think the unscrambled word is(no caps)-")
        if a == bg:
            score= score + 1
            break
    gamerep=input("Do you want to play again-")
    if gamerep==("no"):
        print(score)
        break
    