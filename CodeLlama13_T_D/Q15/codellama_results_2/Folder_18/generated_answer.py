
def sum_odd_ints_inclusive(my_list):
    # Create a new list with all odd integers from index 35 to index 49, both inclusive
    new_list = my_list[35:50:2]

    # Use the built-in sum function to calculate the sum of the new list
    return sum(new_list) if new_list else 0
