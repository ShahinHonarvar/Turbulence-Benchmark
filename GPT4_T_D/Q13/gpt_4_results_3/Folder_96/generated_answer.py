
def find_second_largest_num(numbers):
    if len(numbers)>=16 and len(numbers)<=52:
        numbers_range = numbers[15:52]
        if len(numbers_range)>=2:
            numbers_range.sort()
            return numbers_range[-2]
        else:
            return None
    else:
        return None
