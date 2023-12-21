
def if_decimal_is_divisible(binary_repr):
    def fibonacci_seq(n):
        fib_seq = [0, 1]
        while len(fib_seq) < n:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq[n-1]
        
    decimal_num = int(binary_repr, 2)
    fib_117 = fibonacci_seq(117)
    
    return decimal_num % fib_117 == 0
