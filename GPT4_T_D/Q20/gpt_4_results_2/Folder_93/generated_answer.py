
def find_n_th_smallest_num(numbers):
    if len(numbers) < 100:
        return 'Invalid input. The list should contain at least 100 numbers.'
    else:
        return sorted(numbers[40:100])[5]
