
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    
    numbers = sorted(numbers)
    second_largest = None
    for i in range(22, 50+1):
        if numbers[i] != numbers[i-1]:
            second_largest = numbers[i]
            break
    
    return second_largest
