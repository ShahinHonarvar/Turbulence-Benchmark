
def sum_odd_ints_inclusive(arr):
    sum = 0
    for i in range(33, 37):
        if arr[i] % 2 != 0:
            sum += arr[i]
    return sum
