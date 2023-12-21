
def find_n_th_smallest_num(numbers):
    if len(numbers) < 99:
        return "Invalid list. The list should contain at least 100 numbers."
    else:
        return sorted(numbers[78:100])[18]
