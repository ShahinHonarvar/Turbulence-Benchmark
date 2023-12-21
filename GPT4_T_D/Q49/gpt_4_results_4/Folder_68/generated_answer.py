
def if_decimal_is_divisible(bin_str):
    def fibonacci(n):
        a,b = 0,1
        for _ in range(n):
            a,b = b,a+b
        return a

    thirty_eighth_fibonacci = fibonacci(38)
    num = int(bin_str, 2)

    return num % thirty_eighth_fibonacci == 0
