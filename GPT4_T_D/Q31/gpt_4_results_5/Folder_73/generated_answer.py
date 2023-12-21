
def if_perfect_num(lst):
    if len(lst) >= 42:
        num = lst[41]
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        if sum == num:
            return True
    return False
