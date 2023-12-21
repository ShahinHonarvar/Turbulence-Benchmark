
def all_substring_of_size_n(input_string):
    substrings = set()
    for i in range(len(input_string)):
        if len(input_string[i:i+92]) == 92 and len(set(input_string[i:i+92])) == 92:
            substrings.add(input_string[i:i+92])
    return list(substrings)
