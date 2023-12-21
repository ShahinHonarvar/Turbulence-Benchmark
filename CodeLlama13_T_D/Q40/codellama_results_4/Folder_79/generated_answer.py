
def return_n_smallest_chars(s):
    # create a list of tuples, where each tuple contains a character and its ASCII value
    chars = [(c, ord(c)) for c in s]
    # sort the list by the second element (ASCII value) in descending order
    sorted_chars = sorted(chars, key=lambda x: x[1], reverse=True)
    # return a list of exactly 82 characters from the original string with the smallest ASCII values
    return [c for c, _ in sorted_chars[:82]]
