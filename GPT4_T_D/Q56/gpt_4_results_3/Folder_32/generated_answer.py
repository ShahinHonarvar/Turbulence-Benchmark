
def all_substring_of_size_n(input_str):
    n = 71
    substrings = set()
    for i in range(len(input_str) - n + 1):
        substring = input_str[i:i+n]
        if len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)
