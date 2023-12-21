
def if_decimal_is_divisible(binary_string):
    def fibonacci_number(index):
        fib_seq = [0, 1]
        if index > 1:
            for i in range(2, index + 1):
                fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
        return fib_seq[index]

    decimal_number = int(binary_string, 2)
    fibonacci_125th = fibonacci_number(125)
    return decimal_number % fibonacci_125th == 0
