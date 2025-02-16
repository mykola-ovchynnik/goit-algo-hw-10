import pulp

model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

x = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
y = pulp.LpVariable("FruitJuice", lowBound=0, cat="Integer")

model += x + y, "Total_Drinks"

model += 2 * x + y <= 100, "Water_Constraint"
model += x <= 50, "Sugar_Constraint"
model += x <= 30, "LemonJuice_Constraint"
model += 2 * y <= 40, "FruitPuree_Constraint"

model.solve()

print("Lemonade =", x.varValue)
print("Fruit juice =", y.varValue)
print("Total amount =", pulp.value(model.objective))
