
def if_decimal_is_divisible(binary_str):
    def fibonacci(n):
        if n<=1:
            return n
        else:
            a,b = 0,1
            for i in range(2,n+1):
                a, b = b, a+b
            return b
    
    sixth_fib_num = fibonacci(6)
    decimal_number = int(binary_str, 2)
    return decimal_number % sixth_fib_num == 0
