binary = input("Enter The Number ")
decimal = 0

for digit in binary :
    decimal = decimal * 2 +  int(digit)
print(decimal)