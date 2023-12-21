
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    if decimal % fib(146) == 0:
        return True
    else:
        return False
