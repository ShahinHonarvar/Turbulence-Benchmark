
def find_n_th_smallest_num(numbers):
    # Check if the input is a list of distinct numbers
    if not all(x != y for x in numbers for y in numbers[:x]):
        raise ValueError("Input must be a list of distinct numbers")

    # Find the 6th smallest number from index 42 to index 67, both inclusive
    return sorted(numbers[42:67+1])[5]
