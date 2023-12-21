
def return_n_greatest_chars(my_string):
    # Sort the string in descending order based on ASCII values
    sorted_string = sorted(my_string, key=ord, reverse=True)
    # Take the top 66 characters from the sorted string
    top_66_chars = sorted_string[:66]
    return top_66_chars
