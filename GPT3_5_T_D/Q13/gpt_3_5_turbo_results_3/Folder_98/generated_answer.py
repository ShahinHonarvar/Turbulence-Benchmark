
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
        
    first = float('-inf')
    second = float('-inf')
    
    for num in numbers[:7]:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    if second == float('-inf'):
        return None
    else:
        return second
