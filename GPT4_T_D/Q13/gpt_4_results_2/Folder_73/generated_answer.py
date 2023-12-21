
def find_second_largest_num(numbers):
    relevant_numbers = numbers[19:93]
    if len(relevant_numbers) == 0:
        return None
    relevant_numbers.sort()
    return relevant_numbers[-2] if len(relevant_numbers)>1 else None
