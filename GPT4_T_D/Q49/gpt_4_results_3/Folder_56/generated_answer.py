
def if_decimal_is_divisible(binary_num):
    decimal_int = int(binary_num, 2)
    fibonaccis = []
    num1, num2 = 0, 1
    while len(fibonaccis) < 84:
        fibonaccis.append(num1)
        num1, num2 = num2, num1 + num2
    return decimal_int % fibonaccis[-1] == 0
