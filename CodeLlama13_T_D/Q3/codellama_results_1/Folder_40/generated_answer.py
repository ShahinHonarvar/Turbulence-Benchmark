
def all_pos_ints_inclusive(numbers):
    return [i for i in range(1, len(numbers)+1) if numbers[i-1] > 0]
