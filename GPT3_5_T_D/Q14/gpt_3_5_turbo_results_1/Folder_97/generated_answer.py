
def find_second_smallest_num(numbers):
    if len(numbers) < 35:
        return None
    
    sorted_nums = sorted(numbers[31:35])
    
    return sorted_nums[1] if len(sorted_nums) > 1 else None
