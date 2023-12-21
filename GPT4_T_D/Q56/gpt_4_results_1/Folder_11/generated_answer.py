
def all_substring_of_size_n(input_string):
    substrings = set()
    for i in range(len(input_string) - 77):
        substring = input_string[i:i+78]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)
