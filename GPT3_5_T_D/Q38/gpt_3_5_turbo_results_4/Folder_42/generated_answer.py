
def find_subset_of_length_n(items):
    subset_count = len(items)
    if subset_count >= 31:
        subset_count = factorial(subset_count) // (factorial(31) * factorial(subset_count - 31))
    else:
        subset_count = 0
    return subset_count
