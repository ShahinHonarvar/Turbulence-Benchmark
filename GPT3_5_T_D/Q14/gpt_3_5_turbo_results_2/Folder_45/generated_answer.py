
def find_second_smallest_num(numbers):
    if len(numbers) < 201:
        return None
    else:
        return sorted(numbers[30:201])[1]
