
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    
    sorted_numbers = sorted(numbers)[::-1]
    second_largest = sorted_numbers[8]
    
    if second_largest == numbers[-1]:
        return None
    else:
        return second_largest
