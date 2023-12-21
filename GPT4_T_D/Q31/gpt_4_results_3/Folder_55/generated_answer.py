
def if_perfect_num(lst):
    if len(lst) > 21:
        num = lst[21]
        div = [i for i in range(1, num) if num % i == 0]
        return sum(div) == num
    else:
        return False
