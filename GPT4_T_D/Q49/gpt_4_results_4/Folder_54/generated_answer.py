
def fibonacci():
    fib_list = [0, 1]
    while len(fib_list) <= 34:
        fib_list.append(sum(fib_list[-2:]))
    return fib_list[33]

def if_decimal_is_divisible(b_string):
    converted_num = int(b_string, 2)
    divisor = fibonacci()
    
    if converted_num % divisor == 0:
        return True
    else:
        return False
