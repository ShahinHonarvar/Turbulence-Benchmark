
def fib(n): 
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def if_decimal_is_divisible(binary):
    num = int(binary, 2)
    fnum = fib(180)
    return num % fnum == 0
