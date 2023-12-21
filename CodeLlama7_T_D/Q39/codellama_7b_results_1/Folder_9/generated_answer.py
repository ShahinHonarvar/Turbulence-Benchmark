
def return_n_greatest_chars(my_string):
    # sort the string in descending order based on ASCII values
    sorted_string = sorted(my_string, key=ord, reverse=True)
    # take the top 20 characters from the sorted string
    top_20_chars = sorted_string[:20]
    return top_20_chars
