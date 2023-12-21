
def if_decimal_is_divisible(binary_str):
    def generate_fibonacci(n):
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib[-1]

    decimal = int(binary_str, 2)
    fib_40 = generate_fibonacci(41)
    if decimal % fib_40 == 0:
        return True
    return False
