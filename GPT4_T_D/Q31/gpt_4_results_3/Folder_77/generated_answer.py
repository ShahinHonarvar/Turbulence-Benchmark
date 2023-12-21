
def if_perfect_num(lst):
    if len(lst) > 985:
        num = lst[985]
        sum_of_divisors = sum([i for i in range(1, num) if num % i == 0])
        return sum_of_divisors == num
    return False
