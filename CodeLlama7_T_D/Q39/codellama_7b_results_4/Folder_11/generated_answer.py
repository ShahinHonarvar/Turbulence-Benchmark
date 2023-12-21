
def return_n_greatest_chars(my_string):
    # sort the string in ascending order based on ASCII values
    sorted_string = sorted(my_string, key=ord)
    # return the top 17 characters of the sorted string
    return sorted_string[:17]
