line = input("Enter one line ")
con = ""
count=0
v='aeiouAEIOU'
for latter in line:
        if latter.isalpha():
                if latter not in v:
                        con+=latter
                        count+=1
print("Total consonants",con)
print("Total count",count)