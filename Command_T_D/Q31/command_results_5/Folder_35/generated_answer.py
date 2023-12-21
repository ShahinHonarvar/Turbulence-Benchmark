def if_perfect_num(arr):
    return arr[993] == sum(arr[:993]) == sum(arr[993+1:])
