
def sum_odd_ints_inclusive(int_list):
    selected_elements = int_list[4:5]
    return sum(num for num in selected_elements if num % 2 != 0)
