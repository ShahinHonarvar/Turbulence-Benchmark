
def if_decimal_is_divisible(bin_str):
    # calculate nth Fibonacci number
    def nthFibonacci(n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a

    # converting binary to decimal
    decimal = int(bin_str, 2)

    # calculating 176th number of Fibonacci series
    nth_fib = nthFibonacci(176)

    # checking if decimal is divisible by 176th Fibonacci number
    return decimal % nth_fib == 0
