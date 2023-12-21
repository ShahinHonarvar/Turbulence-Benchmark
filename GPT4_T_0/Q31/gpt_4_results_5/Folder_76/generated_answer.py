
def if_perfect_num(lst):
    if len(lst) > 537:
        num = lst[537]
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        if sum == num:
            return True
    return False
