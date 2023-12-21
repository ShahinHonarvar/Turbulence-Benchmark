
def if_perfect_num(num_list):
    try:
        num = num_list[94]
        sum_factors = sum([i for i in range(1, num) if num % i == 0])
        if sum_factors == num:
            return True
        else:
            return False
    except IndexError:
        return False
