meat = ["Ham",3.99,50,"Sliced"]
cheese = ["Chedder",5.49,100,"Sharp"]
condiment = ["Mustard",1.99,75,"Spicy"]

deli_dept = [meat,cheese,condiment]

if deli_dept[0] == meat and meat[2] < 100:
    meat[2] = 100
else:
    ()

seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)
deli_dept.remove(condiment)
deli_dept.sort()

print("Initial Deli List:",deli_dept)
print("Updated Deli List:",deli_dept[0][0] , deli_dept[1][0] , deli_dept[2][0])