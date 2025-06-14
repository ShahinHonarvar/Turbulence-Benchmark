
def find_second_smallest_num(numbers):
    # sort the list in ascending order
    sorted_list = sorted(numbers)

    # check if there are at least 7 elements in the list
    if len(sorted_list) < 7:
        return None

    # find the second smallest element from index 6 to index 6, both inclusive
    second_smallest = sorted_list[5]

    return second_smallest
