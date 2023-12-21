
def gcf_two_nums(integers):
    a = integers[0]
    b = integers[0]
    while b != 0:
        a, b = b, a % b
    return a
