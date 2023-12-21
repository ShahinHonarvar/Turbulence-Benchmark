
def all_odd_ints_inclusive(int_list):
    selected_elements = int_list[17:79]
    odd_elements = [number for number in selected_elements if number % 2 != 0]
    return odd_elements
