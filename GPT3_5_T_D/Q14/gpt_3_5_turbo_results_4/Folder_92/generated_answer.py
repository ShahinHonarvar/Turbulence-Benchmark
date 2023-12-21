
def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    
    sorted_nums = sorted(numbers[:2])
    return sorted_nums[1]
