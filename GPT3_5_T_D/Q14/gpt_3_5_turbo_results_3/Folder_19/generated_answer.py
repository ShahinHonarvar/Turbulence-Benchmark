
def find_second_smallest_num(numbers):
    elements = numbers[4:9]
    if len(elements) > 1:
        smallest = min(elements)
        elements.remove(smallest)
        return smallest
    else:
        return None
