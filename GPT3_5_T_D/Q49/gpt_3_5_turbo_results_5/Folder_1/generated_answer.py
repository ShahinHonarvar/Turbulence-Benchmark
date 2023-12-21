
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        fib_seq = [0, 1]
        for i in range(2, n + 1):
            fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
        return fib_seq
    
    def convert_to_decimal(binary):
        decimal = 0
        for bit in binary:
            decimal = decimal*2 + int(bit)
        return decimal
    
    fib_sequence = fibonacci(90)
    decimal = convert_to_decimal(binary)
    
    return decimal % fib_sequence[89] == 0
