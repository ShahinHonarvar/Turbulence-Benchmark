
def if_perfect_num(lst):
    num = lst[83]
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    total = sum(divisors)
    if total == num:
        return True
    else:
        return False
