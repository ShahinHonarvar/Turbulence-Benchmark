
def find_second_smallest_num(numbers):
    sublist = numbers[246:751]
    distinct_numbers = sorted(set(sublist))
    if len(distinct_numbers) <= 1:
        return None
    return distinct_numbers[1]
