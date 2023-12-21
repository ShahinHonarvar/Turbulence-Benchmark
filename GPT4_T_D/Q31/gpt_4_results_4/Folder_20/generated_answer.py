
def if_perfect_num(lst):
    if len(lst) < 54:
        return "List is too short"
    else:
        num = lst[53]
        summ = 0
        for i in range(1, num):
            if num % i == 0:
                summ += i
        return summ == num
