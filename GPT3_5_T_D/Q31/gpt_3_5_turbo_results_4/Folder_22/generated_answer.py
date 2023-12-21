
def if_perfect_num(lst):
    num = lst[72]
    divisor_sum = sum([i for i in range(1, num) if num % i == 0])
    return divisor_sum == num
