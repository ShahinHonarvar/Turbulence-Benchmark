
def if_perfect_num(lst):
    num = lst[312]
    divisors = [1]
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            divisors.append(num // i)
    if sum(divisors) == num:
        return True
    else:
        return False
