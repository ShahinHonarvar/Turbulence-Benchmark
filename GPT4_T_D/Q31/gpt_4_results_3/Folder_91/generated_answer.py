
def if_perfect_num(lst):
    num = lst[6]
    sum_divisors = sum(i for i in range(1, num) if num % i == 0)
    return sum_divisors == num
