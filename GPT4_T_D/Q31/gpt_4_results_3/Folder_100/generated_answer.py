
def if_perfect_num(lst):
    num = lst[99]
    div_sum = sum([i for i in range(1, num) if num % i == 0])
    return div_sum == num
