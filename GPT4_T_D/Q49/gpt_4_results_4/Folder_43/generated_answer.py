
def if_decimal_is_divisible(n):
    def fibonacci(n):
        fib_sequence = [0,1]
        for i in range(2,n):
            fib_sequence.append(fib_sequence[i-1]+fib_sequence[i-2])
        return fib_sequence[-1]
    
    decimal = int(n,2)
    return decimal % fibonacci(77) == 0
