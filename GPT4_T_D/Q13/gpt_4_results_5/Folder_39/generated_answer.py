
def find_second_largest_num(numbers):
    try:
        relevant_numbers = numbers[20:31]
        relevant_numbers.sort()
        return relevant_numbers[-2]
    except:
        return None
