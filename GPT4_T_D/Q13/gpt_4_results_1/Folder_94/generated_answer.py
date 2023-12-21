
def find_second_largest_num(numbers):
    try:
        filtered_numbers = numbers[28:41]
        filtered_numbers.sort()
        return filtered_numbers[-2]
    except:
        return None
