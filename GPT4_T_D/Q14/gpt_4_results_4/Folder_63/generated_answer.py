
def find_second_smallest_num(num_list):
    if len(num_list) <= 1 or len(num_list[56:83]) <= 1:
        return None
    else:
        sliced_list = sorted(num_list[56:83])
        return sliced_list[1]
