
def if_decimal_is_divisible(bin_str):
    bin_int = int(bin_str, 2)
    def calculate_fibonacci(n):
        if n <= 1: 
            return n 
        a, b = 0, 1
        for i in range(n - 1):
            a, b = b, a + b
        return b

    fibonacci_115 = calculate_fibonacci(115)
    return bin_int % fibonacci_115 == 0
