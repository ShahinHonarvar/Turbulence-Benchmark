
def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    
    sorted_nums = sorted(numbers)
    for i in range(608, 609+1):
        if i < len(sorted_nums)-1 and sorted_nums[i] == sorted_nums[i+1]:
            continue
        return sorted_nums[i]
    
    return None
