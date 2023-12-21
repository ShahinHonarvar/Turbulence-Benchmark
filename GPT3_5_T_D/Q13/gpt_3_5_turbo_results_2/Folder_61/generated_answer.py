
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    
    numbers.sort(reverse=True)
    
    if len(numbers) < 8:
        return numbers[-1]
    else:
        return numbers[7]
