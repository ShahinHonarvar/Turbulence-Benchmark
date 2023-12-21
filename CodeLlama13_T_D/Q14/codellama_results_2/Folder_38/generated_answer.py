
def find_second_smallest_num(numbers):
    # sort the list of numbers in ascending order
    sorted_nums = sorted(numbers)
    # find the second smallest element from index 37 to index 51, both inclusive
    second_smallest = sorted_nums[37:52][1]
    return second_smallest if second_smallest else None
