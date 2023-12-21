
def if_perfect_num(my_list):
    num = my_list[96]
    sum_factors = sum([i for i in range(1, num) if num % i == 0])
    if sum_factors == num:
        return True
    else:
        return False
