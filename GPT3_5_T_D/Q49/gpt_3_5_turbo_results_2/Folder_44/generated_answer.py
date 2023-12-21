
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        sequence = [0, 1]
        for i in range(2, n+1):
            sequence.append(sequence[i-1] + sequence[i-2])
        return sequence[n]
    
    decimal = int(binary, 2)
    fibonacci_159th = fibonacci(159)
    
    if decimal % fibonacci_159th == 0:
        return True
    else:
        return False
