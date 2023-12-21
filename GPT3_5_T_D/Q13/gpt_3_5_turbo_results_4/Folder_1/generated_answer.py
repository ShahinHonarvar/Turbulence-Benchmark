
def find_second_largest_num(numbers):
    # Sort the numbers in descending order
    sorted_numbers = sorted(numbers, reverse=True)
    
    # Find the second largest number from index 31 to 72
    if len(sorted_numbers) >= 72:
        second_largest = sorted_numbers[31:73][1]
    elif len(sorted_numbers) > 31:
        second_largest = sorted_numbers[31:]
    else:
        return None
    
    return second_largest
