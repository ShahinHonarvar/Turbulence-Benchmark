
def if_perfect_num(lst):
    if len(lst) > 66:
        num = lst[66]
        divisors = [i for i in range(1, num) if num % i == 0]
        return True if sum(divisors) == num else False
    else:
        return False
