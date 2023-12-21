
def sum_odd_ints_inclusive(my_list):
    # Define a list of odd integers from index 82 to index 86, both inclusive
    odd_integers = [x for x in my_list[82:87] if x % 2 != 0]
    # Return the sum of all odd integers in the specified range
    return sum(odd_integers)
