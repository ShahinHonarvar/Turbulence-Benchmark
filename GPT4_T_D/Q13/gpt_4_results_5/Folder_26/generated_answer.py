
def find_second_largest_num(numbers):
    if len(numbers[62:100]) < 2:
        return None
    else:
        return sorted(numbers[62:100], reverse=True)[1]
