
def all_substring_of_size_n(input_string):
    substrings = []
    for i in range(len(input_string)):
        if i+42 <= len(input_string):
            substring = input_string[i:i+42]
            if len(set(substring)) == len(substring):
                substrings.append(substring)
    return list(set(substrings))
