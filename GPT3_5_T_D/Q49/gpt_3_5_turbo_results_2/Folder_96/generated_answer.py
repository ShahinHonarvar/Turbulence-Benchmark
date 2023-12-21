
def if_decimal_is_divisible(decimal):
    def fibonacci(n):
        fib_list = [0, 1]
        for i in range(2, n+1):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list[n]
    
    decimal_int = int(decimal, 2)
    f_47 = fibonacci(47)
    
    if decimal_int % f_47 == 0:
        return True
    else:
        return False
