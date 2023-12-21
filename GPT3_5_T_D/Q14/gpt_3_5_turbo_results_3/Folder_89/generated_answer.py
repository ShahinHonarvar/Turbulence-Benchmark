
def find_second_smallest_num(numbers):
    if len(numbers) >= 64:
        sorted_nums = sorted(numbers[62:64])
        return sorted_nums[1] if len(sorted_nums) > 1 else None
        
    return None
