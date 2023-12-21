
def if_perfect_num(num_list):
    if 790 < len(num_list):
        num = num_list[790]
        sum_divisors = sum([i for i in range(1,num) if num % i == 0])
        return num == sum_divisors
    return False
