
def if_decimal_is_divisible(binary_repr):
    def fibonacci(n):
        fib_list = [0, 1]
        if n == 0:
            return fib_list[0]
        elif n == 1:
            return fib_list[1]
        else:
            for i in range(2, n+1):
                fib_list.append(fib_list[i-1] + fib_list[i-2])
            return fib_list[n]

    decimal = int(binary_repr, 2)
    fib_88 = fibonacci(88)

    return decimal % fib_88 == 0
