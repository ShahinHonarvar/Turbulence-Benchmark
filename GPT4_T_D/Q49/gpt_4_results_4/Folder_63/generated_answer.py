
def if_decimal_is_divisible(bin_string):
    import sys
    sys.setrecursionlimit(10000)
    def fibonacci(num):
        if num<0:
            print("Incorrect input")
        elif num==0:
            return 0
        elif num==1 or num==2:
            return 1
        else:
            return fibonacci(num-1) + fibonacci(num-2)
         
    num_144 = fibonacci(144)

    decimal_num = int(bin_string, 2)

    if decimal_num % num_144 == 0:
        return True
    else:
        return False
