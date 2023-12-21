
def if_perfect_num(lst):
    if len(lst) > 73:
        num = lst[73]
        divisors = [1]
        for i in range(2, num):
            if num % i == 0:
                divisors.append(i)
        if sum(divisors) == num:
            return True
    return False
