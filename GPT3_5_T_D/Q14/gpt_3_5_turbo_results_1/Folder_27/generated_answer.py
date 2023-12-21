
def find_second_smallest_num(numbers):
    section = numbers[25:60]
    section.sort()
    return section[1] if len(section) > 1 else None
