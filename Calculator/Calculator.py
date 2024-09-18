def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print("Choose an operation")
print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")

choice=input("\n Input an operation: ")

num1=int(input("Input the first value: "))
num2=int(input("Input the second value: "))

if choice=="A":
    print("Addition of the two values is ", add(num1,num2))
elif choice=="B":
    print("Subtraction of the two values is ", sub(num1,num2))
elif choice=="C":
    print("Multipilication of the two values is ", mul(num1,num2))
elif choice=="D":
    print("Division of the two values is ", div(num1,num2))
else:
    print("Inavild Input")