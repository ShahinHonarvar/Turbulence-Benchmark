
def if_perfect_num(lst):
    num = lst[60]
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors) == num
