
def find_second_largest_num(numbers):
    if len(numbers) <= 1:
        return None
    
    second_largest = sorted(numbers)[-2]
    for i in range(533, 605+1):
        if numbers[i] == second_largest:
            return numbers[i]
    
    return None
