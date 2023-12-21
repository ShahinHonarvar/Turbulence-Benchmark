
def if_decimal_is_divisible(binary_num):
    decimal_num = int(binary_num, 2)
    num1, num2 = 0, 1
    fibonacci_num = num1
    for i in range(29):
        fibonacci_num = num1 + num2
        num1, num2 = num2, fibonacci_num
    if decimal_num % fibonacci_num == 0:
        return True
    else:
        return False
