
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        result = [0,1]
        while len(result) <= n:
            result.append(result[-1] + result[-2])
        return result[n]
        
    decimal_number = int(binary_string, 2)
    fibonacci_27th = fibonacci(27)
    if decimal_number % fibonacci_27th == 0:
        return True
    else:
        return False
