
def gcf_two_nums(numList):
    a = numList[24]
    b = numList[68]
    while b != 0:
        a, b = b, a % b
    return a
