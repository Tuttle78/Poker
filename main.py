
import random as ran

deck=["da","d2","d3","d4","d5","d6","d7","d8","d9","d9","d10","dj","dq","dk","sa","s2","s3","s4","s5","s6","s7","s8","s9","s10","sj","sq","sk","ha","h2","h3","h4","h4","h5","h6","h7","h8","h9","h10","hj","hq","hk","ca","c2","c3","c4","c5","c6","c7","c8","c9","c10","cj","cq","ck"]
#hand
hand1=ran.choice(deck)
deck.remove(hand1)
hand2=ran.choice(deck)
deck.remove(hand2)
river=[]
raiseNum=0
Raise=False
pot=0
money=100


#river
for _ in range(3):
    riverT = ran.choice(deck)
    deck.remove(riverT)
    river.append(riverT)





#gameplay
print(hand1)
print(hand2)
decision=input("raise, check, or fold?")
if decision=="raise":
    Raise=True
    raiseNum=input("amount - ")
elif decision=="check":
    print(river)
