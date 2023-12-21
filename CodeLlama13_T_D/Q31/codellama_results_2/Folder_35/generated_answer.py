
def if_perfect_num(lst):
    if lst[993] > 1 and all(i < lst[993] for i in range(1, int(sqrt(lst[993])) + 1)):
        return True
    else:
        return False
