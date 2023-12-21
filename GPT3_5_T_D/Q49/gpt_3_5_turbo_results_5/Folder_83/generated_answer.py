
def if_decimal_is_divisible(binary_str):
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib_list = [0, 1]
            for i in range(2, n+1):
                fib_list.append(fib_list[i-1] + fib_list[i-2])
            return fib_list[-1]
    
    decimal = int(binary_str, 2)
    fibonacci_60th = fibonacci(60)
    
    if decimal % fibonacci_60th == 0:
        return True
    else:
        return False
