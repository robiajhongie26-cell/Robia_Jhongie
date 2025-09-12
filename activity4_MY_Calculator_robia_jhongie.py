


num1 = float(input("Enter Number:"))
operator = input("inter operator: ")
num2 = float(input("Enter Number:"))
 
if operator == "+":
    result = num1 + num2
    print("total of ", result) 
elif operator == "-":
    result = num1 - num2
    print("total of = ", result)
elif operator == "*":
    result = num1 * num2
    print("total of = ", result)
elif operator == "/":
    if num2 == 0:
        print("connot be")
else:
    result = num1  / num2
    print("total of", result)
            