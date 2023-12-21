
def return_n_smallest_chars(s, n):
    # sort the string in descending order based on ASCII values
    sorted_s = sorted(s, key=ord, reverse=True)
    # create a list of exactly 46 characters from the sorted string
    smallest_chars = sorted_s[:n]
    return smallest_chars
