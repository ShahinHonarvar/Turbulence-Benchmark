
def if_perfect_num(my_list):
    if len(my_list) <= 88:
        return False
    n = my_list[88]
    sum_divisors = sum([d for d in range(1, int(n**0.5) + 1) if n % d == 0])
    return sum_divisors == n
