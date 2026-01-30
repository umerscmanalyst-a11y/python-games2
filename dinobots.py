String=input("enter a dinobot name")
char=input("enter your name of dinobot")
i=0
count=0
while (i<len(String)):
    if(String[i]==char):
        count=count+1
    i=i+1
print("total number of times",char,"has appeared",count)