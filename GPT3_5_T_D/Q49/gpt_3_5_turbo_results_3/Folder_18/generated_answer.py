
def if_decimal_is_divisible(binary_num):
    def fibonacci(n):
        sequence = [0, 1]
        for i in range(2, n+1):
            sequence.append(sequence[i-1] + sequence[i-2])
        return sequence[n]
    
    decimal_num = int(binary_num, 2)
    fibonacci_199th = fibonacci(199)
    
    if decimal_num % fibonacci_199th == 0:
        return True
    else:
        return False
