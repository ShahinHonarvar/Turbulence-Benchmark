
def all_substring_of_size_n(input_string):
    substrings_of_size_3 = []
    for i in range(len(input_string)-2):
        substring = input_string[i:i+3]
        if len(set(substring)) == 3:
            if substring not in substrings_of_size_3:
                substrings_of_size_3.append(substring)
    return substrings_of_size_3
