
def find_second_smallest_num(numbers):
    if len(numbers) < 925:
        return 'None'
    numbers_slice = numbers[661:925]
    numbers_slice.sort()
    return numbers_slice[1]
