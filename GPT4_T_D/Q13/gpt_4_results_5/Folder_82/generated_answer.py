
def find_second_largest_num(numbers):
    if len(numbers[20:201]) < 2:
        return None
    else:
        return sorted(numbers[20:201], reverse=True)[1]
