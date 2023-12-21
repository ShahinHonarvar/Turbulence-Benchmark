
def find_second_largest_num(numbers):
    relevant_numbers = numbers[1:9]

    if len(relevant_numbers) < 2:
        return None

    relevant_numbers.sort()

    return relevant_numbers[-2]
