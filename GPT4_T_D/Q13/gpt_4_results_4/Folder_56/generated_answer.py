
def find_second_largest_num(numbers):
    if len(numbers) == 0:
        return None
    else:
        return sorted(numbers)[0]
