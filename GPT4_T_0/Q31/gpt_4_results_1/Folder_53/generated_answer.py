
def if_perfect_num(lst):
    if len(lst) > 73:
        num = lst[73]
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        if sum == num:
            return True
        else:
            return False
    else:
        return False
