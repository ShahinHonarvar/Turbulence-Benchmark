
def if_perfect_num(lst):
    num = lst[74]
    sum_div = sum([i for i in range(1, num) if num % i == 0])
    return True if sum_div == num else False  
