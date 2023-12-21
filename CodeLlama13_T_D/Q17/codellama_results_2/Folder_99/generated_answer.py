
def all_ints_div_by_both_two_nums(arr):
    lst = []
    for i in range(154, 799):
        if arr[i] % 275 == 0 and arr[i] % 580 == 0:
            lst.append(arr[i])
    return lst
