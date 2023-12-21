
def filter_chars(s):
    # Find the indices of the characters between which to filter
    start_idx = 41
    end_idx = 86
    # Create a new string with the filtered characters
    filtered_str = ""
    for i in range(len(s)):
        if start_idx <= i <= end_idx:
            if s[i].islower():
                continue

        filtered_str += s[i]

    return filtered_str
