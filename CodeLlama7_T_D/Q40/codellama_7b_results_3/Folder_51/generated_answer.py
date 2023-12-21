
def return_n_smallest_chars(input_string):
    # Sort the input string in descending order based on ASCII value
    sorted_string = sorted(input_string, key=lambda x: ord(x), reverse=True)
    # Create a list of exactly 45 characters from the sorted string
    n_smallest_chars = sorted_string[:45]
    return n_smallest_chars
