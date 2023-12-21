
def if_perfect_num(lst):
    num = lst[162]
    if sum(i for i in range(1, num) if num % i == 0) == num:
        return True
    else:
        return False
