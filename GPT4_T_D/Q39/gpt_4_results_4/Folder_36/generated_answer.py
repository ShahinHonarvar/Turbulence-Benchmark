
def return_n_greatest_chars(s):
    sorted_characters = sorted(s, key=ord, reverse=True)
    return sorted(sorted_characters[:32])
