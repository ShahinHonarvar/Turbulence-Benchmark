
def if_perfect_num(lst):
    try:
        num = lst[46]
        divisors = [i for i in range(1, num//2 + 1) if num % i == 0]
        if sum(divisors) == num:
            return True
        else:
            return False
    except IndexError:
        return False
