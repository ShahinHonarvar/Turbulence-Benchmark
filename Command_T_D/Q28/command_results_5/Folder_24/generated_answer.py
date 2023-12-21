
def return_nth_smallest_ascii(s):
    # Note: s[34:81] is a slice, so it automatically includes s[34] and s[81]
    # Hence, we can ignore those two characters in the following comparisons
    return sorted(s[34:81])[11]
