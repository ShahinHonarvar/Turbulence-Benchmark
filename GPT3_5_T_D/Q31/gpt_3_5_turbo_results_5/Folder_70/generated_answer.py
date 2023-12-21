
def if_perfect_num(lst):
    perfect_num = lst[845]
    divisors_sum = sum([i for i in range(1, perfect_num) if perfect_num % i == 0])

    if divisors_sum == perfect_num:
        return True
    else:
        return False
