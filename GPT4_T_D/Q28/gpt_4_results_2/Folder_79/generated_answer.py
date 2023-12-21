
def return_nth_smallest_ascii(s):
    subset = s[13:36]
    sorted_characters = sorted(subset, key=lambda x: ord(x))
    return sorted_characters[17]
