
def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    
    sorted_nums = sorted(numbers[4:])
    if len(sorted_nums) < 2:
        return None
    
    return sorted_nums[-2]
