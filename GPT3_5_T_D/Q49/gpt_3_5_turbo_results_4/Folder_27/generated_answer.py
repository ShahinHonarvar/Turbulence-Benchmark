
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        if n <= 1:
            sequence = [0]
        else:
            sequence = [0, 1]
            for _ in range(n - 2):
                sequence.append(sequence[-1] + sequence[-2])
        return sequence

    fibonacci_sequence = fibonacci(87)
    decimal = int(binary, 2)

    if decimal % fibonacci_sequence[-1] == 0:
        return True
    else:
        return False
