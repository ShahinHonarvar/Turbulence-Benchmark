
def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers[10:101])
    
    if len(sorted_numbers) > 1:
        return sorted_numbers[1]
    else:
        return None
