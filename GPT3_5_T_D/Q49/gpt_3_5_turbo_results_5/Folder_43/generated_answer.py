
def if_decimal_is_divisible(bin_str):
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

    dec_num = int(bin_str, 2)
    fib_77 = fibonacci(77)

    if dec_num % fib_77 == 0:
        return True
    else:
        return False
