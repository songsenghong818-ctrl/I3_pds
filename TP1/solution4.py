#Part1---------------
print(int("7")+3.5)
print(str(10)*3)
print(bool(""),bool(" "))
print(int(3.99))
print(float("1e3"))
print(int(True)+float("2.5"))
print(round(2.5),round(3.5))
print(type(10/2))

#Part2---------------
def safe_int(text):
    try:
        return int(float(text.strip()))
    except ValueError:
        return None

for sample in ["42", " -8 ", "3.9", "abc", ""]:
    print(repr(sample), "->", safe_int(sample))

#part3---------------
def safe_int(text):
    try:
        return int(float(text.strip()))
    except ValueError:
        return None

    
num1 = safe_int(input("Enter first number: "))
num2 = safe_int(input("Enter second number: "))
if num1 is None or num2 is None:
     print("Please enter valid numbers.")
else:
     print("The sum is :",num1 + num2)


    



