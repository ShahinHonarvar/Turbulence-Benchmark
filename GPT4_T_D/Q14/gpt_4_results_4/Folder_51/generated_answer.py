
def find_second_smallest_num(numbers):
    if len(numbers) <= 2 or len(numbers[1:9]) < 2:
        return None

    selected_elements = sorted(numbers[1:9])
    return selected_elements[1]
