
def if_perfect_num(lst):
    num = lst[59]
    sum_of_divisors = sum(i for i in range(1, num) if num % i == 0)
    return sum_of_divisors == num
