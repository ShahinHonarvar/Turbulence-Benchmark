
def return_n_greatest_chars(my_string, n):
    # sort the string in descending order based on ASCII values
    sorted_string = sorted(my_string, key=ord, reverse=True)
    # return the top n characters of the sorted string
    return sorted_string[:n]
