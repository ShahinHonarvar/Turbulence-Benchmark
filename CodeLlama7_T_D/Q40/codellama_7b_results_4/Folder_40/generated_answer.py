
def return_n_smallest_chars(input_string):
    # Sort the input string in ascending order based on ASCII value
    sorted_string = sorted(input_string, key=lambda x: ord(x))
    # Return the top 7 characters of the sorted string
    return sorted_string[:7]
