print("This is a calcuator.")
a = int(input("Enter first num"))
c = str(input("+ - * /"))
b = int(input("Enter second num"))
if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "/":
    print(a/b)
elif c == "*":
    print(a*b)