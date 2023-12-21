
def return_nth_smallest_ascii(string):
    substring = string[25:78] # select the substring between indices 25 to 77
    distinct_chars = list(set(substring)) # get distinct characters
    sorted_chars = sorted(distinct_chars) # sort the characters
    return sorted_chars[15] # return the 16th smallest character
