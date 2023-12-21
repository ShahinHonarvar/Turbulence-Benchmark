
def sum_odd_ints_inclusive(my_list):
    # Initialize an empty list to store the odd integers from index 0 to index 6, both inclusive
    odd_integers = []

    # Iterate through the list and append only the odd integers to the 'odd_integers' list
    for i in range(len(my_list)):
        if my_list[i] % 2 != 0:
            odd_integers.append(my_list[i])

    # Return the sum of all the odd integers from index 0 to index 6, both inclusive
    return sum(odd_integers)
