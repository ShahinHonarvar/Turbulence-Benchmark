
def if_decimal_is_divisible(binary_str):
    fibonacci_numbers = [0, 1]

    def compute_fibonacci(n):
        if n <= len(fibonacci_numbers) - 1:
            return fibonacci_numbers[n]
        fibonacci_numbers.append(compute_fibonacci(n - 1) + compute_fibonacci(n - 2))
        return fibonacci_numbers[n]

    def binary_to_decimal(bin_string):
        return int(bin_string, 2)

    if binary_to_decimal(binary_str) % compute_fibonacci(154) == 0:
        return True
    else:
        return False
