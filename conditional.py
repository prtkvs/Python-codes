# proper indentation is mandatory
age = 1
if age >= 18:
    print("You're adult")   # distance of tab(4-spaces) is must
    print("You can vote") 
elif age>3 and age<18:      # represents else if
    print("You're in school")
else:
    print("You're a child")

print("thank you") # not inside indentation therefore does not on IF statement(run indenpendently)

# calculator program
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operator = input("Enter +,-,*,/: ")
if operator=='+':
    print(int(num1)+int(num2))
elif operator=='-':
    print(int(num1)-int(num2))
elif operator=='*':
    print(int(num1)*int(num2))
else:
    print(print(int(num1)/int(num2)))

print("Thank You!")