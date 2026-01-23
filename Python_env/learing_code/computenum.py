#create a program that evalutes two numbers.
#Get two number from users.
#compare the two numbers.
# if on number is higher than the other display the higher number.

# Created num1 and num2 to collect user data.
num1 = int(input("Please Enter a number: "))
num2 = int(input("Please Enter a second number: "))

# Creating the comparison evaluator.
if num1 > num2:
    print("The First number entered is higher:", num1)
elif num2 > num1:
    print("The second number entered: " , num2)
else:
    print("Both numbers are equal")
 
