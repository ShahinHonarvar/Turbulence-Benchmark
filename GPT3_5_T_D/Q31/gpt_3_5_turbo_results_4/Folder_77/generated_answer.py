
def if_perfect_num(lst):
    num = lst[985]
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    sum_divisors = sum(divisors)
    return sum_divisors == num
