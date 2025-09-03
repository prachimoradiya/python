line = input("Enter one line ")
symbol= 0
for latter in line:
    if not latter.isalnum() and not latter.isspace():
        symbol+=1
print("Total symbol",symbol)