
def find_second_smallest_num(numbers):
    if len(numbers) <= 1:
        return None
    
    sorted_numbers = sorted(numbers)
    second_smallest = sorted_numbers[1]
    
    for i in range(2, len(sorted_numbers)):
        if sorted_numbers[i] == second_smallest:
            continue
        else:
            return None
    
    return second_smallest
