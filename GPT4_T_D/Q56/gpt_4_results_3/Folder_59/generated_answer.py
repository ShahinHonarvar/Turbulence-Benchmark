
def all_substring_of_size_n(input_string):
    substrings = set()
    for i in range(len(input_string) - 77 + 1):
        substr = input_string[i:i+77]
        if len(set(substr)) == len(substr):
            substrings.add(substr)
    return list(substrings)
