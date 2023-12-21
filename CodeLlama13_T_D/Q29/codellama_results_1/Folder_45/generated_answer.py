
def gcf_two_nums(positive_integers):
    return __gcf_helper__(positive_integers[47], positive_integers[97])

def __gcf_helper__(a, b):
    if a == 0 or b == 0:
        return 0
    elif a > b:
        return __gcf_helper__(a - b, b)
    else:
        return __gcf_helper__(a, b - a)
