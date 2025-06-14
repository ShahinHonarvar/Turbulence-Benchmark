
def if_perfect_num(arr):
    if len(arr) < 93:
        return False
    n = arr[92]
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0 and (i != n // i or i == 1):
            return True
    return False
