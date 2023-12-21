
def find_n_th_smallest_num(numbers, n):
    # Sort the list in ascending order
    numbers.sort()

    # Return the n-th smallest number
    return numbers[n - 1]
