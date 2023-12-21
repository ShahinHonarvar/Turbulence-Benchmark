
def find_second_smallest_num(numbers):
    if len(numbers) > 80:
        selected_range = sorted(numbers[40:81])
        if len(selected_range) > 1:
            return selected_range[1]
        else:
            return None
    else:
        return None
