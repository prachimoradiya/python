line = input("Enter one line ")
vowels = 0
v='aeiouAEIOU'
for latter in line:
    if latter in v:
        vowels+=1
print("Total vowels",vowels)