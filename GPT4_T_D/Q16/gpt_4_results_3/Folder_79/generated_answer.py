
def sum_even_ints_inclusive(int_list):
    sub_list = int_list[4:5]
    even_ints = [number for number in sub_list if number % 2 == 0]
    return sum(even_ints) if even_ints else 0
