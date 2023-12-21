
def find_second_largest_num(numbers):
    subset = numbers[31:73]
    if len(subset) <= 1:
        return None
    largest = max(subset)
    subset.remove(largest)
    second_largest = max(subset)
    return second_largest
