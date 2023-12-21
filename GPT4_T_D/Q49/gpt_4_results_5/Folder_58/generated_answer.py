
def if_decimal_is_divisible(binary_num):
    decimal_num = int(binary_num, 2)
    fib_num1 = 0
    fib_num2 = 1
    for i in range(104):
        fib_num_next = fib_num1 + fib_num2
        fib_num1 = fib_num2
        fib_num2 = fib_num_next
    return decimal_num % fib_num2 == 0
