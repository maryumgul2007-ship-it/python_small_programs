a = float(input("enter the first number : "))
b = float(input("enter the second number : "))
# take operator from the user 
operator = input("enter operator (+, -, *, %, / ):")
#calculate based on th operator
if operator == "+":
    print("resul:t" , a+b)   
elif operator == "-":
    print("result :", a-b)
elif operator == "%":
    print("result :", a % b)
elif operator == "/":
    print("ressult :" , a / b)
elif operator == "*":
    print("result :" , a * b)           
else:
    print("invalid operator:")    