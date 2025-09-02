age = int(input("Enter yout age: "))
balance = 20000
if age<18:
    print("you are under 18 pyment not allow")
else:
    balance = int(input("Enter your balance"))

    amount = int(input("Enter amount tp pay "))

    if amount<=balance:
        balance=amount
        print(f"payment successful")
        print(f"remaining balance:{balance}")

    else:
        print("payment failed")