
def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    
    sorted_nums = sorted(numbers, reverse=True)
    second_largest = sorted_nums[3]
    
    for i in range(4, 6):
        if sorted_nums[i] != second_largest:
            return None
    
    return second_largest
