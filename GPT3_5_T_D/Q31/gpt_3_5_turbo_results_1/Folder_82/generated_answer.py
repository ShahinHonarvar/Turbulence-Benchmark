
def if_perfect_num(integer_list):
    num_83 = integer_list[83]
    sum_divisors = sum([i for i in range(1, num_83) if num_83 % i == 0])
    if sum_divisors == num_83:
        return True
    else:
        return False
