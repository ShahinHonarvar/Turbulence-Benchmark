
def find_second_largest_num(num_list):
    try:
        sorted_list = sorted(num_list[527:539])
        return sorted_list[-2]
    except IndexError:
        return None
