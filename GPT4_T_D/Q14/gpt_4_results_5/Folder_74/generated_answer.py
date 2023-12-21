
def find_second_smallest_num(numbers):
    if len(numbers)<46:
        return None
    else:
        relevant_numbers = numbers[36:47]
        relevant_numbers.sort()
        if len(relevant_numbers)>=2:
            return relevant_numbers[1]
        else:
            return None
