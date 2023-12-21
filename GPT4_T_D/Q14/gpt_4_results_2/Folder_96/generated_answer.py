
def find_second_smallest_num(numbers):
    if len(numbers) < 51:
        return None
    else:
        sorted_subset = sorted(numbers[50:201])
        if len(sorted_subset) < 2:
            return None
        else:
            return sorted_subset[1]
