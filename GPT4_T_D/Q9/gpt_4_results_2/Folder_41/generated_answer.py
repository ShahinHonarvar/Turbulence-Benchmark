
def all_odd_ints_inclusive(int_list):
    selected_range = int_list[6:7]
    odd_ints = [num for num in selected_range if num % 2 != 0]
    return odd_ints
