income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
Monthly_saving = income - expenses
Projected_savings = int(Monthly_saving *12 +(Monthly_saving*12*0.05))
print("Your monthly savings are $" + str(Monthly_saving)+".")
print("Projected savings after one year, with interest, is : $" + str(Projected_savings)+ ".")
