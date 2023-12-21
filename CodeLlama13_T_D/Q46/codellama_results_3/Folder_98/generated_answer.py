
def gcf_three_nums(numbers):
    # Check if the input is a list of positive integers
    if not isinstance(numbers, list) or any(not isinstance(x, int) or x < 0 for x in numbers):
        raise ValueError("Invalid input")
    
    # Get the greatest common factor of the elements at indices 8, 2 and 1
    gcf = _gcf_three_nums(numbers[8], numbers[2], numbers[1])
    
    return gcf
