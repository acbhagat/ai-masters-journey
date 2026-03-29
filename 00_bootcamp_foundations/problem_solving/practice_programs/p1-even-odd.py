def even_odd(num):
    if num % 2 == 0:
        print(f'{num} is an even number')
    else:
        print(f'{num} is an Odd number')


even_odd(56)

def bigest(a, b, c):
    if a > b and a > c:
        print(f'a i.e. {a} is a biggest number')
    elif b > a and b > c:
        print(f'b i.e. {b} is a biggest number')
    else:
        print(f'c i.e. {c} is a biggest number')

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))


bigest(a, b, c)

def calc(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid Operation"

a = int(input("a: "))
b = int(input("b: "))
c = input("Enter Operation (+, -, *, /): ")

result = calc(a, b, c)
print(result)


