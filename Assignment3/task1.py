a = int(input('Enter a number: '))

def fact(n):
    if(n<2):
        return 1
    else:
        return n*fact(n-1)

print('Factorial of', a, 'is: ', fact(a))