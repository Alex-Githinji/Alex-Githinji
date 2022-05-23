weight = int(input (" weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "k":
    converted = weight / 0.45
    print ("weight in Lbs: " + converted)
else:
    converted = weight * 0.45
    print ("weight in kgs: "+ str(converted))





