
def all_substring_of_size_n(input_string):
    substrings = []
    for i in range(len(input_string) - 72):
        substring = input_string[i:i+73]
        if len(set(substring)) == 73:
            if substring not in substrings:
                substrings.append(substring)
    return substrings
