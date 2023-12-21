
def find_second_smallest_num(numbers):
    if len(numbers) < 88:
        return None
    distinct_numbers = list(set(numbers))
    distinct_numbers.sort()
    if len(distinct_numbers) < 2:
        return None
    return distinct_numbers[1]
