
def all_odd_ints_exclusive(int_list):
    return [num for idx, num in enumerate(int_list[1:7]) if num % 2 != 0]
