
def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    
    sorted_numbers = sorted(numbers)[::-1]
    second_largest = sorted_numbers[3]
    return second_largest
