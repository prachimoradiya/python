line = input("Enter one line ")
digit = 0
for latter in line:
    if latter.isdigit():
        digit+=1
print("Total digits",digit)