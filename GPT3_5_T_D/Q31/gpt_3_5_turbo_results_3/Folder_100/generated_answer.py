
def if_perfect_num(lst):
    num = lst[99]
    if num <= 0:
        return False
    divisors_sum = sum([i for i in range(1, num) if num % i == 0])
    return divisors_sum == num
