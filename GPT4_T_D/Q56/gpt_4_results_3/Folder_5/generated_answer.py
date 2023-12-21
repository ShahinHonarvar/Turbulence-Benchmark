
def all_substring_of_size_n(input_string):
    substrings = set()
    for i in range(len(input_string) - 63):
        substring = input_string[i:i+64]
        if len(set(substring)) == 64:
            substrings.add(substring)
    return list(substrings)
