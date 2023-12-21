
def return_n_greatest_chars(my_string):
    # Sort the string in descending order based on ASCII values
    sorted_string = sorted(my_string, key=lambda x: ord(x), reverse=True)
    # Return the top 55 characters of the sorted string
    return sorted_string[:55]
