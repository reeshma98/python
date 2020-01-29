name=str(input("enter your name:"))
fromloc=str(input("enter your location:"))
toloc=str(input("enter your destination:"))
dis=int(input("enter distance in kilometer:"))
print("1.premium")
print("2.non-premium")
print("3.ac")
print("4.non-ac")
print("5.sleeper")
print("6.semi-sleeper")
category=int(input("select the category"))
if category==1:
    cost=dis*5
elif category==2:
    cost=dis*3.50
elif category==3:
    cost=dis*4
elif category==4:
    cost=dis*2
elif category==5:
    cost=dis*2.50
elif category==6:
    cost=dis*1.50
else:
    print("invalid selection")
print("---------your bill-------")
print("name: ",name)
print("from: ",fromloc)
print("destination: ",toloc)
print("distance: ",dis)
print("cost: ",cost)
