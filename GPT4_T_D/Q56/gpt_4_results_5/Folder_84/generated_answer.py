
def all_substring_of_size_n(input_string):
    len_string = len(input_string)
    substrings = []
    for i in range(0, len_string):
        if i + 114 <= len_string:
            substring = input_string[i:i+114]
            if len(set(substring)) == len(substring):
                substrings.append(substring)
    return list(set(substrings))
