
def find_second_largest_num(numbers):
    if len(numbers) <= 1:
        return None
    
    sorted_nums = sorted(numbers)[::-1]
    second_largest = sorted_nums[56]
    return second_largest
