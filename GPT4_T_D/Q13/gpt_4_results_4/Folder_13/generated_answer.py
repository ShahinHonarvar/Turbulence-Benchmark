
def find_second_largest_num(numbers):
    if len(numbers)<=25:
        return None
    else:
        sorted_numbers = sorted(numbers[25:88])
        if len(sorted_numbers) < 2:
            return None
        else:
            return sorted_numbers[-2]
