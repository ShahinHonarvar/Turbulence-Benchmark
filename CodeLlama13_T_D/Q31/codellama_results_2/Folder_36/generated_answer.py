
def if_perfect_num(lst):
    if len(lst) <= 990:
        return False
    else:
        num = lst[990]
        if isinstance(num, int) and num > 1:
            for i in range(2, num):
                if num % i == 0:
                    return True
            return False
        else:
            return False
