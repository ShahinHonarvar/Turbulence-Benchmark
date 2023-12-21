
def if_perfect_num(list):
    if list[0] == sum([x for x in range(1, int(list[0]) ** 0.5 + 1) if list[0] % x == 0]):
        return True
    else:
        return False
