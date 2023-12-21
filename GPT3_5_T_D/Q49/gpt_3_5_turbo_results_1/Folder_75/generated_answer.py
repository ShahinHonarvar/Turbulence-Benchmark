
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        fib_list = [0, 1]
        while len(fib_list) <= n:
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list[n]

    decimal = int(binary, 2)
    fib_189 = fibonacci(189)

    if decimal % fib_189 == 0:
        return True
    else:
        return False
