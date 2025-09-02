a = int(input("Enter your Mark: "))

if a>=33:
    print("result:pass")

    if a>=90:
        print("Grade A+")
    elif a<=89 and a>=80:
        print("Gread A")
    elif a<=79 and a>=70:
        print("Gread B")
    elif a<=69 and a>=60:
        print("Gread c")
    else:
        print("Gread D")
else:
    print("fail")
    