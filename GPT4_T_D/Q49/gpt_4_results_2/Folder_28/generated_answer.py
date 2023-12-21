
def fibonacci_number(n):
    if n<0:
        return "Incorrect input"
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        fib_values = [0, 1]
        while len(fib_values) < n+1:
            fib_values.append(fib_values[len(fib_values)-1] + fib_values[len(fib_values)-2])
        return fib_values[n]

def if_decimal_is_divisible(bin_string):
    decimal = int(bin_string, 2)
    return decimal % fibonacci_number(104) == 0
