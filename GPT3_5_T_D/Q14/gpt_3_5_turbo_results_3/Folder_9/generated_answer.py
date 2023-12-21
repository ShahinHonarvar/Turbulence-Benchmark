
def find_second_smallest_num(numbers):
    sublist = numbers[70:201]
    unique_numbers = list(set(sublist))
    if len(unique_numbers) < 2:
        return None
    else:
        sorted_numbers = sorted(unique_numbers)
        return sorted_numbers[1]
