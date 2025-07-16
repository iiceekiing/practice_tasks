# Simple calculator app

print(""" Welcome to Ekuke calculator 🆓 🤖 📲

MENU:
you can perform!:
1. Addition
2. Subtraction
3. Multiplication
4. Division {1. integer division, 2. floor division, 3. modulus} 
5. Exponential
6. Show Last operation
7. Show all previous operations
8. Exit
""" 
)


choice = float(input('select any option to run operation: '))

if choice == 1:
	print("great! your are now ready to perform 'Addition! ➕ ' \n ")
	num1 = float(input("Please enter first number: "))
	num2 = float(input("Please enter second number: "))
	sum = num1 + num2
	print(f"The sum of {num1} and {num2} = {sum}")


elif choice == 2:
	print("Now ready to perform 'Subtraction! ➖' \n ")
	num1 = float(input("Please enter first number: "))
	num2 = float(input("Please enter second number: "))
	sub = num1 - num2
	print(f"The difference between {num1} and {num2} is = {sub}") 

elif choice == 3:
	print("Now ready to perform 'Multiplication! ✖️ ' \n ")
	num1 = float(input("Please enter first number:  "))
	num2 = float(input("Please enter second number:  "))
	mul = num1 * num2
	print(f"The product of {num1} and {num2} is = {mul}")

elif choice == 4:
	print("Now ready to perform 'Division! ➗' \n ")
	division_type = int(input('''please select type of division: 
	1 for float division /
	2 for floor/integer division //
	3 for modulus didvision %
	4 to exit 
	'''

	))

	
	if division_type == 1: 
		print("Now ready to perform integer division! \n ")
		num1 = float(input("Please enter the numerator:  "))
		num2 = float(input("Please enter the denominator:  "))
		float_division = num1 / num2
		print(f"{num1} / {num2} is = {float_division:.2f}")

	elif division_type == 2:
		print("Now ready to perform floor or integer division! \n ")
		num1 = float(input("Please enter the dividend:  "))
		num2 = float(input("Enter the divisor:  "))
		floor_division = num1 // num2 
		print(f"{num1} // {num2} = {floor_division:.2f}")

	elif division_type == 3:
		print('Now ready to perform modulus operation \n ')
		num1 = float(input("Enter first number:  "))
		num2 = float(input("Enter second number:  "))
		modulus = num1 % num2
		print(f"{num1} % {num2} = {modulus}")

	else:
		print("good bye! 👋👋👋 \n ") 



elif choice == 5: 
	print("Your now ready to perform 'Exponentials'")
	num1 = float(input("Please enter base number:  "))
	num2 = float(input("Please enter the exponent/power:  "))
	exp = num1 ** num2
	print(f"{num1} exponential {num2} = {exp:.2f}")
