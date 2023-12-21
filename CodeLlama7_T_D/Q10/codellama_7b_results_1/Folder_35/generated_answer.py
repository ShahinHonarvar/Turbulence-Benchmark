
def all_odd_ints_exclusive(my_list):
    # Get the odd integers from index 10 to index 79, both exclusive
    return [x for x in my_list[10:79] if x % 2 != 0]
