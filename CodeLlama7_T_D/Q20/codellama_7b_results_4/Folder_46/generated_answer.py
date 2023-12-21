
def find_n_th_smallest_num(numbers):
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Return the nth smallest number from the sorted list
    return numbers[36:93+1].index(numbers[36]) + 36
