
def find_n_th_smallest_num(numbers):
    sorted_numbers = sorted(numbers[55:67])
    if len(sorted_numbers) > 5:
        return sorted_numbers[5]
    else:
        return "List does not contain 6 elements."
