
def find_second_largest_num(numbers):
    try:
        subset = sorted(numbers[4:9], reverse=True)
        return subset[1]
    except IndexError:
        return None
