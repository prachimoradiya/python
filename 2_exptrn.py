for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()


for i in range(1,5+1):
        print(" " * (5-i) + "* " * i)


for i in range(1,5+1):
        print(" " * (5-i) + "*"*i)
 


for i in range(0, 5 + 1):
        print(" " * (5 - i), end='')
        for j in range(0,i + 0):
            print((i + j) % 2,end=' ')
        print()
    


for i in range(1,5 + 1):
    print( " " *(5 - i), end='')
    print((str(i) + " ") * i)
for i in range(5 - 1, 0, -1):
    print( " " * (5 - i), end='')
    print((str(i) + " ")* i)


for i in range(1,5 + 1):
    print( " " * (5 - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
for i in range(5 - 1, 0, -1):
    print( " " * (5 - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


for i in range(5):
     row = []
     for j in range(5):
          if i in (0, 5-1) or j in (0, 5-1) or (i == 5 // 2 and j == 5 // 2):
                row.append('*')
          else:
                row.append('')
print(''.join(row))