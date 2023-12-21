
def if_perfect_num(num_list):
    if len(num_list) > 926:
        num = num_list[926]
        sum_factors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_factors += i
        if sum_factors == num:
            return True
    return False
