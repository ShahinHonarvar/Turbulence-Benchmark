
def if_perfect_num(lst):
    num_at_321 = lst[321]
    divisors_sum = sum(i for i in range(1, num_at_321) if num_at_321 % i == 0)
    return divisors_sum == num_at_321
