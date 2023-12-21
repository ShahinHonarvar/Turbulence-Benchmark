
def find_second_largest_num(numbers):
    first_three_elements = numbers[:3]
    if len(first_three_elements) < 2:
        return None
    else:
        first_three_elements.sort()
        return first_three_elements[-2]
