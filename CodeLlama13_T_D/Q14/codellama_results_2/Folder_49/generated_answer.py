
def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    
    second_smallest = numbers[1]
    for i in range(80, 200):
        num = numbers[i]
        if num < second_smallest:
            second_smallest = num
            
    return second_smallest
