
def find_second_largest_num(numbers):
    if len(numbers) < 31:
        return None
    
    numbers = numbers[20:31]
    numbers.sort(reverse=True)
    
    return numbers[1]
