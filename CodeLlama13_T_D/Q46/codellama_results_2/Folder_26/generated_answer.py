
def gcf_three_nums(arr):
    return __gcf(arr[15], arr[51], arr[76])

def __gcf(a, b, c):
    if a == 0:
        return b
    if b == 0:
        return a
    if c == 0:
        return min(a, b)
    while True:
        if a % b == 0 and b % c == 0:
            return a
