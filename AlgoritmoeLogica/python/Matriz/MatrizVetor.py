import random

i = 0
vetor=[0]*10


while i<len(vetor):
    vetor[i]=random.randint(-100,100)
    i=i+1
i=0
while i<len(vetor):
        if vetor[i]<=0:
         vetor[i]=1
        i = i+1