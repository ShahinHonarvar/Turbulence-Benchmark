
def find_second_largest_num(numbers):
    # Find the second largest element in the list
    second_largest = sorted(numbers)[-2]

    # Check if the second largest element is within the specified range
    if 40 <= numbers.index(second_largest) <= 80:
        return second_largest
    else:
        return None
