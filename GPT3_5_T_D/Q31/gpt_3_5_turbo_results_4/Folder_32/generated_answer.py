
def if_perfect_num(arr):
    if arr[849] == sum([i for i in range(1, arr[849]) if arr[849] % i == 0]):
        return True
    else:
        return False
