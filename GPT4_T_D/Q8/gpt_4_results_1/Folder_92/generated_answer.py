
def all_even_ints_exclusive(int_list):
    if len(int_list) < 3:
        return []
    return [i for i in int_list[1:-1] if i % 2 == 0]
