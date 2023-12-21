
def find_second_largest_num(numbers):
    numbers_62_to_78 = numbers[62:79]
    distinct_numbers = sorted(set(numbers_62_to_78))
    if len(distinct_numbers) < 2:
        return None
    return distinct_numbers[-2]
