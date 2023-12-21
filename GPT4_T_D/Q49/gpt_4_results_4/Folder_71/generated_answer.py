
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        fib=[0]*(n+1)
        fib[1] = 1
        for i in range(2, n+1):
            fib[i] = fib[i-1] + fib[i-2]
        return fib[n]

def int_to_binary(n):
    return bin(n).replace("0b", "")

def if_decimal_is_divisible(bin_string):
    decimal_number = int(bin_string, 2)
    fib_number = fibonacci(147)
    if decimal_number % fib_number == 0:
        return True
    else:
        return False
