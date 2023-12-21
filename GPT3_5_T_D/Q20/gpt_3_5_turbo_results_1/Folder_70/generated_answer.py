
def find_n_th_smallest_num(numbers):
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Return the 4th smallest number from index 26 to index 90 (both inclusive)
    return sorted_numbers[26:91][3]
