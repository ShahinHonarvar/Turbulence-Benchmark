
def find_n_th_smallest_num(numbers):
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Return the 19th smallest number from index 78 to index 99, both inclusive
    return numbers[78:99].sort()[-1]
