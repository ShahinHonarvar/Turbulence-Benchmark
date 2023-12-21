
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib_list = [0, 1]
            for i in range(2, n+1):
                fib_list.append(fib_list[i-1] + fib_list[i-2])
            return fib_list[n]

    decimal = int(binary_string, 2)
    fib_6th = fibonacci(6)

    return decimal % fib_6th == 0
