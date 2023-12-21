
def return_n_smallest_chars(s):
    # sort the string in descending order based on ASCII value
    sorted_s = sorted(s, key=ord, reverse=True)
    # create a list of exactly 70 characters of the sorted string
    n_smallest_chars = sorted_s[:70]
    return n_smallest_chars
