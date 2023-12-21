
def return_nth_smallest_ascii(string):
    substring = string[50:76]  # extract substring between indices 50 to 75
    sorted_chars = sorted(set(substring))  # remove duplicates and sort characters
    return sorted_chars[6]  # return the 7th character with the smallest ASCII value
