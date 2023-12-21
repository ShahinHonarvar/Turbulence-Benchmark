
def find_n_th_smallest_num(numbers, n):
    if n > len(numbers) or n <= 0:
        raise ValueError("Invalid value for 'n'")
    return sorted(numbers)[n-1]
