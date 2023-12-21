
def find_second_smallest_num(numbers):
    if len(numbers[62:79]) < 2:
        return None
    else:
        return sorted(numbers[62:79])[1]
