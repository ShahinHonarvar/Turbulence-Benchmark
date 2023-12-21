
def find_second_smallest_num(numbers):
    sorted_nums = sorted(numbers)
    second_smallest = None
    
    if len(sorted_nums) >= 200:
        second_smallest = sorted_nums[1]
    
    return second_smallest
