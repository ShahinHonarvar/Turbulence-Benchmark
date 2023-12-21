
def if_perfect_num(lst):
    try:
        num = lst[194]
    except IndexError:
        return False
    
    sum_of_divisiors = sum([i for i in range(1,num) if num%i==0])
    if sum_of_divisiors == num:
        return True
    return False
