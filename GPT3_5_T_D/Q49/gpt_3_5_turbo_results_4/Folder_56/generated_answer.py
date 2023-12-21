
def if_decimal_is_divisible(bin_str):
    def fib(n):
        fibs = [0, 1]
        for i in range(2, n+1):
            fibs.append(fibs[i-1] + fibs[i-2])
        return fibs[n]

    dec_num = int(bin_str, 2)
    fib_84 = fib(84)
    return dec_num % fib_84 == 0
