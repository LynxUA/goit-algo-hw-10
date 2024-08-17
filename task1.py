import pulp

prob = pulp.LpProblem("Maximize_Drink_Production", pulp.LpMaximize)

lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('FruitJuice', lowBound=0, cat='Continuous')

prob += lemonade + fruit_juice, "Total_Production"

prob += 2 * lemonade + fruit_juice <= 100, "Water_Constraint"
prob += 1 * lemonade <= 50, "Sugar_Constraint"
prob += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
prob += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# WA for Mac on Apple Silicon
# You need to have GLPK installed 
# brew install glpk 
prob.solve(pulp.GLPK_CMD())
# or use default solver
# prob.solve()

print(f"Статус: {pulp.LpStatus[prob.status]}")
print(f"Оптимальне виробництво лимонаду: {lemonade.varValue} штук")
print(f"Оптимальне виробництво фруктового соку: {fruit_juice.varValue} штук")
print(f"Всього: {pulp.value(prob.objective)} штук")
