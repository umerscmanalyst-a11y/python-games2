print("enter your marks in your subjects out of 500")
aqua_grabber=int (input("enter your marks in aqua grabber: "))
card_jitsu_vs=int (input("enter your marks in card jitsu versions: "))
ice_fishing=int (input("enter your marks in ice fishing: "))
agent_agency=int (input("enter your marks in agent agency : "))
puffle_launch=int (input("enter your marks in puffle launch: "))
total=aqua_grabber+card_jitsu_vs+ice_fishing+agent_agency+puffle_launch
print("your total marks are: ",total)
if total>=450:
    print("you are not normal like other students")
else:
    print("you will do it soon just keep trying hard and again to succeed")