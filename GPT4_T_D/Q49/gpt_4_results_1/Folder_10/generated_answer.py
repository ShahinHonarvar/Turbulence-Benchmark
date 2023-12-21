
def if_decimal_is_divisible(bin_string):
    num = int(bin_string, 2)
    fibo_nums = [0, 1]
    while len(fibo_nums) < 88:
        fibo_nums.append(fibo_nums[-1] + fibo_nums[-2])
    return num % fibo_nums[-1] == 0
