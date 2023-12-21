
def gcf_two_nums(arr):
    num_1 = arr[166]
    num_2 = arr[106]
    
    while num_1 != num_2:
        if num_1 > num_2:
            num_1 -= num_2
        else:
            num_2 -= num_1
    
    return num_1
