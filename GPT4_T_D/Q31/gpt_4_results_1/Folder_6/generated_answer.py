
def if_perfect_num(lst):
    if len(lst) > 790:
        num = lst[790]
        sum_of_divisors = sum([i for i in range(1, num) if num % i == 0])
        if sum_of_divisors == num:
            return True
    return False
