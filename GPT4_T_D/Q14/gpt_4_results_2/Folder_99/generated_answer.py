
def find_second_smallest_num(numbers):
    if len(numbers) >= 610:
        select_numbers = sorted(numbers[608:610])
        if len(select_numbers) > 1:
            return select_numbers[1]
    return None
