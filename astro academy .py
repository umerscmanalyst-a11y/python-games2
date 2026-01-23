num=int (input(" enter the astro number"))
sum=0
temp=num
while temp>0:
    digit=temp % 10
    sum+=digit**3
    temp//=10
if num==sum:
    print(num,"it is astro number")
else:
    print(" try again you didnt succeed")