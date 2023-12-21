
def if_decimal_is_divisible(binary_representation):
    binary_number = int(binary_representation, 2)

    # Fibonacci function
    def fib(n):
        fib_numbers = [0, 1]
        while len(fib_numbers) < n:
            fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
        return fib_numbers[-1]

    # 94th number in the Fibonacci sequence
    num = fib(94)

    return binary_number % num == 0
