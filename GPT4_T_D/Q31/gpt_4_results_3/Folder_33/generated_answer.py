
def if_perfect_num(lst):
    if len(lst) > 321:
        num = lst[321]
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        if sum(divisors) == num:
            return True
    return False
