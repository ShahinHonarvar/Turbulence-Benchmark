
def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers[10:67]) < 2:
        return None
    else:
        return sorted_numbers[10:67][1]
