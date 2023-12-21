
def sum_ints_div_by_either_nums(arr):
    sum = 0
    for i in range(55, 67):
        if len(arr) > i and (arr[i] % 22 == 0 or arr[i] % 82 == 0):
            sum += arr[i]
    return sum
