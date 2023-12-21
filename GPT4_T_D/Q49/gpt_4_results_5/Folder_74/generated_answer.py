
def if_decimal_is_divisible(binary_num):
    decimal_num = int(binary_num, 2)
    fibonacci_num = fibonacci(166)
    if decimal_num % fibonacci_num == 0:
        return True
    else:
        return False

def fibonacci(n):
    array = [0, 1]
    while len(array) < n:
        array.append(array[-1] + array[-2])
    return array[-1]
