line=input("Enter a string ")
revers=""
for i in range(len(line)-1,-1,-1):
    revers+=line[i]
print("original string",line)
print("revers string",revers)