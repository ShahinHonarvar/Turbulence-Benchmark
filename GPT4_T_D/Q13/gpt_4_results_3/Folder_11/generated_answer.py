
def find_second_largest_num(numbers):
    if not numbers or len(numbers) < 52:
        return None
    relevant_numbers = sorted(numbers[37:52], reverse=True)
    if len(relevant_numbers) > 1:
        return relevant_numbers[1]
    else:
        return None
