
def all_odd_ints_inclusive(lst):
    start_index = 22
    end_index = 50
    
    odd_ints = []
    for i in range(start_index, end_index+1):
        if lst[i] % 2 != 0:
            odd_ints.append(lst[i])
    
    return odd_ints
