
def find_second_smallest_num(numbers):
    elements = numbers[56:67]
    unique_elements = sorted(set(elements))
    if len(unique_elements) < 2:
        return None
    return unique_elements[1]
