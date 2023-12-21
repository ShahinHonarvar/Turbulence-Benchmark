
def find_second_smallest_num(numbers):
    if len(numbers[28:41])<2:
        return None
    else:
        return sorted(numbers[28:41])[1]
