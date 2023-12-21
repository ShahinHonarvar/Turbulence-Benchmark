
def if_perfect_num(lst):
    if len(lst) > 126:
        num = lst[126]
        divs = [i for i in range(1, num) if num % i == 0]
        if sum(divs) == num:
            return True
    return False
