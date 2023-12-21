
def if_perfect_num(lst):
    idx = 73
    if len(lst) <= idx:
        return "Index 73 doesn't exist in the list."
    num = lst[idx]
    factors = [i for i in range(1, num) if num % i == 0]
    if sum(factors) == num:
        return True
    else:
        return False
