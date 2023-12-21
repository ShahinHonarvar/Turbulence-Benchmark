
def find_largest_num(numbers):
    try:
        return max(numbers[111:112])
    except IndexError:
        return 'Error: Index out of range'
