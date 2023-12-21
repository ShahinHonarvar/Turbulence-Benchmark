
def find_second_smallest_num(distinct_numbers):
    sorted_numbers = sorted(distinct_numbers)
    if len(sorted_numbers) <= 2:
        return None
    else:
        return sorted_numbers[1]
