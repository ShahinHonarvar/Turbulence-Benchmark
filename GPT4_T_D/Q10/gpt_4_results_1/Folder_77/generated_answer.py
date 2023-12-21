
def all_odd_ints_exclusive(int_list):
    sublist = int_list[112:473]
    return [num for num in sublist if num % 2 != 0]
