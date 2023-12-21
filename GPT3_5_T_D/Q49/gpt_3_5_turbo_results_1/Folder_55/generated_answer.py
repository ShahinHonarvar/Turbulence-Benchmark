
def if_decimal_is_divisible(binary_rep):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return(fibonacci(n-1) + fibonacci(n-2))

    decimal_num = int(binary_rep, 2)
    fibonacci_39th = fibonacci(39)

    if decimal_num % fibonacci_39th == 0:
        return True
    else:
        return False
