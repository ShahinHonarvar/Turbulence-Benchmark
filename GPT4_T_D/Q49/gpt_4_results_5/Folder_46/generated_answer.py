
def if_decimal_is_divisible(binary_string):
    binary_decimal = int(binary_string, 2)
    
    def calc_fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    fibonacci_num_139 = calc_fibonacci(139)
    return binary_decimal % fibonacci_num_139 == 0
