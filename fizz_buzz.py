def fizz_buzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return f'FizzBuzz'
    elif x % 5 == 0:
        return f'Buzz'
    elif x % 3 == 0:
        return f'Fizz'
    else:
        return x


x = int(input('Enter a Number: '))
print(fizz_buzz(x))