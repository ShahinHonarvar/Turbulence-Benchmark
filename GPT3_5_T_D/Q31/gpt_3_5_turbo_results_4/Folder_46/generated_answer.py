
def if_perfect_num(lst):
    num = lst[453]
    divisors_sum = sum([i for i in range(1, num) if num % i == 0])
    return num == divisors_sum
