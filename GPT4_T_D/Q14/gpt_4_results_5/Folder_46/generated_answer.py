
def find_second_smallest_num(numbers):
    if len(numbers) >= 14:
        sorted_elements = sorted(numbers[13:69])
        try:
            return sorted_elements[1]
        except IndexError:
            return None
    else:
        return None
