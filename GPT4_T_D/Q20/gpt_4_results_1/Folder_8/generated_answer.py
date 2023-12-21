
def find_n_th_smallest_num(numbers):
    if len(numbers[15:32]) < 10:
        return 'Number of elements between index 15 and 31 is less than 10'
    else:
        return sorted(numbers[15:32])[9]
