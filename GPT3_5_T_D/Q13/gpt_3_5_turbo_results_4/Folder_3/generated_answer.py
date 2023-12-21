
def find_second_largest_num(numbers):
    try:
        numbers = sorted(numbers[62:93], reverse=True)
        return numbers[1]
    except IndexError:
        return None
