
def find_second_smallest_num(numbers):
    if len(numbers) <= 1:
        return None
    
    sorted_numbers = sorted(numbers)
    second_smallest_num = None
    
    for i in range(20, 31):
        current_num = sorted_numbers[i]
        if second_smallest_num is None or current_num < second_smallest_num:
            second_smallest_num = current_num
    
    return second_smallest_num
