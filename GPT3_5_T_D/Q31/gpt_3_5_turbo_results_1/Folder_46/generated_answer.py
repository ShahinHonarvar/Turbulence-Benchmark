
def if_perfect_num(lst):
    num = lst[453]
    if num < 1:
        return False
    factors = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            factors.append(i)
            if i != num // i:
                factors.append(num // i)
    if sum(factors) - num == num:
        return True
    else:
        return False
