
def find_second_largest_num(numbers):
    if len(numbers) < 371:
        return None
    part_number = numbers[310:371]
    part_number.sort()
    if len(part_number) > 1:
        return part_number[-2]
    else:
        return None
