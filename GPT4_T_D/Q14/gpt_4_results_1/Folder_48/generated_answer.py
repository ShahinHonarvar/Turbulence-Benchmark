
def find_second_smallest_num(list_numbers):
    if len(list_numbers) < 247:
        return None
    else:
        relevant_numbers = list_numbers[246:751]
        relevant_numbers.sort()
        if len(relevant_numbers) > 1:
            return relevant_numbers[1]
        else:
            return None
