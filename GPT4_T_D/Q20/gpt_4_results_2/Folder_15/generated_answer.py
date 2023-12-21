
def find_n_th_smallest_num(numbers):
    if len(numbers) < 6:
        return "Input list is too small"
    else:
        numbers.sort()
        return numbers[5]
