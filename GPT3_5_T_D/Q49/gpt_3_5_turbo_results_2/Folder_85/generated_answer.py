
def if_decimal_is_divisible(binary_representation):
    def fibonacci(n):
        fib = [0, 1] # initialize the first two numbers in the Fibonacci sequence
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2]) # calculate the next number by summing the previous two numbers
        return fib[n] # return the nth number in the Fibonacci sequence

    decimal_integer = int(binary_representation, 2) # convert binary_representation to decimal integer
    fibonacci_45th = fibonacci(45) # calculate the 45th number in the Fibonacci sequence

    if decimal_integer % fibonacci_45th == 0: # check if the decimal integer is divisible by the 45th Fibonacci number
        return True
    else:
        return False
