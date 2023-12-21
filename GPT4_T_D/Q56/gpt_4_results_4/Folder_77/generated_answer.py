
def all_substring_of_size_n(input_string):
    substr_len = 144
    substrings = set()

    for i in range(len(input_string) - substr_len + 1):
        substr = input_string[i:i+substr_len]
        if len(set(substr)) == len(substr):
            substrings.add(substr)

    return list(substrings)
