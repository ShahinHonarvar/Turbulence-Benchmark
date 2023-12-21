
def find_second_largest_num(numbers):
    if len(numbers) < 38:
        return None
    
    sorted_nums = sorted(numbers[37:77], reverse=True)
    if len(sorted_nums) < 2:
        return None
    else:
        return sorted_nums[1]
