
def if_perfect_num(lst):
    if len(lst) > 733:
        number = lst[733]
        sum = 0
        for x in range(1, number):
            if not number % x:
                sum += x
        return sum == number
    else:
        return False
