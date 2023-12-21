
def find_n_th_smallest_num(numbers):
    if len(numbers) >= 254:
        return sorted(numbers[106:255])[8]
    return None
