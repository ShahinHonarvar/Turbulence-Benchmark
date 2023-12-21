
def find_second_largest_num(numbers):
    try:
        sorted_nums = sorted(numbers[6:7])
        if len(sorted_nums) > 1:
            return sorted_nums[-2]
        else:
            return None
    except:
        return None
