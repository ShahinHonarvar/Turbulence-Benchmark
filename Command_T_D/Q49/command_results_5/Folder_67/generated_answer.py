def if_decimal_is_divisible(s):
    return if_binary_is_divisible(s) and if_decimal_is_divisible_by_a_Fibonacci_number(s)
def if_binary_is_divisible(s):
    return s.count("1") == 1
def if_decimal_is_divisible_by_a_Fibonacci_number(s):
    return if_decimal_is_divisible_by_Fibonacci_number(int(s, 2))
def if_decimal_is_divisible_by_Fibonacci_number(n):
    return n % 107 == 0
