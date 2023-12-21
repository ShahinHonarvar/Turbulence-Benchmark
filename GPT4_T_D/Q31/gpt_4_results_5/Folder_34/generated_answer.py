
def if_perfect_num(lst):
    num = lst[97] if len(lst) > 97 else -1
    if num > 0:
        sum_of_divisors = sum([i for i in range(1, num) if num % i == 0])
        if sum_of_divisors == num:
            return True
    return False
