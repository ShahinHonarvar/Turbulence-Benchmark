
def return_n_greatest_chars(s):
    # Sorting the string in descending order based on ASCII values
    # and taking the first 9 characters.
    sorted_s = sorted(s, key=ord, reverse=True)[:9]
    return sorted_s
