
def all_odd_ints_inclusive(list_of_ints):
    odd_ints = [int for int in list_of_ints[0:8] if int % 2 != 0]
    return odd_ints
