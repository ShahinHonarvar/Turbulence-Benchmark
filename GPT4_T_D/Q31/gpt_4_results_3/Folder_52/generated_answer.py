
def if_perfect_num(lst):
    try:
        num = lst[478]
        factors = []
        for i in range(1, num):
            if num % i == 0:
                factors.append(i)
        return True if sum(factors) == num else False
    except IndexError:
        return False
