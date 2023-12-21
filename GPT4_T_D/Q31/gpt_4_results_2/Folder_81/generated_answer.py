
def if_perfect_num(lst):
    if len(lst) > 20:
        perfect_num = lst[20]
        divisors = [n for n in range(1, perfect_num) if perfect_num % n == 0]
        if sum(divisors) == perfect_num:
            return True
    return False
