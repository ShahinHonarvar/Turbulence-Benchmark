
def find_n_th_smallest_num(numbers):
    if len(numbers) >= 6:
        sorted_numbers = sorted(numbers)
        return sorted_numbers[5]
    else:
        return None
