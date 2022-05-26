m = [0]*3

for i in range(len(m)):
    m[i]=[0]*3

    for j in range(len(m[i])):
        m[i][j]=int(input())
        
for i in range(len(m)-1,-1,-1):
    print("")
    for j in range (len(m[i])-1,-1,-1):
        print(m[i][j], end="")