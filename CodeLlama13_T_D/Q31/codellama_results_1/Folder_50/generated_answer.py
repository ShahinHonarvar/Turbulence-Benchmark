
def if_perfect_num(lst):
    if len(lst) <= 40:
        return False
    else:
        n = lst[40]
        sum_divisors = sum([i for i in range(1, int(n**0.5)+1) if n % i == 0])
        return sum_divisors == n
