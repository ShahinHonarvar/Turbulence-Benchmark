
def if_perfect_num(lst):
    n = lst[53]
    sum_divisors = sum([i for i in range(1, n) if n % i == 0])
    return sum_divisors == n
