number = input("Enter a number to see its multiplication table: ")
for X in number:
  for Y in range(1, 11):
    Z =  int(X) * Y
    print(f"{X} * {Y} = {Z}")
    Y+=1
    print()