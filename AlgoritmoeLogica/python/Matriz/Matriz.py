m1=[0]*3
m2=[0]*3

for i in range(len(m1)):
        m1[i] = [0]*3
        m2[i] = [0]*3
        for j in range(len(m1[i])):
            m1[i][j] = i+1
            m2[i][j] = j+1
print(m1)
print(m2)
for i in range(len(m1)):
    for j in range(len(m1[i])):
        if m1[i][j] == m2[i][j]:
            m1[i][j] = 0
        else:
             m2[i][j] = 1
print(m1)
print(m2)
