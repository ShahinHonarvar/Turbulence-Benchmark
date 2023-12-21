
def if_decimal_is_divisible(binary_representation):
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib_sequence = [0, 1]
            for i in range(2, n+1):
                fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
            return fib_sequence[n]
    
    decimal = int(binary_representation, 2)
    fib = fibonacci(77)
    return decimal % fib == 0
