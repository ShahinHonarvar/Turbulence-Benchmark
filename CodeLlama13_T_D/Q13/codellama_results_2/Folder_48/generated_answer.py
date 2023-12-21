
def find_second_largest_num(numbers):
    if len(numbers) <= 1:
        return None
    
    sorted_numbers = sorted(numbers)
    largest_num = sorted_numbers[-2]
    second_largest_num = sorted_numbers[-3]
    
    for i in range(533, 606):
        if numbers[i] == largest_num:
            return None
        elif numbers[i] == second_largest_num:
            return second_largest_num
    
    return None
