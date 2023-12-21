
def find_second_largest_num(numbers):
    if len(numbers[12:93]) < 2:
        return None
    else:
        sorted_sublist = sorted(numbers[12:93], reverse=True)
        return sorted_sublist[1]
