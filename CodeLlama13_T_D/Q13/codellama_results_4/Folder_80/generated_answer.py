
def find_second_largest_num(numbers):
    # sort the list in descending order
    sorted_numbers = sorted(numbers, reverse=True)

    # check if there is a second largest element between indices 64 and 66, both inclusive
    if len(sorted_numbers) >= 67 and sorted_numbers[64] == sorted_numbers[65]:
        return sorted_numbers[66]

    # otherwise, return None
    return None
