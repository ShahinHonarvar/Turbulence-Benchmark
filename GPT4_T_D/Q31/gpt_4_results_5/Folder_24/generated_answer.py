
def if_perfect_num(int_list):
    target = int_list[74]
    divisors_sum = sum([ii for ii in range(1, target) if target % ii == 0])
    return divisors_sum == target
