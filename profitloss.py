actual=float(input("please enter the buying amount "))
selling=float(input("please enter selling amount "))
if selling>actual:
    total=selling-actual
    print("u are rich you win! u got profit of ",total)
else:
    print("u are poor game over!")