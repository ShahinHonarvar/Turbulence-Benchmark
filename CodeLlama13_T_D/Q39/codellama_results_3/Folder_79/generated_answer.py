
def return_n_greatest_chars(s):
    # create a list of tuples containing each character and its ASCII value
    char_ascii = [(c, ord(c)) for c in s]

    # sort the list by the second element (ASCII value) in descending order
    char_ascii.sort(key=lambda x: x[1], reverse=True)

    # create a new list with exactly 82 characters, taking the top ASCII values from the original string
    result = [c for c, _ in char_ascii[:82]]

    return result
