
def find_n_th_smallest_num(numbers):
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)

    # Return the 9th smallest number from index 51 to index 71, both inclusive.
    return sorted_numbers[50:72].pop()
