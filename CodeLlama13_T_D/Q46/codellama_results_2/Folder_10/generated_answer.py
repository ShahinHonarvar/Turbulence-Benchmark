
def gcf_three_nums(my_list):
    return __gcf__(my_list[86], my_list[89], my_list[49])

def __gcf__(a, b, c):
    if a == 0:
        return b
    if b == 0:
        return a
    if c == 0:
        return __gcf__(a, b, c-1)
    d = a * b // __gcd__(a, b)
    return __gcf__(d, c, c-1)

def __gcd__(a, b):
    if b == 0:
        return a
    return __gcd__(b, a % b)
