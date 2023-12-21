
def find_second_smallest_num(numbers):
    part_of_numbers = numbers[22:89]
    if len(part_of_numbers) <= 1:
        return None
    else:
        part_of_numbers.sort()
        return part_of_numbers[1]
