
def if_perfect_num(lst):
    num = lst[263]
    if num == sum([i for i in range(1, num) if num % i == 0]):
        return True
    else:
        return False
