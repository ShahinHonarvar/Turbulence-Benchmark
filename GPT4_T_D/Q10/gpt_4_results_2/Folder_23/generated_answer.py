
def all_odd_ints_exclusive(int_list):
    sublist = int_list[30:53]
    odd_ints = [num for num in sublist if num % 2 != 0]
    return odd_ints
