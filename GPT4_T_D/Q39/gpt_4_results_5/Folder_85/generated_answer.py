
def return_n_greatest_chars(s):
    if len(s) != 85:
        return None
    sorted_characters = sorted(s, key=ord, reverse=True)
    return sorted_characters
