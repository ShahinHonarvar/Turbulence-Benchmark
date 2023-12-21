
def if_decimal_is_divisible(binary_num):
    def fibonacci(n):
        if n <= 1:
           return n
        else:
           return(fibonacci(n-1) + fibonacci(n-2))

    fib_num = fibonacci(154)
    decimal_num = int(binary_num,2)

    if decimal_num % fib_num == 0:
        return True
    else:
        return False
