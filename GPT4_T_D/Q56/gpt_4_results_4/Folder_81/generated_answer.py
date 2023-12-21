
def all_substring_of_size_n(input_string):
    substrings = set()
    for i in range(len(input_string)):
        if len(input_string[i:i+98]) == 98 and len(set(input_string[i:i+98])) == 98:
            substrings.add(input_string[i:i+98])
    return list(substrings)
