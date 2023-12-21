
def find_second_largest_num(numbers):
    nums_in_range = numbers[310:371]
    
    if len(nums_in_range) < 2:
        return None
    
    nums_in_range.sort(reverse=True)
    
    return nums_in_range[1]
