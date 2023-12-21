
def if_perfect_num(lst):
    if len(lst) <= 29:
        return False
    num = lst[29]
    sum_of_divisors = sum([d for d in range(1, num + 1) if num % d == 0])
    return sum_of_divisors == num * (num + 1) // 2
