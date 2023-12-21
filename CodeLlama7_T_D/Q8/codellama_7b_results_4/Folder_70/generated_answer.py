
def all_even_ints_exclusive(my_list):
    # create a slice of the list from index 38 to 81, exclusive
    even_ints = my_list[38:81]
    # filter out any odd integers
    even_ints = [i for i in even_ints if i % 2 == 0]
    return even_ints
