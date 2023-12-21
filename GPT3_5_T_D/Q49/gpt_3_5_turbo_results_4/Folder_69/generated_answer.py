
def if_decimal_is_divisible(bin_str):
    def fibonacci(n):
        fib_list = [0, 1]
        for i in range(2, n+1):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list[n]

    decimal = int(bin_str, 2)
    fib_170 = fibonacci(170)
    if decimal % fib_170 == 0:
        return True
    else:
        return False
