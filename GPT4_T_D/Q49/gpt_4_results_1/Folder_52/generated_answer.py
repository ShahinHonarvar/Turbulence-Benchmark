
def if_decimal_is_divisible(bin_str):
    def fib(n):
        if n<=0:
           return 0
        elif n==1:
           return 1
        else:
          return fib(n-1)+fib(n-2)
    
    num = int(bin_str, 2)
    fib_num = fib(176)
    
    if num % fib_num == 0:
        return True
    else:
        return False
