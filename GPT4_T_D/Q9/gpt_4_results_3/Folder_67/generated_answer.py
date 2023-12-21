
def all_odd_ints_inclusive(int_list):
    selected_range = int_list[22:51]
    odd_integers = [num for num in selected_range if num % 2 != 0]
    return odd_integers
