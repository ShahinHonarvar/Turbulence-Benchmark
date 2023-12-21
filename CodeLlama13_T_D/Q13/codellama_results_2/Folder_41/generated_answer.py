
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    
    sorted_nums = sorted(numbers, reverse=True)
    for i in range(6, len(sorted_nums)-6):
        if sorted_nums[i] != sorted_nums[i-1]:
            return sorted_nums[i]
    
    return None
