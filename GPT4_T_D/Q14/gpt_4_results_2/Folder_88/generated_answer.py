
def find_second_smallest_num(numbers):
    try:
        second_smallest = sorted(numbers[6:9])[1]
        return second_smallest
    except IndexError:
        return None
