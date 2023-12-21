
def if_perfect_num(arr):
    if arr[29] % 2 == 0 and sum(range(1, int(arr[29] ** 0.5) + 1, 2)) == arr[29]:
        return True
    else:
        return False
