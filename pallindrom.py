line =input("Enter string: ")
revers=line[::-1]
if line == revers:
    print(f"{line} is pallindroem ")
else:
    print(f"{line} is not pallindrome ")