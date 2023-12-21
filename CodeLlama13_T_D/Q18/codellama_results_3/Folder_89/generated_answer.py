
def sum_ints_div_by_either_nums(arr):
    total = 0
    for i in range(28,97):
        if arr[i]%90==0 or arr[i]%97==0:
            total+=arr[i]
    return total
