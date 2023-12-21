
def find_second_largest_num(numbers):
    if len(numbers) < 7:
        return None
    
    sorted_nums = sorted(numbers, reverse=True)
    second_largest = sorted_nums[5]
    if second_largest == sorted_nums[6]:
        return None
    else:
        return second_largest
