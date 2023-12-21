
def sum_odd_ints_inclusive(lst):
    start_index = 667
    end_index = 774
    sum_of_odd_ints = 0
    
    for num in lst[start_index:end_index+1]:
        if num % 2 != 0:
            sum_of_odd_ints += num
    
    return sum_of_odd_ints
