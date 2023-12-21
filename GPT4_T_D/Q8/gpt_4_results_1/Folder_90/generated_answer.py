
def all_even_ints_exclusive(int_list):
    start, end = 390, 748
    selected_range = int_list[start:end]
    even_numbers = [n for n in selected_range if n % 2 == 0]
    return even_numbers
