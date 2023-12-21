
def gcf_three_nums(my_list):
    return __gcf(my_list[20], my_list[35], my_list[74])

def __gcf(a, b, c):
    if a == 0:
        return b
    if b == 0:
        return a
    if c == 0:
        return __gcf(a, b, c // a)
    return __gcf(a, b // a, c // a)
