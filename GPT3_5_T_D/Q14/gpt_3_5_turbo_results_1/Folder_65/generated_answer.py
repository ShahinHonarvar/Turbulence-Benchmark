
def find_second_smallest_num(numbers):
    numbers_slice = numbers[56:58]
    sorted_slice = sorted(numbers_slice)
    
    if len(sorted_slice) > 1:
        return sorted_slice[1]
    else:
        return None
