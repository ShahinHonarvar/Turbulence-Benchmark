
def find_second_smallest_num(numbers):
    if len(numbers) <= 50:
        return None
    
    sorted_numbers = sorted(numbers[50:201])
    
    second_smallest = None
    for i in range(len(sorted_numbers)):
        if sorted_numbers[i] != sorted_numbers[i-1]:
            second_smallest = sorted_numbers[i]
            break
        
    return second_smallest
