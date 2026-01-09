dragon_battle=int((input("enter your dragon health number to fight dinos the heigher number wins")))
elemental_element=input("does your dragon have every element yes or no")
if elemental_element=="yes":
   print("you can fight dinos start again to play again!")
else:
    if dragon_battle>=89:
        print("you can fight but be careful to fight play a battle game")
    else:
        print("your dragon number is too low play a protector game")