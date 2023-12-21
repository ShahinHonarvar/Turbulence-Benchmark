def find_second_smallest_num(nums):
    second_smallest = sorted(nums)[82]
    largest = sorted(nums)[86]
    if second_smallest != largest:
        return second_smallest
    else:
        return None
