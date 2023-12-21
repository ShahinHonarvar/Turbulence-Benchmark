
def if_perfect_num(int_list):
    num = int_list[3]
    sum_factors = sum([i for i in range(1, num) if num % i == 0])
    if sum_factors == num:
        return True
    else:
        return False
