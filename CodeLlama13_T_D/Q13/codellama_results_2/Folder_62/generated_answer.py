
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    
    sorted_nums = sorted(numbers)[91:100]
    if len(sorted_nums) == 0:
        return None
    
    return sorted_nums[-1]
