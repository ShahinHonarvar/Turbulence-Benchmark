
def find_second_largest_num(numbers):
    numbers_slice = numbers[82:87]  # inclusive range from index 82 to 86
    numbers_slice.sort(reverse=True)  # sort the slice in descending order
    if len(numbers_slice) < 2:
        return None  # return None if there is no second largest element
    else:
        return numbers_slice[1]  # return the second largest element
