# Bill Calculator

bill=float(input(" Enter the bill\n"))
tip=int(input(" enter the tip if you wan to give 12, 10 ,15 \n"))
tipv=float((tip/100)*100)

noofpeop=int(input("enter the number of people for bill split"))

eachp=float((bill+tipv)/noofpeop)
eachp=round(eachp,2)

print(f" the bill pay by individual is:,{eachp}")