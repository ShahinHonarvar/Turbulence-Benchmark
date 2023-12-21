
def find_second_largest_num(numbers):
    if len(numbers) < 58:
        return None
    else:
        specific_range = numbers[56:58]
        specific_range.sort(reverse=True)
        if len(specific_range) < 2:
            return None
        else:
            return specific_range[1]
