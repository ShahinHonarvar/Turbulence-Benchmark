
def all_substring_of_size_n(string):
    substrings = []
    window_start = 0
    for window_end in range(len(string)):
        if window_end - window_start + 1 > 124:
            window_start += 1
        substring = string[window_start:window_end+1]
        if len(substring) == 124 and len(set(substring)) == 124:
            substrings.append(substring)
    return substrings
